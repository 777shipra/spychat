from spy_details import friends
from select_friend import select_a_friend
from termcolor import colored
# function to read the chat history
def read_chat_history():
    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            # The date and time is printed in blue
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'blue')),
            # The message is printed in red
            print(colored("You said:", 'red')),
            # black is by default
            print str(chat.message)
        else:
            # The date and time is printed in blue
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'blue')),
            # The message is printed in red
            print(colored(str(friends[read_for].name) + " said:", 'red')),
            # Black color is by default
            print str(chat.message)

