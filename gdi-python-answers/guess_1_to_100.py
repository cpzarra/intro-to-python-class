play_again = 'y'

while(play_again == 'y'):
    secret_number = 55
    guess = raw_input("Guess a number from 1 to 100:")
    guess = int(guess)

    if abs(secret_number - guess) > 50:
        print "Cold"
    elif abs(secret_number - guess) > 20:
        print "Cool"
    elif abs(secret_number - guess) > 10:
        print "Warm"
    elif abs(secret_number - guess) > 5:
        print "Hot"
    elif abs(secret_number - guess) > 0:
        print "Scalding!!!"
    else:
        play_again = raw_input("You guessed correct! Do you want to play again? (y/n):")
