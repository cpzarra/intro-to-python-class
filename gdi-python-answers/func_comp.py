def get_name():
    return raw_input("What is your name?")

def get_email_address():
    return raw_input("What is your address?")

def register():
    print "Please fill out the following information to register:"
    name = get_name()
    email = get_email_address()
    print name, "is registered under the email address", email

register()
            