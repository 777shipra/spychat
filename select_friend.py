<<<<<<< HEAD
from globals import friends

def select_friend():
    counter = 1
    for friend in friends:
        print str(counter) + ". " + friend['name'] + "Age : " + str(friend['age'])
        counter = counter + 1

    result = int(raw_input("Select from the list : "))
=======
from globals import friends

def select_friend():
    counter = 1
    for friend in friends:
        print str(counter) + ". " + friend['name'] + "Age : " + str(friend['age'])
        counter = counter + 1

    result = int(raw_input("Select from the list : "))
>>>>>>> d410c3ac9eb01e3cf7d066617243c76b57647683
    return result - 1