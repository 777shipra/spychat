from globals import new_friend
from globals import friends
from select_friend import  select_friend
def read_chat():
    select_friend()

    name = raw_input("whose chat you want to see:")
    for friend in friends:
        if new_friend['name'] == name:
            print new_friend['chats']




