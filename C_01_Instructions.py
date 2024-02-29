# Generates heading (e.g. ***** Heading *****
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
- Enter an integer that is between 1 and 200 (inclusive) to output the factors of that integer
- If the integer is 1, it will tell you that 1 is unity as it only has one factor
- If the integer is a prime number, it will say so and only have two factors
- If the integer is a perfect square, it will say so and there will be an odd number of factors 
    ''')


# Main routine goes here

# Display instructions if required
want_instructions = input("Press <enter> to read the instructions or any key to continue")

if want_instructions == "":
    instructions()


print("program continues")



