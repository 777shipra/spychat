# import statements
from spy_details import spy_name, spy_salutation, spy_age, spy_rating
from start_chat import  start_chat

print "Let's get started!"
question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N): "
existing = raw_input(question)

# validating users input
if (existing == 'Y' or existing == 'y') :
    # logic here.
    start_chat(spy_name, spy_age, spy_rating)
elif (existing == 'N' or existing == 'n'):
    # new users code here.
    spy_name = raw_input("Provide your name here :")
    # chek wether spy has input something or not
    if len(spy_name) > 0:
        # code block if the condition is true.
        # concatination of salutation and name.
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False
        spy_slautation = raw_input("What should we all you ? : ")
        spy_age = raw_input("Enter your age. ?")
        print type(spy_age)
        spy_age = int(spy_age)
        print type(spy_age)
        spy_name = spy_slautation + " " + spy_name
        print 'Welcome ' + spy_name + " Glad to have you back with us."
        print "Alright " + spy_name + "i'd like know liitle bit more about you before we proceed further."
    else:
        print "Invalid name. Try again."
else:
    print "Wrong choice. Try again."
