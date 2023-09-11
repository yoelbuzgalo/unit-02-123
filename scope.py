GLOBAL_VAR_1 = 10 # Stores an integer value of 10
GLOBAL_VAR_2 = "Some string" # Stores a string value of "Some string"
GLOBAL_VAR_3 = 20.0 # Stores a float value of "20.0"

def print_param(param_1, param_2, param_3):
    '''
    This function takes in three parameters and prints each values of the parameters respectively
    '''
    print("The values of the parameters are:", param_1, param_2, param_3, sep="\n") # Prints out to the console the three parameters' values

def print_local():
    '''
    This function prints a value of a local variable within this scope
    '''
    local_var_1 = "I am local!" # Stores a literal string value to local_var_1 that is accessible by this function only
    print("The local variable's string of this function is: ", local_var_1) # Prints out to the console the local_var_1's value

def print_which():
    '''
    This function prints a value of the local variable within this scope (a test variable against global variable)
    '''
    GLOBAL_VAR_3 = "I am superior to global variables!" # Stores a string value to local variable
    print("The local variable of this function is: ", GLOBAL_VAR_3) # Prints out to the console the local variable GLOBAL_VAR_3

def main():
    '''
    The main entry of this program, calls all functions
    '''
    local_var_1 = 20
    print_param(GLOBAL_VAR_1, GLOBAL_VAR_2, GLOBAL_VAR_3)
    print_local()
    print_which()

main()