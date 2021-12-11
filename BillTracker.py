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

total = 0

for key, val in bills.items():
    total += bills[key]
    total = round(total, 2)

print(total, (total_biweekly_entry * 4))

#Goal is to create a billing audit log, so that I can see where potential discrepancies in money transferred/money spent occur
#Download CSV files from bank site and compare money entered and taken out to what is in this list of costs. Every time you
#transfer bill money for the two week period, you have to write to the audit log how much you entered, and if it doesn't match
#what's expected, where the over/under is coming from. 

total_entered = round(float(input("How much did you transfer for this two week period?:\n")), 2)
print(f"You entered ${total_entered:.2f}")

if not total_entered == total_biweekly_entry:

    if total_entered > total_biweekly_entry:
        
        difference = total_entered - total_biweekly_entry

        print(f"You entered ${total_entered:.2f}, which is ${difference:.2f} more than expected. How many extra transactions are you accounting for?")
        num_of_trans = int(input())
        for trans in range(num_of_trans):
            reason = input(f"Transaction {trans + 1}:\n")    
            cost = round(float(input("How much?\n")), 2)
            print(f"Entered ${cost:.2f} for {reason}")
    else:

        difference = total_biweekly_entry - total_entered

        print(f"You entered ${total_entered:.2f}, which is ${difference:.2f} less than expected. How many transactions do you want to identify as not needed?")
        num_of_trans = int(input())
        for trans in range(num_of_trans):
            reason = input(f"Transaction {trans + 1}:\n")    
            cost = round(float(input("How much?\n")), 2)
            print(f"Subtracted ${cost:.2f} from total for {reason}")
else:
    print(f"${total_entered:.2f} is exactly what was expected for this period.")