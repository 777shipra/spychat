#<-----------------------IMPORT STATEMENTS-------------------------->
from spy_details import friends
from select_friend import select_a_friend
from termcolor import colored
# function to read the chat history of friends
def read_chat_history():
    #read_for stores the value returned by select_a_friend()
    read_for = select_a_friend()

    print '\n'
    #iterating through friends chats list
    for chat in friends[read_for].chats:
        if chat.sent_by_me:#when True
            # The date and time is printed in blue
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'blue')),
            # The message is printed in red
            print(colored("You said:", 'red')),
            # black is by default
            print str(chat.message)
        else:#when False
            # The date and time is printed in blue
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'blue')),
            # The message is printed in red
            print(colored(str(friends[read_for].name) + " said:", 'red')),
            # Black color is by default
            print str(chat.message)

