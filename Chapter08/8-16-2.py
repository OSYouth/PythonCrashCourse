# from module_name import function_name an fn
from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs[:], completed_models)
pm(unprinted_designs, completed_models)
scm(completed_models)



# import module_name as mn

# from module_name import *
