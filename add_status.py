#<---------------IMPORT STATEMENTS------------>
from globals import STATUS_MESSAGES
from spy_details import spy
from termcolor import colored
#<-------------TO ADD STATUS------------->
def add_status():
    # in the beginning no status message
    updated_status_message = None

    # check if current status message is set or not
    if spy.current_status_message is not None:
        print 'Your current status message is %s \n' % spy.current_status_message
    else:
        print 'You don\'t have any status message currently \n'

    # Asking if the user wants to select a default status or a status which is already present
    default = raw_input(colored("Do you want to select from the older status (y/n)? ", "magenta"))

    # A spy wants to add another status rather from the existing one
    # .upper() converts from any case to upper case
    if default.upper() == "N":
        # ask the user to enter a new status
        new_status_message = raw_input(colored("What status message do you want to set?: ", "magenta"))

        # if valid status message is entered
        if len(new_status_message) > 0:
            # in the existing status list add the new status
            STATUS_MESSAGES.append(new_status_message)
            # variable update
            updated_status_message = new_status_message

    # A spy wants to choose from the existing status
    elif default.upper() == 'Y':

        # To give an index number to the statuses
        item_position = 1

        # To show all the default statuses so that the user can select
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        # Ask the user which index of the list he wants to choose.
        message_selection = int(raw_input(colored("\nChoose the index of the status: ", "magenta")))

        # Check if the position exists and then only set it
        if len(STATUS_MESSAGES) >= message_selection:
            # Variable update
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    # When the user chooses neither yes nor no
    else:
        print (colored('The option you chose is not valid! Press either y or n.','red'))

    # When the status message is updated
    if updated_status_message:
        print 'Your updated status message is:',
        print(colored(updated_status_message, "yellow"))

    # When it is not updated
    else:
        print(colored('You did not update your status message','red'))

    # The updated message will be read
    return updated_status_message