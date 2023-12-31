'''
This function prints out variable practices, different kinds of variables part of Activity 2.17
'''

def variable_practice():
    my_age = 23*12 # my age variable, times with 12 as in months per year
    number_of_days_in_year = 365 # number of days in a year
    pet_name = "Curry" # my pet name
    pi_value = 3.1475 # pi value

    print("Your age is", my_age, "months! The number of days in a year is", number_of_days_in_year, "and your pet name is", pet_name, "and pi is", pi_value) # prints out all of the variables values


'''
This function is part of activity 2.20, testing and practicing different variables with arithmetic operations
'''
def expressions_practice():
    literal_exp = 5
    addition_exp = 1+1
    exponent_exp = 2**2
    floor_exp = 4//2
    mod_exp = 2%5
    math_exp = (2+2)*(5-3)
    mix_exp = 2*(4/2)+5%10-20

    # Prints out results of each variables
    print("Literal expression:", literal_exp)
    print("Additional expression:",addition_exp)
    print("Exponent expression:",exponent_exp)
    print("Floor division expression:",floor_exp)
    print("Mod expression:",mod_exp)
    print("Math operation expression:",math_exp)
    print("Mix of everything expression:",mix_exp)

# This function takes in two numbers and supposedly prints added numbers of these two input numbers. However it prints out concentated string literals ("1"+"2" = "12") which is not correct.
def prompt_and_print():
    number_1 = input("Enter first number: ")
    number_2 = input("Enter second number: ")
    result = int(number_1) + int(number_2)
    print("Result is:", result)


'''
Part of Activity 2.22, adding a main function
'''
def main():
    variable_practice()
    expressions_practice()
    prompt_and_print()

main()