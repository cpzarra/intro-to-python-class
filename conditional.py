print "It's your birthday!"
answer = raw_input("How old are you? ")
age = int(answer)
if age < 21:
    print "You may not have a beer, but here's some juice!"
else:
    beers = raw_input("How many beers do you want?")
    beers = int(beers)
    if beers > 3:
        print "Oops, you're drunk!"
    elif beers > 1:
        print "You got a little tipsy"
    else:
        print "Looks like you're the designated driver"
print "Happy birthday!"
