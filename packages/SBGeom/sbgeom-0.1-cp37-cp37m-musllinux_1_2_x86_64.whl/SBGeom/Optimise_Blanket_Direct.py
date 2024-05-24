from .SBGeom_cpp import Flux_Surfaces, Flux_Surfaces_Fourier_Extended, Flux_Surfaces_Normal_Extended
from .Optimisers import Levenberg_Marquardt_Total
from .HB_Boundary_representation import Point_Error_Unconstrained_HB, To_Rmnc_Zmns, To_Rmnc_Zmns_trunc
from .Flux_Surfaces import *
import jax.numpy as jnp
import jax
from typing import List
import h5py
import numpy as np
import ctypes as ct
import itertools
from scipy.interpolate import interp1d
def position_R(rmnc, ui,vi,mn_vector,ntor_vector):
    return jnp.dot(rmnc, jnp.cos(mn_vector *  ui  - ntor_vector *  vi))
def position_Z(zmns, ui, vi, mn_vector, ntor_vector):
    return jnp.dot(zmns, jnp.sin(mn_vector *  ui  -  ntor_vector * vi))

pos_R_vec = jax.vmap(position_R, (None, 0,0, None, None), 0)
pos_Z_vec = jax.vmap(position_Z, (None, 0,0, None, None), 0)

def Point_Error_Unconstrained(rmnc,zmns,ui,Ri, Zi,vi, mn_vector, ntor_vector):
    return jnp.concatenate((pos_R_vec(rmnc, ui, vi, mn_vector, ntor_vector) - Ri, pos_Z_vec( zmns, ui, vi, mn_vector, ntor_vector) - Zi))

class Stellarator_Blanket_Optimizer_Direct:
    def __init__(self,filename_vmec : str):
        self.flux_surfaces = Flux_Surfaces_Normal_Extended_From_HDF5(filename_vmec)
        

        self.fourier_shape = self.flux_surfaces.Rmnc.shape[1]
        self.symm          = self.flux_surfaces.flux_surface_settings.symmetry
        self.m_pol_vec       = self.flux_surfaces.m_pol_vec
        self.n_tor_vec       = self.flux_surfaces.n_tor_vec
    def optimize_d(self,d_func, Nv : int, Nu : int, lambda_k : float = 0.01, nu : float = 1.8, maxiter = 10, optimize_arclength = True):
        ### Three-step process

        u = np.linspace(0, 2 * np.pi, Nu, endpoint=False)
        v = np.linspace(0.0, 2 * np.pi / self.symm / 2.0, Nv)
        uu, vv = np.meshgrid(u,v)
        ui = uu.ravel()
        vi = vv.ravel()

        xyz = self.flux_surfaces.Return_Position(np.ones(ui.shape),d_func(ui,vi, self.flux_surfaces), ui, vi)
        
        Ri = np.sqrt(xyz[:,0]**2 + xyz[:, 1]**2)
        Zi = xyz[:,2]
        vi = np.arctan2(xyz[:,1], xyz[:,0]) # because normal vector is not exactly in orthogonal to phi, we should just take the new phi 

        # 1:
        # First we optimise naively the Rmnc & Zmns coefficients under variable ui
        # Very important: start with Rmnc & Zmns zero. This ensures the ui coefficients do NOT update
        # the first iteration and you basically have a first step where Rmnc & Zmns are linearly least squares 
        # fitted on the curve. This provides a good starting point for ui optimisation (if Rmnc, Zmns != 0, this 
        # would update the ui to an undesirable state...)
        args = (jnp.zeros(self.fourier_shape), jnp.zeros(self.fourier_shape), ui, Ri, Zi, vi, self.m_pol_vec, self.n_tor_vec)
        optimizer_nums = 3

        args_new = Levenberg_Marquardt_Total(Point_Error_Unconstrained, optimizer_nums, *args, lambda_k = lambda_k, nu = nu, maxiter = maxiter, output = True)

        Rmnc_ex_naive = args_new[0]
        Zmns_ex_naive = args_new[1]
        if not optimize_arclength:
            return  Rmnc_ex_naive, Zmns_ex_naive
        # 2: 
        # We now have a well-fitted curve but due to the freedom in u, it can be parametrized very unfavourably (and it is most often)
        # So, now we need to find equi-distant sampling points on the surface.
        # This means we need to find points that are equally spaced on the surface, and then give them equidistant u coordinates
        #
        # To do this, note that the v slices are already equi-distant by design (the v coordinate isn't modified)
        # Therefore, for each considered v slice, we look at the arclength(u). Then, we construct new u coordinates
        # that have approximatley equal arclength.
        # This is done by considering a point and the arc length it would have if it was equally spaced u.
        # Then, the delta-u is scaled linearly such that it is approximately an equal arc length delta-u.
        # This gives a function that takes a u value and finds an equal-arc-length corresponding u.
        # We create a new meshgrid of u & v equidistant. Then, we transform these u to equal-arc-length u 
        # and sample Ri, Zi. We now identify these points with the equidistant u & v (i.e. give them new u coordinates.)
        def get_transformation_function(v,ns, Rmnc_ex, Zmns_ex):
            v_v = np.linspace(v, v, ns)
            u_v = np.linspace(0, 2*np.pi , ns , endpoint=False)
            du  = u_v[1] - u_v[0]

            R     = pos_R_vec(Rmnc_ex, u_v, v_v, self.m_pol_vec, self.n_tor_vec)
            Z     = pos_Z_vec(Zmns_ex, u_v, v_v, self.m_pol_vec, self.n_tor_vec) 
            arc   = np.sqrt( (R - np.roll(R,1))**2 + (Z - np.roll(Z,1))**2 )
            marc  = np.mean(arc) 
            arc_f = interp1d(u_v, arc, kind='cubic', fill_value='extrapolate')

            u_n   = np.zeros(u_v.shape)
            
            for j in range(1, ns):
                u_n[j] = u_n[j - 1] +  du * marc / arc_f(u_n[j-1] + du)
            return interp1d(u_v, u_n, kind='cubic', fill_value='extrapolate')
        
        nv = np.linspace(0, 2 * np.pi /( 2 * self.symm), Nv)
        uv = np.linspace(0, 2 * np.pi, Nu, endpoint = False)

        vv_ed, uu_ed = np.meshgrid(nv, uv)
        vv,    uu    = np.meshgrid(nv, uv)

        ns = 300

        for i in range(Nv):
            uf       = get_transformation_function(nv[i], ns, Rmnc_ex_naive, Zmns_ex_naive)
            uu[:, i] = uf(uv)

        Ri_u_resampled = pos_R_vec(Rmnc_ex_naive, uu.ravel(), vv.ravel(), self.m_pol_vec, self.n_tor_vec)
        Zi_u_resampled = pos_Z_vec(Zmns_ex_naive, uu.ravel(), vv.ravel(), self.m_pol_vec, self.n_tor_vec)

        # 3.
        # 
        # Finally, we fix the equi-distant u & v coordinates and just optimise the Rmnc & Zmns coefficients given these equi-distant coordinates.
        # Note that we cannot do this from the beginning because the normal vectors don't give you a v slice but something different. You could interpolate 2D or something,
        # but this isn't really that accurate.
        args_ea = (jnp.zeros(self.fourier_shape), jnp.zeros(self.fourier_shape), uu_ed.ravel(), Ri_u_resampled.ravel(), Zi_u_resampled.ravel(), vv_ed.ravel(),self.m_pol_vec, self.n_tor_vec)

        optimizer_nums_ea = 2

        args_ea_new = Levenberg_Marquardt_Total(Point_Error_Unconstrained,optimizer_nums_ea, *args_ea, lambda_k = 0.01, nu = 1.8, maxiter= 5,output=True)

        return args_ea_new[0], args_ea_new[1]
    
    def Optimize_d_list(self, d_func_list, Nv : int, Nu : int, lambda_k : float = 0.01, nu : float = 1.8, maxiter = 5, optimize_arclength = True):
        Rmnc_list = []
        Zmns_list = []
        for i,d in enumerate(d_func_list):
            print("Optimising distance " + str(i))
            rmnc_opt, zmns_opt = self.optimize_d(d, Nv, Nu, lambda_k, nu, maxiter, optimize_arclength=optimize_arclength)

            Rmnc_list.append(rmnc_opt)
            Zmns_list.append(zmns_opt)
        return jnp.array(Rmnc_list), jnp.array(Zmns_list)
