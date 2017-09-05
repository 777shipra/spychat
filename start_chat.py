#<------------------------------IMPORT STATEMENTS------------------------>
from add_status import add_status
from add_friend import add_friend
from send_a_message import send_a_message
from read_a_message import read_a_message
from send_message_help import send_message_help
from read_chat_history import read_chat_history
from termcolor import colored
#function shows the main menu of the application
#function contains all the functions
def start_chat(spy):
    # updated variable
    spy.name = spy.salutation + " " + spy.name
    # Age cannot be less than 12 or greater than 50
    if 12 < spy.age < 50:

        # Authentication complete
        # Show a message with all te spy details
        print"Authentication complete."
        print(colored("Welcome " + str(spy.name), "grey"))
        print(colored("Your age:" + str(spy.age), "grey"))
        print(colored("Your rating:"+str(spy.rating), "grey"))
        print(colored("Bravo!Proud to have you on board.", "yellow"))

        # Can be done in this way also print "Authentication complete. Welcome %s, age: %d and rating of: %.2f.Proud
        # to have you on board" % (spy.name, spy.age, spy.rating)

        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n" \
                           " 2. Add a friend \n 3. Send a secret message \n " \
                           "4. Read a secret message \n 5. Read Chats from a user \n" \
                           " 6. Close Application \n"
            # Taking the input of the choice
            menu_choice = raw_input(colored(menu_choices, "blue"))

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    # Set your current status
                    spy.current_status_message = add_status()

                elif menu_choice == 2:
                    # Add a new friend
                    number_of_friends = add_friend()
                    print 'You have %d friends' % number_of_friends

                elif menu_choice == 3:
                    # Send a secret message
                    send_a_message()

                elif menu_choice == 4:
                    # Read the secret message sent by your friend
                    read_a_message()

                elif menu_choice == 5:
                    # Read the chat history
                    read_chat_history()

                elif menu_choice == 6:
                    # Close the app
                    print(colored("we will miss you", "green"))
                    show_menu = False

                # When the user chooses other than the menu choices.
                else:
                    print(colored("That was a wrong choice.", 'red'))
                    exit()
