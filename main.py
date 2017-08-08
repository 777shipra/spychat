print "lets's get started"
spy_name = raw_input("provide your name here")
if len(spy_name) > 0:
    spy_salutation = raw_input("provide your salutation mr./ms.")
    if len(spy_salutation) > 0:
        spy_name = spy_salutation + " " + spy_name
        spy_age = 0
        spy_rating = 0.0
        spy_online = False
        spy_age = int(raw_input("enter your age please: "))
        if spy_age > 12 and spy_age < 50:
            spy_rating = float(raw_input("enter the rating"))

        else:
            print "You are notof  a correct age to be spy "
    else:
        print "Enter a Valid salutation..."


else:
    print "invalid name please try again "