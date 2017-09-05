#<------------------------IMPORT STATEMENTS------------------>
from select_friend import select_a_friend
from spy_details import ChatMessage,friends
from termcolor import colored
from steganography.steganography import Steganography
# Function to send a secret message
def send_a_message():
    # Select a friend to whom you want to communicate with
    friend_choice = select_a_friend()

    # Select the image in which you want to write a secret message
    original_image = raw_input("What is the name of the image?: ")

    # the output path of the image where the message is stored
    output_path = "output.jpg"
    # write the secret message
    text = raw_input("Enter your secret message: ")

    # The library steganography that helps to encode the message
    Steganography.encode(original_image, output_path, text)

    # The text message wil be stored in chat messages
    new_chat = ChatMessage(text, True)

    # Along with the name of the friend we add the message
    friends[friend_choice].chats.append(new_chat)

    # After the encoding is done the message is ready.
    print(colored("Your secret message image is ready!", "green"))