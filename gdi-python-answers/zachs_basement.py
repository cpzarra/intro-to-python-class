def basementIsOk(temperature, humidity):
    if temperature < 50 or humidity > 70:
        print "There's something wrong with the basement!"
    else:
        print "The basement is fine"

temp = raw_input("What's the basement's temperature? ")
temp = int(temp)
hum = raw_input("What's the basement's humidity percentage? ")
hum = int(hum)

basementIsOk(temp, hum)
