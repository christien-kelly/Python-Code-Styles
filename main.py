
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

def main():
    
    # explicit function
    temporary_list = [1,2]
    dictionary = explict_function(*temporary_list)
    print(dictionary)

    




if __name__ == '__main__':
    main()
