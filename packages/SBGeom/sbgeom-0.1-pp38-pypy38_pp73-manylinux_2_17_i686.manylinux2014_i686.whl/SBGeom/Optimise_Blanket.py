from .SBGeom_cpp import Flux_Surfaces, Flux_Surfaces_Normal_Extended
from .Flux_Surfaces import *
from .Optimisers import Levenberg_Marquardt_Total
from .HB_Boundary_representation import Point_Error_Unconstrained_HB, To_Rmnc_Zmns, To_Rmnc_Zmns_trunc
import jax.numpy as jnp
from typing import List
import h5py
import numpy as np
import ctypes as ct
import itertools
class Stellarator_Blanket_Optimizer:
    def __init__(self,filename_vmec : str, ntor_max : int = None, mpol_max : int = None ):
        self.flux_surfaces = Flux_Surfaces_Normal_Extended_From_HDF5(filename_vmec)
        fs_settings = self.flux_surfaces.flux_surface_settings

        mpol_opt = fs_settings.m_pol
        ntor_opt = fs_settings.n_tor
        if ntor_max:
            if ntor_max > fs_settings.n_tor:
                raise Exception("Cannot optimise for more than the number of ntor harmonics present in the original file")
            ntor_opt = ntor_max
        if mpol_max:            
            if mpol_max > fs_settings.m_pol:
                raise Exception("Cannot optimise for more than the number of mpol harmonics present in the original file")            
            mpol_opt = mpol_max

        mpol_trunc_vec = np.array([0 for i in range(ntor_opt + 1)] +  list(itertools.chain.from_iterable([[j for i in range(2 * ntor_opt + 1)] for j in range(1,mpol_opt)])),dtype=float)
        
        symm = fs_settings.symmetry
        ntor_trunc_vec = np.array([symm  * i for i in range(ntor_opt+1)] + list(itertools.chain.from_iterable([[symm * i for i in range(-ntor_opt, ntor_opt+1)] for j in range(1,mpol_opt)])))
        
        self.ntor_opt = ntor_opt
        self.mpol_opt = mpol_opt
        self.original_ntor_vec = self.flux_surfaces.n_tor_vec
        self.original_mpol_vec = self.flux_surfaces.m_pol_vec

        self.Rn0 = self.flux_surfaces.Rmnc[0,:ntor_opt + 1]
        self.Zn0 = self.flux_surfaces.Zmns[0,:ntor_opt + 1]
        self.bn0 = jnp.zeros(self.Zn0.shape[0])
        self.rho_mn0 = jnp.zeros(mpol_trunc_vec[ntor_opt+1:].shape[0])
        self.alpha = symm / 2.0        
        self.m_pol_vector      = jnp.array(mpol_trunc_vec)
        self.n_tor_vector      = jnp.array(ntor_trunc_vec)
        self.rmn_m_mpol_vector = jnp.array(mpol_trunc_vec[ntor_opt+1:])
        self.rmn_n_ntor_vector = jnp.array(ntor_trunc_vec[ntor_opt+1:])
        self.n_m0_vector       = jnp.array(ntor_trunc_vec[:ntor_opt+1])
        
        # Half module toroidal extent
        self.tor_min  = 0.0
        self.tor_max  = 2 * jnp.pi / (4.0 * self.alpha)

        self.optimizer_num = 5

        self.Rmnc_plasma = self.flux_surfaces.Rmnc
        self.Zmns_plasma = self.flux_surfaces.Zmns
        self.ui_sign     = np.sign(np.sum(self.flux_surfaces.Zmns[-1,:] * self.flux_surfaces.m_pol_vec))
                
    def Optimize_d(self,d , Nv : int, Nu : int, lambda_k : float = 0.01, nu : float = 1.8, maxiter = 10, ui_in = None):
        u = np.linspace(0, 2 * np.pi, Nu, endpoint=False)
        v = np.linspace(self.tor_min, self.tor_max, Nv)
        uu, vv = np.meshgrid(u,v)
        ui = uu.ravel()
        vi = vv.ravel()

        xyz = self.flux_surfaces.Return_Position(np.ones(ui.shape), d(ui,vi, self.flux_surfaces), ui, vi)
        
        Ri = np.sqrt(xyz[:,0]**2 + xyz[:, 1]**2)
        Zi = xyz[:,2]
        vi = np.arctan2(xyz[:,1], xyz[:,0]) # because normal vector is not exactly in orthogonal to phi, we should just take the new phi 

         
         # For some VMEC files the poloidal coordinate should be reversed... I haven't figured out what exactly, but it seems to have to do with dZ/du being different in sign
        if ui_in is None:
            usedui = ui * self.ui_sign
        else:
            usedui = ui_in
        args = (self.Rn0,
                self.Zn0,
                self.rho_mn0,
                self.bn0, 
                usedui   ,
                vi,     
                Ri, 
                Zi, 
                self.rmn_m_mpol_vector, 
                self.rmn_n_ntor_vector, 
                self.n_m0_vector, 
                self.alpha)
        
        args_new = Levenberg_Marquardt_Total(Point_Error_Unconstrained_HB,self.optimizer_num , *args, lambda_k = lambda_k, nu = 1.8, maxiter= maxiter,output=True)
        
        Rn_opt     = args_new[0]
        Zn_opt     = args_new[1]
        rho_mn_opt = args_new[2]
        bn_opt     = args_new[3]
        return To_Rmnc_Zmns_trunc(Rn_opt, Zn_opt, rho_mn_opt,bn_opt, self.original_mpol_vec, self.original_ntor_vec,self.ui_sign, self.ntor_opt, self.mpol_opt)
    
    def Optimize_d_list(self, d_func_list, Nv : int, Nu : int, lambda_k : float = 0.01, nu : float = 1.8, maxiter : int = 30, ui_in = None):
        Rmnc_list = []
        Zmns_list = []
        for i,d in enumerate(d_func_list):
            print("Optimising distance " + str(i))
            rmnc_opt, zmns_opt = self.Optimize_d(d, Nv, Nu, lambda_k, nu, maxiter, ui_in)

            Rmnc_list.append(rmnc_opt)
            Zmns_list.append(zmns_opt)
        return jnp.array(Rmnc_list), jnp.array(Zmns_list)
    
        
      