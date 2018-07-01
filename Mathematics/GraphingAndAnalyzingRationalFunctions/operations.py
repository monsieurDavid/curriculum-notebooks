import sympy as sym
from sympy import diff

from sympy.utilities.lambdify import lambdify, implemented_function
from sympy import Function
from plotting_routines import *
from IPython.display import clear_output
import ipywidgets
from ipywidgets import interact, interactive, fixed, interact_manual
import numpy as np
from functools import partial, update_wrapper
from collections import OrderedDict
   
def variables_setup():
    x = sym.symbols('x')
    a = sym.symbols('a',real=True,positive = True)
    return x,a

def derivative_setup(x_value,a_value,function_setup):
    x,a = variables_setup()
    num, denom = function_setup(x_value,a_value)[1], function_setup(x_value,a_value)[2]
    func = sym.simplify(diff(num/denom,x))
    return (func, sym.fraction(func)[0], sym.fraction(func)[1])

def sign(function_setup,x_value,a_value):
    
    x,a = variables_setup()
    
    lam_f = lambdify((x,a), function_setup(x,a)[0])

    if lam_f(x,a_value).evalf(subs={x: x_value}).is_positive:
        return 1
    elif lam_f(x,a_value).evalf(subs={x: x_value}).is_negative:
        return -1
    else:
        return 0
    

def simplified_function(function_setup,a_value):
    
    x,a = variables_setup()
  
    lam_f_num = lambdify((x,a), function_setup(x,a)[1])
    lam_f_denom = lambdify((x,a), function_setup(x,a)[2])
    
    num = lam_f_num(x,a_value)
    denom = lam_f_denom(x,a_value)
    
    return sym.simplify(factorize(num,x)/factorize(denom,x))

def factorize(poly,x):
    roots = sym.solve(poly,x)
    final_product = 1
    for root in roots:
        if sym.im(root) == 0:
            final_product = final_product*(x-root)
            
    unfactorized_part = sym.polys.polytools.div(poly,final_product)[0]
    final_product = final_product*unfactorized_part
    
    return final_product

def limits_at_a(a_value,x_value,function_setup):
    x,a = variables_setup()
    return sym.limit(function_setup(x,a_value)[0], x, x_value)


def find_real_roots(poly,a_value,function_setup):
    x,a = variables_setup()

    if poly == 'num':
        
        lam_f = lambdify((x,a), function_setup(x,a)[1])
        
    elif poly == 'denom':
        lam_f = lambdify((x,a), function_setup(x,a)[2])
        
        
    poly_at_a = lam_f(x,a_value)
    all_local_roots = sym.solve(poly_at_a,x)
    real_roots = []
    for every_root in all_local_roots:
        if sym.im(every_root) == 0:
            real_roots = np.append(real_roots,every_root)
    return real_roots

def find_multiplicities(poly,a_value,function_setup):
    x = variables_setup()[0]
    
    if poly == 'num':
        
        multiplicity_full_dict = sym.roots(sym.fraction(simplified_function(function_setup,a_value))[0],x)
        
    elif poly == 'denom':
        multiplicity_full_dict = sym.roots(sym.fraction(simplified_function(function_setup, a_value))[1],x)
        
    multiplicity_real_dict = {}
        
    for each_root in multiplicity_full_dict.keys():
        if sym.im(each_root) == 0:
            multiplicity_real_dict[each_root] = multiplicity_full_dict[each_root]
    
    return multiplicity_real_dict
        
      

def true_answers(P,Q,function_setup,a_value):
    x,a = variables_setup()
	
    true_answers = {}
    if factorize(Q,x) == Q:
        true_answers['factorization'] = 'No'
    else:
        true_answers['factorization'] = 'Yes'

    disc_option_a = 'No cancellation occurs; therefore, there is an infinite discontinuity at the root(s) of the denominator.'
    disc_option_b = 'Some factors got cancelled, and the discontinuity is removable!'
    
    list_num_roots = []
    list_denom_roots = []
    
    for each_num_root in sym.solve(P,x):
        list_num_roots = np.append(list_num_roots, each_num_root.evalf(subs={a: a_value}))
    
    for each_denom_root in sym.solve(Q,x):
        list_denom_roots = np.append(list_denom_roots, each_denom_root.evalf(subs = {a: a_value}))
    

    if bool(set(list_num_roots) & set(list_denom_roots)) == False:
        true_answers['discontinuity_type'] = disc_option_a
    else:
        true_answers['discontinuity_type'] = disc_option_b
        
    num_root_multiplicities = find_multiplicities('num',a_value,function_setup)
    denom_root_multiplicities = find_multiplicities('denom',a_value,function_setup)
    
    root_multiplicities = {**num_root_multiplicities, **denom_root_multiplicities}
    
    true_answers['multiplicity'] = {}
    
    for each_root in root_multiplicities.keys():
        true_answers['multiplicity'][each_root] = root_multiplicities[each_root]
        
    true_answers['extrema'] = {}
        
    derivative = partial(derivative_setup, function_setup = function_setup)
    der_zeros = list(find_multiplicities('num',a,derivative).keys())
    
    f = implemented_function(Function('f'), lambda x,a: diff(derivative(x,a)[0],x))
        
    lam_f = lambdify((x,a), f(x,a))
    
    
    for each_extremum in der_zeros:
        second_derivative_value = lam_f(x, a_value).evalf(subs = {x: each_extremum})
        if second_derivative_value.is_positive:
            true_answers['extrema'][each_extremum] = 1
        elif second_derivative_value.is_negative:
            true_answers['extrema'][each_extremum] = -1
        else:
            true_answers['extrema'][each_extremum] = 0
 

    return true_answers


def on_value_change(change, problem_type, widget, function_setup, a_value):
    
    clear_output()
    display(widget)
    
    x,a = variables_setup()
        
    P,Q = function_setup(x,a)[1], function_setup(x,a)[2]
    if change['new'] == true_answers(P,Q,function_setup,a_value)[problem_type]:
        print('Correct!')

    else:
        print('Please try again!')

def return_zeros(a,function_setup):
    
    x = variables_setup()[0]

    num,denom = function_setup(x,a)[1], function_setup(x,a)[2]

    
    func_zeros = []
    func_remov_disc = []
    func_inf_disc = []
    func_limits_remov = []
    
    numerator_roots = find_real_roots('num',a,function_setup)
    denominator_roots = find_real_roots('denom',a,function_setup)
    
    for every_root in numerator_roots:
        if (every_root in list(find_multiplicities('num',a,function_setup).keys())) & \
            (every_root in denominator_roots):
            func_remov_disc = np.append(func_remov_disc, every_root)
        elif (every_root not in list(find_multiplicities('num',a,function_setup).keys())) & \
        (every_root not in list(find_multiplicities('denom',a,function_setup).keys())):
            func_remov_disc = np.append(func_remov_disc, every_root)
        elif every_root in list(find_multiplicities('denom',a,function_setup).keys()):
            continue
        else:
            func_zeros = np.append(func_zeros, every_root)
    
    for every_root in denominator_roots:
        if every_root in list(find_multiplicities('denom',a,function_setup).keys()):
            func_inf_disc = np.append(func_inf_disc,every_root)
    
    return (func_zeros, func_remov_disc, func_inf_disc)

    

                
         
  

