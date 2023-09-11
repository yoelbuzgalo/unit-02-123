'''
This is the main function called when the program starts
'''
def main():
    # Prompts and asks the user to enter all of the 10 items for the bad_libs game
    adjective_1 = input("Enter a adjective: ")
    adjective_2 = input("Enter another adjective: ")       
    car_type = input("Enter a type of car: ")  
    country_place = input("Enter a country: ")
    verb_past_tense = input("Enter a past tense verb: ")
    verb = input("Enter a verb: ")
    school_name = input("Enter a school name: ")
    plural_noun = input("Enter a plural noun: ")
    weapon_item = input("Enter a weapon item: ")
    verb_ing_1 = input("Enter a verb that ends with ing: ")
    game_name = input("Enter a game name: ")

    print("A ", adjective_1," ", car_type, " that is so ", adjective_2, " went flying through the highways of ",  country_place, " and you were ", verb_past_tense," over by a cop. So you decided to ", verb," back to him!\n", "Unfortunately, he put you to ", school_name, " to learn about ", plural_noun, " and you got so bored so you decided to play ", game_name, " on which you chose...\n", weapon_item, " to fight off your imaginary cops that you were just caught by!", sep="", end="!") #Prints the desired funny story out to the terminal

main()
