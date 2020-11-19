
def calculate_total_amount(loan_amount, number_of_years, interest_rate):
    total_amount = loan_amount * (1 + interest_rate / 100 * number_of_years)
    return total_amount

def calculate_interest_amount(loan_amount, number_of_years, interest_rate):
    interest_amount = loan_amount * interest_rate / 100 * number_of_years
    return interest_amount

def calculate_payments_amount(loan_amount, number_of_years, pay_back_condition, interest_rate):
    if pay_back_condition == 'w':
        number_of_payments = number_of_years * 52
    elif pay_back_condition == 'm':
        number_of_payments = number_of_years * 12
    else:
        number_of_payments = number_of_years
    return round(calculate_total_amount(loan_amount, number_of_years, interest_rate) / number_of_payments, 2)


while True:
    try:
        loan_amount = int(input("Please enter loan amount: "))
        number_of_years = int(input("Please enter loan terms(number of years): "))
        pay_back_condition = input("Please enter pay back condition('w' for weekly, 'm' for monthly, 'y' for yearly): ")
        if pay_back_condition not in ['w', 'm', 'y']:
            print('Wrong input')
            print('-------------------------------------------------------------------------------------------------------')
            continue
        interest_rate = int(input("Please enter yearly interest rate: "))
        print('----------------- Result ------------------')
        print('Total amount: ' + str(calculate_total_amount(loan_amount, number_of_years, interest_rate)))
        print('Interest amount: ' + str(calculate_interest_amount(loan_amount, number_of_years, interest_rate)))
        print('Payments amount: ' + str(calculate_payments_amount(loan_amount, number_of_years, pay_back_condition, interest_rate)))
        print('-------------------------------------------------------------------------------------------------------')

    except:
        print('Wrong input')
        print('-------------------------------------------------------------------------------------------------------')
        break