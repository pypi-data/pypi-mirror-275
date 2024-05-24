import jax
import jax.numpy as jnp
import numpy as np

def position_R(rmnc, ui,vi,mn_vector,ntor_vector):
    return jnp.dot(rmnc, jnp.cos(jnp.outer(mn_vector, ui ) - jnp.outer(ntor_vector, vi)))
def position_Z(zmns, ui, vi, mn_vector, ntor_vector):
    return jnp.dot(zmns, jnp.sin(jnp.outer(mn_vector, ui ) -  jnp.outer(ntor_vector, vi)))

def Point_Error_Unconstrained(rmnc,zmns,ui,Ri, Zi,vi, mn_vector, ntor_vector):
    return jnp.concatenate((position_R(rmnc, ui, vi, mn_vector, ntor_vector) - Ri, position_Z( zmns, ui, vi, mn_vector, ntor_vector) - Zi))

## See https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/representing-the-boundary-of-stellarator-plasmas/095F0ECEBBA368D9FE5AA5233F792DA2
def Position_R_HB(Rn, rho_mn, bn, theta, phi, alpha, rmn_m_pol_vector, rmn_n_tor_vector, n_m0_vector ):
    R0_phi        = jnp.dot(Rn, jnp.cos( -  n_m0_vector * phi))
    rho_theta_phi = jnp.dot(rho_mn, jnp.cos(rmn_m_pol_vector * theta + rmn_n_tor_vector * phi- alpha * phi))
    zeta_theta_phi= jnp.dot(bn, jnp.cos( n_m0_vector * phi) * jnp.sin(theta - alpha * phi))
    Rtheta_phi    = R0_phi + rho_theta_phi * jnp.cos(alpha * phi) - zeta_theta_phi * jnp.sin(alpha * phi)
    return Rtheta_phi

def Position_Z_HB(Zn, rho_mn, bn, theta, phi, alpha, rmn_m_pol_vector, rmn_n_tor_vector, n_m0_vector):
    Z0_phi        = jnp.dot(Zn, jnp.sin(  - n_m0_vector * phi))
    rho_theta_phi = jnp.dot(rho_mn, jnp.cos(rmn_m_pol_vector * theta + rmn_n_tor_vector * phi- alpha * phi))
    zeta_theta_phi= jnp.dot(bn, jnp.cos( n_m0_vector * phi) * jnp.sin(theta - alpha * phi))
    Rtheta_phi    = Z0_phi + rho_theta_phi * jnp.sin(alpha * phi) + zeta_theta_phi * jnp.cos(alpha * phi)
    return Rtheta_phi

Pos_R_HB_vec = jax.vmap(Position_R_HB,(None,None,None,0,0,None,None,None,None),0)
Pos_Z_HB_vec = jax.vmap(Position_Z_HB,(None,None,None,0,0,None,None,None,None),0)

def Point_Error_Unconstrained_HB(Rn, Zn, rho_mn, bn, ui, vi, Ri, Zi, rmn_m_pol_vector, rmn_n_tor_vector, n_m0_vector, alpha):
    return jnp.concatenate((Pos_R_HB_vec(Rn, rho_mn, bn, ui, vi, alpha, rmn_m_pol_vector, rmn_n_tor_vector, n_m0_vector) - Ri, Pos_Z_HB_vec(Zn, rho_mn, bn, ui, vi, alpha,rmn_m_pol_vector,rmn_n_tor_vector, n_m0_vector) - Zi))


def n_to_bn(n,bn, ntor):
    if n >=0 and n <= ntor:
        return bn[int(n)]
    else:
        return 0


def mn_to_rmn_index(m,n, rho_mn, ntor):
    if n >= -ntor and n <= ntor :
        return rho_mn[ int((2 * ntor + 1) * (m-1) + n  + ntor)]
    else:
        return 0.0

def To_Rmnc_Zmns(Rn, Zn, rho_mn, bn, m_pol_vector, n_tor_vector, ntor, ui_sign):

    Rmnc = np.zeros(m_pol_vector.shape[0])
    Zmns = np.zeros(m_pol_vector.shape[0])
    alpha =   n_tor_vector[-1] / ntor
    
    rmn_mpol = m_pol_vector[ntor+1:]
    rmn_ntor = n_tor_vector[ntor+1:]
    for i in range(Rmnc.shape[0]):
        m = m_pol_vector[i]
        n = n_tor_vector[i] / alpha
        if ui_sign > 0:
            if m == 0:
                Rmnc[i] = Rn[i]
                Zmns[i] = Zn[i]
            else:

                Rmnc[i] = 0.5 * ( mn_to_rmn_index(m, -n, rho_mn, ntor) + mn_to_rmn_index(m, -n + 1, rho_mn, ntor) ) 
                Zmns[i] = 0.5 * (mn_to_rmn_index(m, - n, rho_mn, ntor ) - mn_to_rmn_index(m, -n + 1, rho_mn, ntor))
            if m== 1:
                Rmnc[i] += 0.25 * ( n_to_bn(n, bn, ntor) + n_to_bn(-n, bn, ntor) - n_to_bn(n - 1, bn, ntor) - n_to_bn(-n + 1, bn, ntor))
                Zmns[i] += 0.25 * ( n_to_bn(n, bn, ntor) + n_to_bn(-n, bn, ntor) + n_to_bn(n - 1, bn, ntor) + n_to_bn(-n + 1, bn, ntor))
        else:
            if m == 0:
                Rmnc[i] = Rn[i]
                Zmns[i] = Zn[i]
            else:

                Rmnc[i] = 0.5 * ( mn_to_rmn_index(m, n, rho_mn, ntor) + mn_to_rmn_index(m, n + 1, rho_mn, ntor) ) 
                Zmns[i] = - 0.5 * (mn_to_rmn_index(m, n, rho_mn, ntor ) - mn_to_rmn_index(m, n + 1, rho_mn, ntor))
            if m== 1:
                Rmnc[i] += 0.25 * ( n_to_bn(n, bn, ntor) + n_to_bn(-n, bn, ntor) - n_to_bn( - n - 1, bn, ntor) - n_to_bn(n + 1, bn, ntor))
                Zmns[i] += -0.25 * ( n_to_bn(n, bn, ntor) + n_to_bn(-n, bn, ntor) + n_to_bn(-n - 1, bn, ntor) + n_to_bn(n + 1, bn, ntor))
    
    return Rmnc, Zmns

def To_Rmnc_Zmns_trunc(Rn, Zn, rho_mn, bn, m_pol_vector_orig, n_tor_vector_orig, ui_sign, ntor_trunc, mpol_trunc):

    Rmnc = np.zeros(m_pol_vector_orig.shape[0])
    Zmns = np.zeros(m_pol_vector_orig.shape[0])
    alpha =   n_tor_vector_orig[1]
    
    for i in range(Rmnc.shape[0]):
        m = m_pol_vector_orig[i]
        n = n_tor_vector_orig[i] / alpha
        if ui_sign > 0:
            if m < mpol_trunc and abs(n)  < ntor_trunc:
                if m == 0:
                    Rmnc[i] = Rn[i]
                    Zmns[i] = Zn[i]
                else:

                    Rmnc[i] = 0.5 * ( mn_to_rmn_index(m, -n, rho_mn, ntor_trunc) + mn_to_rmn_index(m, -n + 1, rho_mn, ntor_trunc) ) 
                    Zmns[i] = 0.5 * (mn_to_rmn_index(m, - n, rho_mn, ntor_trunc) - mn_to_rmn_index(m, -n + 1, rho_mn, ntor_trunc))
                if m== 1:
                    Rmnc[i] += 0.25 * ( n_to_bn(n, bn, ntor_trunc) + n_to_bn(-n, bn, ntor_trunc) - n_to_bn(n - 1, bn, ntor_trunc) - n_to_bn(-n + 1, bn, ntor_trunc))
                    Zmns[i] += 0.25 * ( n_to_bn(n, bn, ntor_trunc) + n_to_bn(-n, bn, ntor_trunc) + n_to_bn(n - 1, bn, ntor_trunc) + n_to_bn(-n + 1, bn, ntor_trunc))
        else:
            if m < mpol_trunc and abs(n)  < ntor_trunc:
                if m == 0:
                    Rmnc[i] = Rn[i]
                    Zmns[i] = Zn[i]
                else:

                    Rmnc[i] = 0.5 * ( mn_to_rmn_index(m, n, rho_mn, ntor_trunc) + mn_to_rmn_index(m, n + 1, rho_mn, ntor_trunc) ) 
                    Zmns[i] = - 0.5 * (mn_to_rmn_index(m, n, rho_mn, ntor_trunc ) - mn_to_rmn_index(m, n + 1, rho_mn, ntor_trunc))
                if m== 1:
                    Rmnc[i] += 0.25 * ( n_to_bn(n, bn, ntor_trunc) + n_to_bn(-n, bn, ntor_trunc) - n_to_bn( - n - 1, bn, ntor_trunc) - n_to_bn(n + 1, bn, ntor_trunc))
                    Zmns[i] += -0.25 * ( n_to_bn(n, bn, ntor_trunc) + n_to_bn(-n, bn, ntor_trunc) + n_to_bn(-n - 1, bn, ntor_trunc) + n_to_bn(n + 1, bn, ntor_trunc))
    
    return Rmnc, Zmns