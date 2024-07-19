print ("Welcome to the Virtual Pet Game!") # The welcome massage
check = True # a bool to check if the hunger of the pet is equal to 0

# create a class named Pet
class Pet:
    # initialize the pet's attributes
    def __init__(self,name,hunger,happiness):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness

    def feed(self):
        '''
            A function to Feed the pet and check if the pet's hunger is equal to 0
        '''

        global check

        # check the hunger, and decrease it if it's greater than 0
        if self.hunger == 0:
            print (f"You can't feed {self.name} because the hunger is {self.hunger}\n")
            check = False
            return

        else:
            self.hunger -= 1
            print (f"You fed {self.name}! {self.name}'s hunger is now {self.hunger}\n")

    def play(self):
        '''
            A function to Play with the pet
        '''
        self.happiness += 2
        print (f"You played with {self.name}! {self.name}'s happiness is now {self.happiness}\n")

    def check_status(self):
        '''
            A function to display the pet's status for the user
        '''
        print (f"{self.name}'s hunger is : {self.hunger}, happiness : {self.happiness}\n")


# Take the name of the pet from the user
pet_name = input("What is your pet's name? ")

# Make an object from the Pet class
pet = Pet(pet_name,5,10)

# Take the input of options from the user
choice = 0
while choice != 4:

    # Display the choices list for the user
    print ("Choose an action:")
    print (f"1. Feed {pet_name}")
    print (f"2. Play with {pet_name}")
    print (f"3. Check {pet_name}'s status")
    print ("4. Exit")

    choice = input("Enter your choice: ") # the entered option

    # Handle if the chosen option is wrong
    try:
        choice = int(choice)
        if choice > 4 or choice < 1:
            print ("Invalid choice. Please enter a valid option.\n")
            continue 

    except ValueError:
        print ("Invalid choice. Please enter a valid option.\n")
        continue
    
    # Handle the options
    if choice == 1:
        pet.feed()
        if check == False:
            continue

    elif choice == 2:
        pet.play()

    elif choice == 3:
        pet.check_status()

print ("Thank you for playing the Virtual Pet Game!")