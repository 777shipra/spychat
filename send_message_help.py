from select_friend import select_a_friend
from spy_details import ChatMessage,friends
# Function to send a message of help in case of an emergency
def send_message_help():
    # Select the friend who had sent the emergency message
    friend_choice = select_a_friend()
    # Send the helping message text to the friend in emergency
    text = "I am coming to save you. Do not worry "
    # The message will be added in the chat
    new_chat = ChatMessage(text, True)
    # Add the message to the one who said.
    friends[friend_choice].chats.append(new_chat)

