from AddAdjustments import *

def calculate_difference(total_entered, total_biweekly_entry):

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

    return sum_of_trans, num_of_trans