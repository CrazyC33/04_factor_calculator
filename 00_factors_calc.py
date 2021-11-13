# Certain Things were not in the video, so I could only complete this much as I had no way
# to def get_factors and complete it.
def statement_generator(text, decoration):

    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represent in 24 bit colour (ie: 24 bits per pixel). For text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""

def num_check(question, low):
    valid = False
    while not valid:
        
        error = "Please enter an integer that is more than"
        "(or equal to) {}".format(low)

        try:
            
            response = int(input(question))
            
            if response >= low:
                return response
            
            else: 
                print(error)
                print()
        
        except ValueError:
            print("error")        

def get_factors(to_factor):

    
# Main Routine
statement_generator("Factors Calculator", "-")

first_time = input("Please <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

keep_going = ""
while keep_going == "":
    
    comment = ""

    var_to_factor != num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()