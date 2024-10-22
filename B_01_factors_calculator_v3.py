# Generates heading (e.g. ***** Heading *****
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
To use this program, simply enter an integer between 
1 and 200 (inclusive). The program will show the factors of 
your chosen integer.

It will also tell you if your chosen number ...
- is unity (1) as it only has one factor
- is a prime number (i.e. it has two factors)
- is a perfect square

To exit the program, please type 'xxx' 
    ''')


# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = f"Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # Ask the user for a number
            response = int(response)

            # Check that the number is more than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Gets factors, returns a sorted list
def get_factors(to_factor):
    # x**(0.5) is the square root of x

    # We want to loop until we get to the square root of to_factor
    # stop is the square root of the factor.
    # Basically instead of going from one to the number,
    # we go from 1 to 'stop' (which is the square root
    # of the number we are trying to factorise)

    factors_list = []

    # Square root the number to work out when t stop looping
    stop = to_factor ** 0.5
    stop = int(stop)

    

    for item in range(1, stop + 1):

        # if modulo is zero, then the number is a factor
        if to_factor % item == 0:
            # Add first factor to list
            factors_list.append(item)

            # find second factor by dividing 'to factor' by the first factor
            partner = to_factor // item

            # check second factor is not in list and add it
            if partner not in factors_list:
                factors_list.append(partner)

    # output
    factors_list.sort()
    return factors_list


# Main routine goes here
# Heading
statement_generator("The Ultimate Factor Finder", "*")

# Displays instructions if user has not used the program before
want_instructions = input("Press <enter> to read the instructions or any key to continue")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    # Ask user for number to be factorised ...
    to_factor = num_check("\nEnter an integer (or xxx to quit): ")

    if to_factor == "xxx":
        break

    # Get factors for integers that are 2 or more
    elif to_factor != 1:
        factor_list = get_factors(to_factor)

    # Set up comment for unity
    else:
        comment = "One is UNITY! It only has one factor. Itself :)"
        factor_list = ""

    # Comments for squares/primes

    # Prime numbers have only two factors
    if len(factor_list) == 2:
        comment = "{} is a prime number. ".format(to_factor)

    # Check if the list has an odd number of factors
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(to_factor)

    # Output factors and comment
    if to_factor > 1:
        heading = f"Factors of {to_factor}"

    else:
        heading = "One is special ..."

    # Output factors and comment
    print()
    statement_generator(heading, "*")
    print(factor_list)
    print(comment)

    print("Thank you for using the Ultimate Factor Finder")
