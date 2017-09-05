#<------------------------IMPORT STATEMENTS--------------------------->
from spy_details import friends
from termcolor import colored
#FUNCTION TO SELECT A FRIEND FROM THE LIST
def select_a_friend():
    # indexing the position of a friend
    item_number = 0

    # To select a friend with the indexing
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name, friend.age, friend.rating)

        item_number = item_number + 1

    # Ask the user which friend he want to have a chat with
    friend_choice = raw_input(colored("Choose the index of the friend: ", "blue"))
    # The friend will be selected
    friend_choice_position = int(friend_choice) - 1

    # Check if the user chooses index out of range
    if friend_choice_position + 1 > len(friends):
        print(colored("Sorry,This friend is not present.", 'red'))
        exit()

    else:
        # returns the selected friend to perform the options
        return friend_choice_position
