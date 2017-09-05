from spy_details import spy,Spy
from start_chat import start_chat
from termcolor import colored

print colored("WELCOME TO SPYCHAT APPLICATION","cyan")
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N): "
existing = raw_input(question)

# <------------------validating users input--------------------->
# if the user chooses the default spy
if existing.upper() == "Y":
    # start the chat function is called
    start_chat(spy)
# the user wants to add a new user
elif existing.upper() == "N":
    # declare variables using a class
    spy = Spy(" ", " ", 0, 0.0)

    # Ask for the name
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    # Check if the name is entered or not
    if len(spy.name) > 0 and spy.name.isdigit() == False:
        # ask for the salutation
        spy.salutation = raw_input("What should we call you Mister or Miss?")
        # check if salutation is entered or not
        if len(spy.salutation) > 0:

            # Ask for the age of the spy
            spy.age = raw_input("Please enter your age: ")

            if len(spy.age) > 0:
                # raw input always gives a string to typecast age to int.
                spy.age = int(spy.age)
                # Age cannot be less than 12 and greater than 50
                # nested if
                if 12 <= spy.age < 50:
                    print("Welcome to SpyChat..!!!")

                    # Ask for spy_rating
                    spy.rating = raw_input("Please enter your spy rating: ")
                    if len(spy.rating) > 0:
                        # raw input always gives a string to typecast rating to float.
                        spy.rating = float(spy.rating)

                        # conditions to pass comments according to the spy_rating.
                        if spy.rating > 4.5:  # using if else condition to evaluate users rating
                            print colored('Excellent!','green')
                        elif spy.rating > 3.5 and spy.rating <= 4.5:
                            print colored('You are one of the good ones.','green')
                        elif spy.rating >= 2.5 and spy.rating <= 3.5:
                            print colored('You can do better','green')
                        else:
                            print colored('We can always use somebody to help in the office.','cyan')

                        # Make the spy come online
                        spy.is_online = True

                        # Call the start_chat function to start(the function will authenticate the user)
                        start_chat(spy)

                    # If spy rating is not entered
                    else:
                        print "Enter a valid spy rating"

                # valid age is not entered
                else:
                    # age is less than 12
                    if spy.age <= 12:
                        print(colored("Sorry , you are too young to become a spy!", 'red'))
                    # age is greater than equal to 50
                    elif spy.age >= 50:
                        print(colored("Sorry , you are too old to be a spy!", 'red'))
                    else:
                        print(colored("Please enter a valid age", 'red'))

            # if age is not entered
            else:
                print("Please enter your age")

        # the salutation is not entered
        else:
            print("Please enter a valid salutation")

    # the name is not entered
    else:
        print("Please enter a valid name")

else:
    print(colored("You did not reply with a yes(Y) or no(N)!", 'green'))
    exit()