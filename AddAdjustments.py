from ValidateInputs import *

acceptable_answers = ["N", "Y"]

def add_adjustments():
    
    num_of_trans = input()
    while not valid_num_times(num_of_trans):
        num_of_trans = input("Invalid entry. You must enter a whole number.\n")

    num_of_trans = int(num_of_trans)
    sum_of_trans = 0

    for trans in range(num_of_trans):
        reason = input(f"Transaction {trans + 1}:\n")    
        cost = input("How much?\n")
        #account for user entering $num instead of just num
        cost = cost.replace("$", "")

        while not is_valid_input(cost):
            cost = input("Invalid entry. You must enter a number.\n")

        cost = round(float(cost), 2)
        print(f"Entered ${cost:.2f} for {reason}")
        
        sum_of_trans += cost

        create_note = input("Enter associated notes? Y/N\n").upper()
        
        while create_note not in acceptable_answers:
            create_note = input("Invalid entry. Please enter Y or N.\n").upper()

        if create_note == acceptable_answers[1]:
            note = input(f"Notes for ${cost:.2f} {reason}:\n")
            print(f'"{note}" stored as notes for {reason}')
    
    return sum_of_trans, num_of_trans