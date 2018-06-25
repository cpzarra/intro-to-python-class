input_value = raw_input('Enter a positive integer:')
user_number = int(input_value)
while user_number > 0:
    print "The user's number is still positive, let's subtract 1"
    user_number = user_number - 1
    print user_number
print "User's number is no longer positive."