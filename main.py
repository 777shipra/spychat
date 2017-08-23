# import statements
from spy_details import spy
from start_chat import  start_chat


print "Let's get started!"
question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N): "
existing = raw_input(question)

# validating users input
if (existing == 'Y' or existing == 'y') :
    # logic here.
    start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
elif (existing == 'N' or existing == 'n'):
    # new users code here.
    spy['name'] = raw_input("Provide your name here :")
    # chek wether spy has input something or not
if len(spy['name']) > 0:

    # String Concatenation using + symbol
    print 'Welcome ' + spy['name'] + '. Glad to have you back with us.'

    spy['salutation'] = raw_input("Should I call you Mister or Miss?: ")

    # Variable has been updated
    spy['name'] = spy['salutation'] + " " + spy['name']

    print "Alright " + spy['name'] + ". I'd like to know a little bit more about you before we proceed..."


    # Let's create some new variables
    while True:
        try:
            spy['age'] = raw_input("What is your age?")
            break

        except ValueError:
            print "Invalid age and Try Again"




    # Age cannot be less than 12 and no spies greater than 50 are allowed to exist
    # Nested if
    if spy['age'] > 12 and spy['age'] < 50:

        spy['rating'] =float( raw_input("What is your spy rating?"))


        if spy['rating'] > 4.5:
            print 'Great ace!'
        elif spy['rating'] > 3.5 and spy['rating'] <= 4.5:
            print 'You are one of the good ones.'
        elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'

        # Let's make this spy come online
        spy['is_online'] = True

        # One final message with all the details
        print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str(
            spy['rating']) + " Proud to have you onboard"

        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
    else:
        print 'Sorry you are not of the correct age to be a spy'


else:

    print "A spy needs to have a valid name. Try again please."

