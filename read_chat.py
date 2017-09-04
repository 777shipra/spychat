from globals import new_friend
from globals import friends
from select_friend import  select_friend
from termcolor import colored
def read_chat():

    for friend in friends:
        # print the message
        print "available friend's chat history:"
        print   friend['name']

    for friend in friends:
        read_for=raw_input("enter the name whose chat history u want to see:")
        if read_for==friend['name']:
            print friend['chats']
        else:
            print "<------NO SUCH FRIEND'S CHAT HISTORY------>"
