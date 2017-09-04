from globals import friends#import statement
#function to select friend from the list
def select_friend():
    counter = 1
    for friend in friends:
        #print the message
        print str(counter) + ". " + friend['name'] + " " + "Age : " + str(friend['age'])
        counter = counter + 1

    result = int(raw_input("Select from the list : "))
    #as index starts from 0
    return result - 1