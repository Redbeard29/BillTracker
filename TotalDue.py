def getTotalMonthlyPayment(total_biweekly_entry):
    total_monthly_bills = total_biweekly_entry * 4
    return total_monthly_bills

def calculateTotalCost():
    total_cost_of_bills = 0
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


    for key, val in bills.items():
        total_cost_of_bills += bills[key]
        total_cost_of_bills = round(total_cost_of_bills, 2)

    return total_cost_of_bills