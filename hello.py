'''
This program prints out hello world and prompts you to enter your name,
written by Yoel
'''

def hello_world():
    """
    This function prints out "Hello world!" to the output
    """
    print("Hello, world!")# this prints "Hello world! to terminal"

def hello_you():
    """
    This function prompts you to enter your name and will print"Hello,  yourname"
    """
    your_name = input("Enter your name: ") # Ask the user its name
    print("Hello,", your_name) # Prints hello, name

hello_world()
hello_you()