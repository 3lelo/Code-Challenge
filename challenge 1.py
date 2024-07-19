# The welcome massage
print ("Welcome to the simple ATM!")

amount = 1000.0 # the starting amount in the acount
bonus = 0 # the bonus part
check = True # check if the entered money to withdraw is grater or less than the amount in the acount

def check_balance():
    '''
        function to display the amount in the acount
    '''
    print (f"Your current balance is: ${amount}\n")

def deposit_money(money):
    '''
        function to deposit money to the acount
    '''
    global amount
    global bonus

    amount += money
    print (f"Deposit successful! Your new balance is : ${amount}\n")
    bonus += 1

def withdraw_money(money):
    '''
        function to withdraw money from the acount
    '''
    global amount
    global check

    if money > amount:
        print ("You put a number greater than your amount!\n")
        check = False
        return

    else:
        amount -= money
        print (f"Withdraw successful! Your new balance is : ${amount}\n")
    

# Take the input of options from the user
while True:

    # Display the choices list for the user
    print ("Please chose an operation:")
    print ("1. Check Balance")
    print ("2. Deposit Money")
    print ("3. Withdraw Money")
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
    if choice == 4:
        break

    if choice == 1:
        check_balance()

    else:
        if choice == 2:
            money = input("Enter the amount to deposit: ")
        else:
            money = input("Enter the amount to withdraw: ")
        try:
            money = float(money)
            if money <= 0:
                print ("Enter a positive number please!\n")
                continue
            if choice == 2:
                deposit_money(money)
            else:
                withdraw_money(money)
                if check == False:
                    continue     

        except ValueError:
            print ("Please enter a number\n")
            continue

# The end massage
print ("Thank you to use the simple ATM. Goodbye!")

# The bonus part
print (f"The number of Deposits is : {bonus}")