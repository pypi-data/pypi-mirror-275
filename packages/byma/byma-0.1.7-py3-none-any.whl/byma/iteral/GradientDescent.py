import numpy as np
from ..interface.BaseInterface import BaseInterface as bs
from .Iteral import Iteral as Int
from numpy import linalg as npling
from scipy.optimize import line_search
import warnings
import scipy.sparse as sp

_DEFAULT_OPTS = {
    'stop': 'normal', 
    'maxit': 1e4, 
    'tol': 1e-8, 
    'verbose': False,
    'mode': None, 
    'method': 'normal',
    'delta_x': 0.0005,
    "dim": 1,
    "step": 0,
    "beta": 1,
    "domain": None, 
    "l": 1,
    "alpha": 1,
    "sigma": 0.5,
    "gamma": None,
    "c": 1,
    "p": 1
    }


def _returns(x, fnorm, dxnorm, mode, method):
    """
    Helper function to format the return value based on the mode.

    Parameters
    ----------
    x : array_like
        Root obtained after iterations.
    fnorm : float
        Norm of the residuals.
    dxnorm : float
        Norm of the correction.
    mode : str
        Mode of the output ('full', 'partial', None).
    method : str
        Stopping method used.

    Returns
    -------
    tuple
        Tuple containing the formatted output based on the mode.
    """
    
    if mode == 'full':
        return x, dxnorm, fnorm
    elif mode == 'partial':
        if method == 'normal': 
            return x, dxnorm 
        else: 
            return x, fnorm
        
    elif ((mode == None) or (mode == False)):
        return x, dxnorm, fnorm


def calc_numerical_gradient(f, x, delta_x):
    """Function for computing gradient numerically."""
    val_at_x = f(x)
    val_at_next = f(x + delta_x)
    return (val_at_next - val_at_x) / delta_x

## Armijo stepsize
def step_size_armijo(beta, sigma, alpha, x, d, f, df):
    """
    Armijo's Rule
    """
    i = 0
    inequality_satisfied = True
    while inequality_satisfied:
        if df(x + np.power(beta, i)*alpha * d(x)) <= f(x) + alpha * np.power(beta, i) * sigma * df(x).dot(
                d(x)):
            break

        i += 1

    return np.power(beta, i)

def _step(step, f, df, sigma, alpha, gamma, x, c, p, iter):
    """
    Check type of step
    """
    
    if step == 1:
        k = iter
        gamma = c*(k**(-p))
        
    elif step == 2:
        gamma = alpha*step_size_armijo(beta, sigma, alpha=alpha, x=x, d=d, f=f, df=df)
        
    elif step == 3:
        
        if iter != 0:
            g = df(x)
            beta = (npling.norm(g)/npling.norm(dxnorm))**2
            d = -g + beta*dk
                
        # Perform the line search to find the step size
        with warnings.catch_warnings(record=True) as w:
            dk = d(x) if iter == 0 else d
            result = line_search(f=f, myfprime=df, xk=x, pk=dk)

        # Check for LineSearchWarning
        if any(isinstance(warn.message, warnings.WarningMessage) and 'The line search algorithm did not converge' in str(warn.message) for warn in w):
            raise ValueError('Line search did not converge.')      

        # Extract the step size from the result
        gamma = result[0]
        if gamma == None:
            raise ValueError('Gamma is a NoneType => line search did not converge')

        dxnorm = df(x)
        
    return gamma
            
        

@bs.set_defaults(default_cls = Int, default_opts=_DEFAULT_OPTS)
def gradient_descent(x, f, df, **kwargs):
    """
    Perform Gradient Descent iterations to find the minimizer of a given function.

    Parameters
    ----------
    x : array_like
        Initial guess.
    f : callable
        Function to minimize.
    df : callable/Null
        Jacobian matrix.
    **kwargs : dict
        Additional keyword arguments for customization.
        
        domain : collable. 
            Domain. If collable, input x return Boolean. True if inside domain. Default R^n
        dim :   int. 
            Diamension starting space. Default R. 
        tol : float, optional
            Tolerance for convergence. Default is 1e-8.
        maxit : int, optional
            Maximum number of iterations. Default is 10000.
        verbose : bool, optional
            If True, prints iteration information. Default is False.
        mode : str, optional
            Mode of the output ('full', 'partial', None).
        step :  int. Default 1/L
                    0: constant method
                    1: vanishing method
                    2: armijo method
                    3: Fletcher-reeves method 
            
        stop :  int. Default 0. Default optimal 
                    0: ||grad(f)||<tol
        beta : float
            parameter
        L : float
            smooth constant
    
    Returns
    -------
    minimize, correction_norm, residuals_norm : tuple
        If mode is 'full'
    minimize, correction_norm, (residuals_norm) : tuple
        if mode is 'partial'. The residuals_norm are returned if method is not 'normal' 
    
    minimize, iterations, correction_norm, residuals_norm: tuple
        if mode is None

    Raises
    ------
    ValueError
        If the maximum number of iterations or tolerance is not a positive integer.

    Examples
    --------
    Basic usage:
    """   

    # Initialize the known constants
    _opts = bs.opts(**kwargs)
    verbose = _opts['verbose']
    mode = _opts['mode']
    tol = _opts['tol']
    maxit = int(_opts['maxit'])
    stop = _opts['stop']
    step = _opts['step']
    beta = _opts['beta']
    delta_x = _opts['delta_x']
    dim = _opts['dim']
    domain = _opts['domain'] 
    L = _opts['l']
    c = _opts['c']
    p = _opts['p']
    gamma = _opts['gamma'] if _opts['gamma'] != None else 1/L
    sigma = _opts['sigma']
    alpha = _opts['alpha'] 
    alpha = alpha if alpha != 0 else gamma
    
    
    iterative = lambda x, gamma, d: x + gamma * d(x) if callable(d) else x + gamma * d
    d = lambda x: - df(x)

    ##### Checking correctness parameters #####
    
    assert isinstance(dim, int), "dim must be an integer"
    
    if maxit <= 0 or not isinstance(maxit, int):
        raise ValueError("Maximum number of iterations 'maxit' must be a positive integer.")
    if tol <= 0:
        raise ValueError("Tolerance 'tol' must be a positive value.")
    
    if df == None:
        assert delta_x > 0, "Step must be positive."
        df = lambda x: calc_numerical_gradient(f, x, delta_x)
        
    if  step != 1 and step != 2 and step != 3 and step != 0:
        raise ValueError('the type must be either of the following:  0/floar: constant method 1: vanishing method 2: armijo method 3: Fletcher-reeves method')

    if verbose:
        print('------ Gradient Descent Method summary ------')
        print(f'tollerence: {tol}')
        print(f'maximum iter: {maxit}')
        print(f'stopping criteria: {stop}')
        print(f'starting guess: {x}')
        print(f'step size type: {step}')
        print(f'alpha: {alpha}')
        print(f'L: {L}')
        print(f'gamma: {gamma}')
    
        print('------ Start iteration ------')
        
    # initialize solution lists
    f_value = f(x)
    df_value = df(x)
    normdx = []
    normf = []
    
    
    for iter in range(maxit):
        
        # Initialize the prescibe type of method 
        gamma = _step(step, f, df, sigma, alpha, gamma, x, c, p, iter)
        
        # Iteration Step
        x = iterative(x, gamma, d)
        
        if sp.issparse(f_value) and sp.issparse(df_value):
            fnorm = sp.linalg.norm(f(x))
            dxnorm = sp.linalg.norm(df(x))
        else:
            fnorm = np.linalg.norm(f(x))
            dxnorm = np.linalg.norm(df(x))
            
        normdx.append(dxnorm)
        normf.append(fnorm)
        
        if  (verbose != 0 and verbose != False) and (iter % verbose == 0):
            print(f"Gradient Descent  status at iteration {iter + 1}: ||dx|| = {dxnorm} and ||F|| = {fnorm}")
        
        if (fnorm < tol and stop == 'residual-check'):
            if verbose:
                print(f'Gradient Descent converged in {iter + 1} iterations with ||F|| = {fnorm}')
            return _returns(x, fnorm=fnorm, dxnorm=normdx, mode=mode, method=stop)
        
        if (dxnorm < tol and stop == 'normal'):
            if verbose:
                print(f'Gradient Descent  converged in {iter + 1} iterations with ||dx|| = {dxnorm}')
            return _returns(x, fnorm=fnorm, dxnorm=normdx, mode=mode, method=stop)
       
        if domain != None:
            if domain(x) == False:
                print('Guess is out of bounds')
                break
        
    if verbose:
        print(f'Gradient Descent did not converge within {maxit} iterations')

    return _returns(x, fnorm=fnorm, dxnorm=normdx, mode=mode, method=stop)