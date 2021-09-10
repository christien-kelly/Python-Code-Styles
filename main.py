
def explict_function(*args):
    """
    You cannot explicitly see what is being passed to the functions.

    Args:
        *args - a detructured list of arguments
    
    returns a dict of x and y
    """
    x, y = args
    # The locals() method updates and returns a dictionary of the 
    # current local symbol table.
    return dict(**locals())

def positional_arguments(string: str, integer: int) -> bool:
    """
    You can declare declare arguments in functions in whatever order,
    if you assign them to variable names.
    
    Args: 
        string - string object
        integer - integer object
    
    return boolean
    """
    assert isinstance(string, str), "expecting string"
    assert isinstance(integer, int), "expecting int"

    return True

def using_kwargs(**kwargs):
    """
    This function utilizes the kwargs dictionary.

    Args:
        kwargs - a key value pair passed to the function
    
    void function
    """
    print(kwargs)
    return


def main():
    
    # explicit function
    temporary_list = [1,2]
    dictionary = explict_function(*temporary_list)
    print(f"This is the response of the explicit function: \n {dictionary} \n\n")

    # positional arguments
    value = positional_arguments(integer=13, string="13")
    print(f"This is the response of the positional argument function: \n {value} \n\n")
    
    # kwargs let's do it !
    dict1 = {
        "name": "christien",
        "age": 7
    }

    dict2 = {
        "name": "john",
        "NAME": "JOE"
    }
    using_kwargs(key = 1, dictionary = dict1)
    using_kwargs(obj1 = 1, obj2 = 2, obj3 = dict2)

    # unpacking



    


if __name__ == '__main__':
    main()
