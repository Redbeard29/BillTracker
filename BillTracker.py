from CalculateDifference import *
from TotalDue import *
from ValidateInputs import *
from AddAdjustments import * 

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

total_entered = input("How much did you transfer for this two week period?:\n")

#account for user entering $num instead of just num
total_entered = total_entered.replace("$", "")

while not is_valid_input(total_entered):
    total_entered = input("Invalid entry. You must enter a number.\n")

total_entered = round(float(total_entered), 2)

if not total_entered == total_biweekly_entry:

    sum_of_trans, num_of_trans = calculate_difference(total_entered, total_biweekly_entry)

    print(f"Sum of {num_of_trans} extra transactions: ${sum_of_trans:.2f}")

               
else:
    print(f"You entered ${total_entered:.2f}, which is exactly what was expected for this period.")