import numpy as np
import jax.numpy as jnp
import jax
import meshio
import h5py
from typing import List
from .Optimisers import Levenberg_Marquardt_Total
from .SBGeom_cpp import Flux_Surfaces, Flux_Surfaces_Fourier_Extended, Flux_Surfaces_Normal_Extended, Flux_Surface_Settings

def read_vmec(filename : str):
    with h5py.File(filename) as f:
        Rmnc     = np.array(f['rmnc'])
        Zmns     = np.array(f['zmns'])
        ntor_vec = np.array(f['xn'])
        
        
        m_pol    = int(np.array(f['mpol']))
        n_tor    = int(np.array(f['ntor']))
        no_surf  = int(np.array(f['ns']))
        symm     = int(ntor_vec[1])
    return Rmnc, Zmns, Flux_Surface_Settings(no_surf, n_tor, m_pol, symm)

def Flux_Surfaces_From_HDF5(filename : str):    
    return Flux_Surfaces(*read_vmec(filename))

def Flux_Surfaces_Normal_Extended_From_HDF5(filename : str):
    return Flux_Surfaces_Normal_Extended(*read_vmec(filename))



