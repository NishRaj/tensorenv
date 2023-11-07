def remaining_bal_year(balance, annual_interest_rate, min_amount) -> float:
    remaining_bal = balance
    # Start counting at the start of the month.
    for months in range(1, 13):
        #min_amount = balance * monthly_payment_rate
        unpaid_amount = balance - min_amount
        interest_amount = unpaid_amount * (annual_interest_rate / 12)
        balance = unpaid_amount + interest_amount
    print("Remaining balance:", round(balance, 2))
    return balance

def min_fixed_monthly_payment(balance, annual_interest_rate) -> float:
    guess = 10.0
    while True:
        balance_after_year = remaining_bal_year(balance, annual_interest_rate, guess)
        if balance_after_year <= 0:
            break
        else:
            guess += 10
    return guess

def min_fixed_monthly_payment_bisection(balance, annual_interest_rate) -> float:
    monthly_interest_rate = annual_interest_rate/12
    lower_amount = balance/12
    higher_amount = (balance * (1 + monthly_interest_rate)**12) / 12.0
    result = (lower_amount + higher_amount)/ 2.0
    epsilon = .01
    rem_balance = balance
    while abs(rem_balance) >= epsilon:
        rem_balance = remaining_bal_year(balance, annual_interest_rate, result)
        if rem_balance > 0 and rem_balance <= epsilon:
            break
        elif rem_balance < 0:
            higher_amount = result
        else:
            lower_amount = result
        result = (higher_amount + lower_amount)/2.0
    return round(result, 2)

print(min_fixed_monthly_payment_bisection(320000,0.2))






