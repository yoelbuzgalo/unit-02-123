def convert_to_ascii():
    my_char = input("Enter a char: ")
    my_ord = ord(my_char)
    print(my_ord)

def convert_from_ascii():
    my_int = int(input("Enter an integer: "))
    my_char = chr(my_int)
    print("Ascii Code of your char is: ", my_char)


def main():
    convert_to_ascii()
    convert_from_ascii()
    convert_from_ascii()
    convert_from_ascii()

main()