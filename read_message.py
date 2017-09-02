
from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends

def read_message():
    # choose friend from the list
    sender = select_friend()

    encrypted_image = raw_input("Provide encrypted image : ")
    secret_message = Steganography.decode(encrypted_image)
    # save chats
    new_chat = {
        'message': secret_message,
        'date': datetime.now(),
        'send_be_me': False

    }
    friends[sender]['chats'].append(new_chat)
    print "your secret message has been saved"

