from mortgage import Loan


home_price = 130000.0
down_payment = 13000.0
interest_rate = 2.625
term = 30
loan_amount = home_price - down_payment

loan = Loan(loan_amount, interest_rate/100.0, 30)
#print(loan.monthly_payment)
interest, principle = loan.split_payment(1, loan.monthly_payment)
#print(interest)
#print(principle)
for down_payment in [10000, 13000]:
    print("-"*80)
    print("Down payment = {}".format(down_payment))
    loan_amount = home_price - down_payment
    loan = Loan(loan_amount, interest_rate / 100.0, 30)
    interest, principle = loan.split_payment(1, loan.monthly_payment)
    equity_after_5_year = 0.0
    interest_after_5_year = 0.0
    for month in range(1, 5*12+1):
        interest, principle = loan.split_payment(month, loan.monthly_payment)
        equity_after_5_year += float(principle)
        interest_after_5_year += float(interest)
    print("Monthly payment: {}".format(loan.monthly_payment))
    print("Principle paid in 5 year: {}".format(equity_after_5_year))
    print("Interest paid in 5 year: {}".format(interest_after_5_year))
    print("Down payment + principle paid: {}".format(down_payment + equity_after_5_year))

# Putting 3,000 into stocks, with an 8% return
print("-"*80)
gains = (3000.0*((1+(0.01*20)) ** 5)) - 3000
print("Gained in stock market: {}".format(gains))
PMI_cost = 28 * 5 * 12
print("Spent on PMI={}".format(PMI_cost))
print("Delta = {}".format(gains - PMI_cost))
