import agency as ag

def main():
    # create object of agency
    agency = ag.Agency()


    # add 5 animals
    agency.add_pet("Henry", 4, "Male", "Labrador_Dog", "Playful", "Brown")
    agency.add_pet("Chikku", 0, "Male", "Cockatiel_Bird", "Happy", "Cinnamon")
    agency.add_pet("Mittens", 1, "Female", "California_Spangled_Cat", "Grumpy", "Gray")
    agency.add_pet("Hammy", 0, "Female", "Hamster", "Confused", "Orange/White")
    agency.add_pet("Nemo", 0, "Male", "Clownfish_Fish", "Curious", "Orange/White/Black")


    # start loop for user to adopt an animal
    while True:
        agency.display_pets()

        ask_name = input("What is the name of the new friend you want to adopt: ")
        ask_owner_name = input("What is your name: ")

        agency.adopt_pet(ask_name, ask_owner_name)

main()