from select_friend import select_a_friend
from spy_details import friends
from send_message_help import send_message_help
from spy_details import ChatMessage
from termcolor import colored


def read_a_message():
    # Select a friend to communicate with
    sender = select_a_friend()
    output_path = raw_input("What is the name of the image file?: ")

    # Error handling if a secret message is present or not
    try:
        secret_text = Steganography.decode(output_path)
        print "The secret message you read is",
        print (colored(secret_text, 'red'))
        words = secret_text.split()
        # Convert all the words into uppercase
        new = (secret_text.upper()).split()

        # Maintain the average number of words spoken by a spy every time a message is received from a particular spy.
        friends[sender].count += len(words)

        # Emergency words are present
        if "SOS" in new or "SAVE" in new or "HELP" in new or "AID" in new or "ACCIDENT" in new or "RESCUE" in "ALERT" in new or "ALARM" in new or "CRISIS" in new:

            # Emergency alert
            print(colored("!", 'grey', 'on_yellow')),
            print(colored("!", 'grey', 'on_yellow')),
            print(colored("!", 'grey', 'on_yellow'))

            # Help your friend by sending him a helping message
            print (colored("The friend that sent this message needs an emergency.", 'green'))
            print (colored("PLease help your friend by sending a helping message.", 'green'))
            print (colored("Select that friend to send him a helping message.", 'red'))

            # Calling the send message help function
            send_message_help()
            # The message is sent successfully
            print(colored("You have sent a message to help your friend.", 'magenta'))

            # Adding the chat with the sender
            new_chat = ChatMessage(secret_text, False)
            friends[sender].chats.append(new_chat)

        # When there was no case of emergency
        else:
            # Adding the chat with the sender
            new_chat = ChatMessage(secret_text, False)
            friends[sender].chats.append(new_chat)
            print(colored("Your secret message has been saved!", 'yellow'))

        # Print the avg words spoken by your friend
        print "Average words said by",
        print(colored(friends[sender].name, "blue")),
        print "is",
        print(colored(friends[sender].count, "red"))

        # Delete a spy from your list of spies if they are speaking too much
        if len(words) > 100:
            print(colored(friends[sender].name, 'blue')),
            print(colored("removed from friends list.What a chatter box!.What a drag!!!", "yellow"))
            # Removes that chatterbox friend
            friends.remove(friends[sender])

    # When the image contains no secret message
    # 'TypeError' handling
    except TypeError:
        print(colored("Nothing to decode from the image as it contains no secret message.", 'red'))
