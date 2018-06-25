# Define any function
def square(number):
    return number ** 2

# Pass the function to map along with an iterable
squares = map(square, range(10))
print squares