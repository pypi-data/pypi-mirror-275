import numpy as np
import jax.numpy as jnp
import jax
import meshio
import h5py
from typing import List
from .Optimisers import Levenberg_Marquardt_Total
from .SBGeom_cpp import Coil_Set, Discrete_Coil, Fourier_Coil

def Coils_xyzt(Xc0, Xcn, Xsn, Yc0, Ycn, Ysn, Zc0, Zcn, Zsn,t):
    Nf = Xcn.shape[0]
    nvec = jnp.linspace(1,Nf,Nf,endpoint=True)
    xt = Xc0[0] + jnp.dot(Xcn, jnp.cos(nvec * t)) + jnp.dot(Xsn, jnp.sin(nvec * t))
    yt = Yc0[0] + jnp.dot(Ycn, jnp.cos(nvec * t)) + jnp.dot(Ysn, jnp.sin(nvec * t))
    zt = Zc0[0] + jnp.dot(Zcn, jnp.cos(nvec * t)) + jnp.dot(Zsn, jnp.sin(nvec * t))
    return jnp.array([xt,yt,zt])

def Coils_dxdydz_dt(Xc0, Xcn, Xsn, Yc0, Ycn, Ysn, Zc0, Zcn, Zsn,t):
    Nf = Xcn.shape[0]
    nvec = jnp.linspace(1,Nf,Nf,endpoint=True)
    dx_dt = jnp.dot(Xcn, -nvec * jnp.sin(nvec * t)) + jnp.dot(Xsn, nvec * jnp.cos(nvec * t))
    dy_dt = jnp.dot(Ycn, -nvec * jnp.sin(nvec * t)) + jnp.dot(Ysn, nvec * jnp.cos(nvec * t))
    dz_dt = jnp.dot(Zcn, -nvec * jnp.sin(nvec * t)) + jnp.dot(Zsn, nvec * jnp.cos(nvec * t))
    return jnp.array([dx_dt,dy_dt,dz_dt])

def Coils_dx2dy2dz2_dt2(Xc0, Xcn, Xsn, Yc0, Ycn, Ysn, Zc0, Zcn, Zsn,t):
    Nf = Xcn.shape[0]
    nvec = jnp.linspace(1,Nf,Nf,endpoint=True)
    dx2_dt2 = jnp.dot(Xcn, -nvec**2 * jnp.cos(nvec * t)) + jnp.dot(Xsn, -nvec**2 * jnp.sin(nvec * t))
    dy2_dt2 = jnp.dot(Ycn, -nvec**2 * jnp.cos(nvec * t)) + jnp.dot(Ysn, -nvec**2 * jnp.sin(nvec * t))
    dz2_dt2 = jnp.dot(Zcn, -nvec**2 * jnp.cos(nvec * t)) + jnp.dot(Zsn, -nvec**2 * jnp.sin(nvec * t))
    return jnp.array([dx2_dt2,dy2_dt2,dz2_dt2])

def Coils_Tang(Xc0, Xcn, Xsn, Yc0, Ycn, Ysn, Zc0, Zcn, Zsn,t):
    tang_vec = Coils_dxdydz_dt(Xc0, Xcn, Xsn, Yc0, Ycn, Ysn, Zc0, Zcn, Zsn,t)
    return tang_vec / jnp.sqrt(jnp.dot(tang_vec, tang_vec))


    
Coils_xyzt_vec = jax.vmap(Coils_xyzt,(None, None, None, None,None,None,None,None,None,0),0)
Coils_dxdydz_dt_vec = jax.vmap(Coils_dxdydz_dt,(None, None, None, None,None,None,None,None,None,0),0)
Coils_dx2dy2dz2_dt2_vec = jax.vmap(Coils_dx2dy2dz2_dt2,(None, None, None, None,None,None,None,None,None,0),0)
Coils_Tang_vec          = jax.vmap(Coils_Tang,(None, None, None, None,None,None,None,None,None,0),0)
dTang_dt                = jax.jacfwd(Coils_Tang,argnums = 9)

def Coils_Binorm(Xc0, Xcn, Xsn, Yc0, Ycn, Ysn, Zc0, Zcn, Zsn,t):
    dT_dt = dTang_dt(Xc0, Xcn, Xsn, Yc0, Ycn, Ysn, Zc0, Zcn, Zsn,t)
    return dT_dt / jnp.sqrt(jnp.dot(dT_dt, dT_dt))

Coils_Binorm_vec = jax.vmap(Coils_Binorm,(None, None, None, None,None,None,None,None,None,0),0)

def Coil_Error(Xc0, Xcn, Xsn, Yc0, Ycn, Ysn, Zc0, Zcn, Zsn,t, coil_xyz_data):
    return jnp.ravel(Coils_xyzt_vec(Xc0, Xcn, Xsn, Yc0, Ycn, Ysn, Zc0, Zcn, Zsn,t) - coil_xyz_data)


def Convert_to_Fourier_Coils(coilset_cpp : Coil_Set, Nf : int = 10):
    coil_fourier_args = []
    for i in range(coilset_cpp.Number_of_Coils()):
        print("Optimising coil: " , i)
        coili = coilset_cpp.Return_Coil(i)
        coil0 = coili.Return_Sampling_Curve()
        
        x0,y0, z0 = jnp.mean(coil0,axis=0)
        x0   = jnp.array([x0])
        y0   = jnp.array([y0])
        z0   = jnp.array([z0])
        xcn0 = jnp.zeros(Nf)
        xsn0 = jnp.zeros(Nf)
        ycn0 = jnp.zeros(Nf)
        ysn0 = jnp.zeros(Nf)
        zcn0 = jnp.zeros(Nf)
        zsn0 = jnp.zeros(Nf)
        t0   = jnp.linspace(0,2 * np.pi, coil0.shape[0], endpoint=False)
        args = (x0 , xcn0, xsn0, y0, ycn0,ysn0, z0, zcn0, zsn0,t0,coil0)
        args_opt = Levenberg_Marquardt_Total(Coil_Error,10,*args,lambda_k =  1.2,nu =  0.2, maxiter= 30)
        coil_fourier_args.append(args_opt[:-1])
    coils = []
    for i in range(coilset_cpp.Number_of_Coils()):        
        x0, xcn0, xsn0, y0, ycn0, ysn0, z0, zcn0, zsn0, t0 = coil_fourier_args[i]
        centre = [x0, y0, z0]
        xyz_c  = np.vstack([xcn0, ycn0, zcn0]).T
        xyz_s  = np.vstack([xsn0, ysn0, zsn0]).T
        fc     = Fourier_Coil(xyz_c, xyz_s, centre)
        coils.append(fc)
    return Coil_Set(coils)

def Save_Fourier_Coils_HDF5(coilset_cpp : Coil_Set, filename : str):
    with h5py.File(filename, "w") as f:
        f.create_dataset("Number_of_Coils", data = coilset_cpp.Number_of_Coils())
        for i in range(coilset_cpp.Number_of_Coils()):
            coil_group = f.create_group("Coil_"+str(i))
            coil_group.create_dataset("Centre",data=coilset_cpp.Return_Coil(i).Centre)
            coil_group.create_dataset("Fourier_Cos",data=coilset_cpp.Return_Coil(i).Fourier_Cos)
            coil_group.create_dataset("Fourier_Sin",data=coilset_cpp.Return_Coil(i).Fourier_Sin)


def Discrete_Coil_Set_From_HDF5(filename : str):
    with h5py.File(filename,"r") as f:
        vertices = np.array(f['Dataset1'])
    coils = []
    for i in range(vertices.shape[0]):
        coils.append(Discrete_Coil(vertices[i,:,:]))
    return Coil_Set(coils)

def Fourier_Coil_Set_From_HDF5(filename : str):
    coils = []
    with h5py.File(filename) as f:
        for i in range(np.array(f['Number_of_Coils'])):
            coili = f['Coil_' + str(i)]
            coils.append(Fourier_Coil(np.array(coili['Fourier_Cos']), np.array(coili["Fourier_Sin"]), np.array(coili["Centre"])))
    return Coil_Set(coils)

def GetCoilPoints(coil_set : Coil_Set, coil_index : int, width_phi : float, width_r : float, number_of_points : int, finite_size_type : str = "Centroid"):
    lines = coil_set.Return_Coil(coil_index).Finite_Size_Lines(width_phi, width_r, number_of_points, finite_size_type)
    
    lines_rs = lines.reshape(4,-1,3)
    lines2   = np.zeros(lines_rs.shape)
    lines2[0,:,:] = lines_rs[3,:,:]
    lines2[1,:,:] = lines_rs[1,:,:]
    lines2[2,:,:] = lines_rs[0,:,:]
    lines2[3,:,:] = lines_rs[2,:,:]
    lines_tp = lines2.transpose((1,0,2))
    return lines_tp.reshape((-1,3))