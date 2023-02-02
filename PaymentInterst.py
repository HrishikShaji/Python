def main():
    print("This is a monthly paymentt loan calculator\n")

    principal = float(input("enter the loan amount:"))
    apr = float(input("enter the annual interest rate:"))
    years = int(input("enter the amount of years:"))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 +monthly_interest_rate) ** (-amount_of_months))

    print("monthly payment is : " + str(monthly_payment))

main()