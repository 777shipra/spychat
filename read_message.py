<<<<<<< HEAD
from select_friend import select_friend
from steganography.steganography import Steganography

def read_message():
    # choose friend from the list
    sendr = select_friend()

    encrypted_image = raw_input("Provide encrypted image : ")
    secret_message = Steganography.decode(encrypted_image)
=======
from select_friend import select_friend
from steganography.steganography import Steganography

def read_message():
    # choose friend from the list
    sendr = select_friend()

    encrypted_image = raw_input("Provide encrypted image : ")
    secret_message = Steganography.decode(encrypted_image)
>>>>>>> d410c3ac9eb01e3cf7d066617243c76b57647683
    print secret_message