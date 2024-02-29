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


# Main routine goes here
while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break
