# The welcome massage
print ("Welcome to the Medical Appointment Booking System")

Appointments = [] # Make an empty list to put the Appointments in it
bonus = {} # the bonus part
def Add_appointment(date,time,name):
    '''
        Add an appointment for the list of the appointments
    '''

    global Appointments
    global bonus

    Appointment = [date,time,name]
    Appointments.append(Appointment)

    # The bonus part
    if name not in bonus:
        bonus[name] = 1

    else:
        bonus[name] += 1

    print ("Appointment added successfully.\n")

def display_appointments():
    '''
        Display the appointments for user
    '''

    print ("List of Appointments:")
    number = 1
    for appointment in Appointments:
        print (f"Appointment {number}:")
        print (f"date : {appointment[0]}")
        print (f"time : {appointment[1]}")
        print (f"Doctor : {appointment[2]}")
        print ("----------------------")
        number += 1

    print ()

# Take the input of options from the user
choice = 0
while choice != 3:

    # Display the choices list for the user
    print ("Please select your option:")
    print ("1. Add a New Appointment")
    print ("2. View Booked Appointments")
    print ("3. Exit")

    choice = input("Enter your choice number : ") # the entered option

    # Handle if the chosen option is wrong
    try:
        choice = int(choice)
        if choice > 3 or choice < 1:
            print ("Invalid choice. Please enter a valid option!\n")
            continue

    except ValueError:
        print ("Invalid choice. Please enter a valid option!\n")
        continue
    
    # Handle the options
    if choice == 1:
        print ("Add a New Appointment:")

        date = input("Enter the Appointment date (e.g., 2024-07-15): ")
        if date == '':
            print ("Invalid date!\n")
            continue

        time = input("Enter the Appointment time (e.g., 10:30 AM or 2:00 PM): ")
        if time == '':
            print ("Invalid time!\n")
            continue

        name = input ("Enter the doctor's name: ")
        if name == '':
            print ("Invalid name!\n")
            continue

        try:
            name = int(name)
            print ("Enter a Valid name\n")
            continue

        except ValueError:
            name = name.lower()

        Add_appointment(date,time,name)
    
    elif choice == 2:
        display_appointments()

# The end massage
print ("Thank you, goodbye.")

# The bonus part
for name in bonus:
    print (f"- The Doctor {name} has {bonus[name]} Appointments")