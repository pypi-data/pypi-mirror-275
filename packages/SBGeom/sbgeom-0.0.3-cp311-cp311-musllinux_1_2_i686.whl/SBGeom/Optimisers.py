import jax 
import jax.numpy as jnp 

def Levenberg_Marquardt_Total(residual_function, optimizer_nums : int, *args, lambda_k, nu, maxiter, output = False):
    
    residual_function_jit = jax.jit(residual_function)
    argnums   = tuple(i for i in range(optimizer_nums))
    residual_function_jac_jit = jax.jit(jax.jacfwd(residual_function, argnums = argnums))
    
    for i in range(maxiter):
        args, lambda_k, success = Levenberg_Marquardt_iteration(residual_function_jit, optimizer_nums, *args,lambda_k = lambda_k, nu = nu, jacobian = residual_function_jac_jit, output = output)
        if not success: break
    print("Total final cost: ",jnp.sum(residual_function_jit(*args)**2))
    return args


# If you see weird errors relating to dimensions: keep in mind that hstack doesn't work if the dimensions of the Jacobians are different.
# This might be because your parameters are not 1D arrays (but e.g. 0D scalars). Flatten and create 1D arrays instead.
def Levenberg_Marquardt_iteration(residual_function , optimizer_nums : int , *args, lambda_k, nu, jacobian, output= False):
    not_better = True
    argnums   = tuple(i for i in range(optimizer_nums))
    jax_jac   = jacobian(*args)
    jacobian  = jnp.hstack((jax_jac))
    JTJ       = jacobian.T @ jacobian 
    cost_prev = jnp.sum(residual_function(*args)**2)
    if output:
        print(" lambda_k = " + str(lambda_k)+ " costs: " + str(cost_prev))
    iter      = 0
    while not_better:
        
        iter += 1

        lambda_d_nu = lambda_k / nu

        JTJ_lambda    =  JTJ + jnp.eye(JTJ.shape[0]) * lambda_k
        JTJ_lambda_nu =  JTJ + jnp.eye(JTJ.shape[0]) * lambda_d_nu

        JTf_x_lambda    = jacobian.T @ residual_function(*args)

        update_vec    = jnp.linalg.solve(JTJ_lambda, JTf_x_lambda)
        update_vec_nu = jnp.linalg.solve(JTJ_lambda_nu, JTf_x_lambda)
          
        start_i = 0
        
        args_u  =  []
        args_nu =  []
        for i in range(optimizer_nums):
            i_u  = args[i] - update_vec[start_i:start_i + args[i].shape[0]]
            i_nu = args[i] - update_vec_nu[start_i:start_i + args[i].shape[0]]
            start_i += args[i].shape[0]
            args_u.append(i_u)
            args_nu.append(i_nu)
        for j in range(optimizer_nums, len(args)):
            args_u.append(args[j])
            args_nu.append(args[j])
        
        cost    = jnp.sum(residual_function(*args_u)**2)
        cost_nu = jnp.sum(residual_function(*args_nu)**2)

        
        
        if cost >= cost_prev and cost_nu >= cost_prev:
            lambda_k = nu  * lambda_k
        elif cost_nu < cost:
            not_better = False
            lambda_k = lambda_d_nu
            return args_nu, lambda_k, True

        elif cost < cost_prev:
            return args_u, lambda_k, True

        if ( iter > 20):
            print(" Can no longer decrase in value. LM terminates")
            return args, lambda_k, False
