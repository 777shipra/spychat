
from select_friend import select_friend
from steganography.steganography import Steganography

def read_message():
    # choose friend from the list
    sendr = select_friend()

    encrypted_image = raw_input("Provide encrypted image : ")
    secret_message = Steganography.decode(encrypted_image)

from select_friend import select_friend
from steganography.steganography import Steganography

def read_message():
    # choose friend from the list
    sendr = select_friend()

    encrypted_image = raw_input("Provide encrypted image : ")
    secret_message = Steganography.decode(encrypted_image)
    print secret_message