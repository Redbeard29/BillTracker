from TotalDue import *

#each person's total amount put into main account every two weeks
total_biweekly_entry = 1425.00

#import total_cost_of_bills from TotalDue
total = getTotalMonthlyPayment(total_biweekly_entry)
#import total_monthly_bills from TotalDue
total_monthly_bills = calculateTotalCost()

print(f"${total:.2f}", f"${total_monthly_bills:.2f}")


#Goal is to create a billing audit log, so that I can see where potential discrepancies in money transferred/money spent occur
#Download CSV files from bank site and compare money entered and taken out to what is in this list of costs. Every time you
#transfer bill money for the two week period, you have to write to the audit log how much you entered, and if it doesn't match
#what's expected, where the over/under is coming from. 

def is_valid_input(cost):
    try:
        float(cost)
    except ValueError:
        return False
    else:
        return True

def valid_num_times(times):
    try:
        int(times)
    except ValueError:
        return False
    else:
        return True

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

total_entered = input("How much did you transfer for this two week period?:\n")

#account for user entering $num instead of just num
total_entered = total_entered.replace("$", "")

while not is_valid_input(total_entered):
    total_entered = input("Invalid entry. You must enter a number.\n")

total_entered = round(float(total_entered), 2)
acceptable_answers = ["N", "Y"]

if not total_entered == total_biweekly_entry:

    if total_entered > total_biweekly_entry:
        difference = total_entered - total_biweekly_entry
        print(f"You entered ${total_entered:.2f}, which is ${difference:.2f} more than expected. How many extra transactions are you accounting for?")
        sum_of_trans, num_of_trans = add_adjustments()

    else:
        difference = total_biweekly_entry - total_entered
        print(f"You entered ${total_entered:.2f}, which is ${difference:.2f} less than expected. How many transactions do you want to identify as not needed?")
        sum_of_trans, num_of_trans = add_adjustments()
    
    while sum_of_trans != difference:
        print("The amount entered does not equal the amount specified. Please re-enter adjustments.")
        print("How many extra transactions are you accounting for?")
        sum_of_trans, num_of_trans = add_adjustments()

    print(f"Sum of {num_of_trans} extra transactions: ${sum_of_trans:.2f}")

               
else:
    print(f"You entered ${total_entered:.2f}, which is exactly what was expected for this period.")