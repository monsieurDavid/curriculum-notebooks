import sympy as sym
from sympy.utilities.lambdify import lambdify, implemented_function
from sympy import Function
from plotting_routines import *
from IPython.display import clear_output
import ipywidgets
from ipywidgets import interact, interactive, fixed, interact_manual
import numpy as np
from collections import OrderedDict
   
def variables_setup():
    x = sym.symbols('x')
    a = sym.symbols('a',real=True,nonpositive = True)
    return x,a

def sign(function_setup,x_value,a_value):

    if function_setup(x_value,a_value)[0] > 0:
        return 1
    elif function_setup(x_value,a_value)[0] < 0:
        return -1
    

def simplified_function(function_setup,a_value):
    x,a = variables_setup()
    num = function_setup(x,a_value)[1]
    denom = function_setup(x,a_value)[2]
    
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
        f = implemented_function(Function('f'), lambda a: function_setup(x,a)[1])
    elif poly == 'denom':
        f = implemented_function(Function('f'), lambda a: function_setup(x,a)[2])
        
    lam_f = lambdify(a, f(a))
    
    
    poly_at_a = lam_f(a_value)
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
        if every_root in denominator_roots:
            func_remov_disc = np.append(func_remov_disc, every_root)
        else:
            func_zeros = np.append(func_zeros, every_root)
    
    for every_root in denominator_roots:
        if every_root not in numerator_roots:
            func_inf_disc = np.append(func_inf_disc, every_root)
        else:
            
            func_limits_remov = np.append(func_limits_remov,limits_at_a(a,every_root,function_setup))
            
    
    return (func_zeros, func_remov_disc, func_inf_disc)

    

                
         
  

