#each person's total amount put into main account every two weeks
total_biweekly_entry = 1425.00

bills = {
    'rent' : 1680.00,
    'power' : 100.00,
    'showtime' : 10.99,
    'ms_life_insurance' : 35.00,
    'hbo_max' : 14.99,
    'minol' : 85.00,
    'cable' : 15.40,
    'phone' : 333.00,
    'car' : 510.00,
    'spotify' : 12.99,
    'netflix' : 13.99,
    'state_farm' : 132.65,
    'bs_life_insurance' : 134.46,
    'gas' : 50.00,
    'daycare' : 1591.00,
    'ms_student_loans' : 220.00,
    'therapy' : 100.00,
    'xm_radio' : 22.08,
    'groceries' : 500.00
}

total_monthly_bills = total_biweekly_entry * 4
total = 0

for key, val in bills.items():
    total += bills[key]
    total = round(total, 2)

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
        if sum_of_trans < difference:
            trans_difference = difference - sum_of_trans
            print(f"You entered ${sum_of_trans:.2f}, which is ${trans_difference:.2f} short of ${difference:.2f}. How many more transactions would you like to add to account for this difference?")
            sum_of_extra_trans, num_of_extra_trans = add_adjustments()
            sum_of_trans += sum_of_extra_trans
            num_of_trans += num_of_extra_trans

        else:
            trans_difference = sum_of_trans - difference
            print(f"You entered ${sum_of_trans:.2f}, which is ${trans_difference:.2f} too much. Please re-enter adjustments in an amount totalling ${difference:.2f}. How many transactions are you accounting for?")
            sum_of_trans, num_of_trans = add_adjustments()

    print(f"Sum of {num_of_trans} extra transactions: ${sum_of_trans:.2f}")

               
else:
    print(f"You entered ${total_entered:.2f}, which is exactly what was expected for this period.")