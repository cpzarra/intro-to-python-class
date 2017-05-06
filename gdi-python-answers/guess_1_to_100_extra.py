play_again = 'y'
last_guess = None

while(play_again == 'y'):
    secret_number = 55
    guess = raw_input("Guess a number from 1 to 100:")
    guess = int(guess)

    if last_guess:
        if abs(secret_number - guess) > abs(secret_number - last_guess):
            print "Colder"
        elif abs(secret_number - guess) < abs(secret_number - last_guess):
            print "Warmer"

    last_guess = guess

    play_again = raw_input("Do you want to play again? (y/n):")
