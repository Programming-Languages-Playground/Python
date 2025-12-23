## Types of functions
    - pure vs impure
    - recursive
    - lamdas (anonymous function)

## Lambdas
chai_types = ["ginger", "elaichi", "kadak", "irani"]
strong_chai = list(filter(lamda chai: chai == "kadak", chai_types))

print(strong_chai)

## Documentations
def func_name(flavor="masala"):
    """
    Description      # Documentation of a function
    :param chai: .....
    :param samosa: ...
    : return: (thank you message)
    """ 
    return flavor

print(func_name.__doc__) # dundle
print(func_name.__name__)


