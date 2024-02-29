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


# Main routine goes here

# Display instructions if required
statement_generator("The Ultimate Factor Finder", "*")

want_instructions = input("Press <enter> to read the instructions or any key to continue")

if want_instructions == "":
    instructions()


print("program continues")
