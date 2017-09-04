#import statements
from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends

def send_message():
    # choose a friend from the list.
    friend_choice = select_friend()

    # prepare the message
    original_image = raw_input("Provide the name of the image to hide the message : ")
    output_image = raw_input("Provide the name of the output image  : ")
    text = raw_input("Enter your message here : ")
    if len(text)==0 :
        print "<---NO MESSAGE,TRY AGAIN & WRITE SOMETHING--->"
    else:
        # Encrypt the message
        Steganography.encode(original_image, output_image, text)

        # Successful message
        print "Your message encrypted successfully."

        #save chats
        new_chat={
            'message': [] ,
            'date': [],
            'send_be_me':True

        }
        new_chat['message'].append(text)#appending messages in newchat['message']
        new_chat['date'].append(datetime.now())#appending date and time
        friends[friend_choice]['chats'].append(new_chat)
        print "your secret message is ready"
