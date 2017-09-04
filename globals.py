# global variables and constants here.

# current status message is initialized to None.
current_status_message = None

# list to store status messages.
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

# lists to store users friends information.
friends = []
#<--------------dictionary to be appended in friends[]------------->
new_friend = {
    'name': '',
    'salutation': '.',
    'age': 0,
    'rating': 0.0,
    'is_online': False,
    'chats': []
}