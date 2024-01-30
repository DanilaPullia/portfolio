import math


# I want the user to know what to do, to have access to the service.
print("Welcome to your interest calculator program")
print("\nPlease tell us which calculator you want to use today?")
print("Investment: to calculate the amount of interest you'll earn in your investment")
print("Bond: to calculate the amount you'll have to pay on a home loan\n")

# Variables that we will recall in the program.
option_investment = "INVESTMENT"
option_bond = "BOND"
option_combined = option_investment + option_bond

simple_interest = "SIMPLE"
compound_interest = "COMPOUND"
interest_list = simple_interest + compound_interest


# Ask the user to make a choice between investment or bond.
interest = input("Write 'investment' or 'bond' to select your choose \n")
# Use upper method to make user input case-insensitive.
interest = interest.upper()

# While loop gives error for input other then Investment or Bond.
while interest not in option_combined:
    print("Sorry this is not a valid data, please try again: \n")
    interest = input("Write 'investment' or 'bond' to select your choose \n")
    interest = interest.upper()

# The follow block will run when a user selects the investment option.
if interest in option_investment:
    print("Perfect! We will help you with your Investment\n")
    # Ask inputs from user, to calculate the interest of the investment.
    # While loop gives error for invalid input.
    while True:
        try:
            deposit = float(input("Write the amount of money you want to deposit: "))
            rate = float(input("Write the interest rate in number only without % "))
            years = float(input("How many years do you want to invest? "))
            break
        except ValueError:
            print("Please insert a valid data")

    interest_user_choice = input("Which interest do you want: simple or compound? ")
    interest_user_choice = interest_user_choice.upper()
    while interest_user_choice not in interest_list:
        interest_user_choice = input("Invalid input: "
                                    "which interest do you want: "
                                    "simple or compound? ")
        interest_user_choice = interest_user_choice.upper()

    print(" ")
    print(f"Your deposit is {deposit}",
        f"your rate is {rate / 100} %" ,
        f"your years are {years} ",
        f"your interest is {interest_user_choice}")

    # Calculate and return the Simple interest for the investment.
    if interest_user_choice in simple_interest:
        result_simple_inv = deposit * (1 + (rate / 100) * years)
        result_simple_round = round(result_simple_inv,2)
        print(f"This is want you will earn: {result_simple_round}")

    # Calculate and return the Compound interest for the investment.
    if interest_user_choice in compound_interest:
        result_compound_inv = deposit * math.pow((1 + (rate / 100)), years)
        result_compound_round = round(result_compound_inv,2)
        print(f"This is want you will earn: {result_compound_round}")

# The follow block run when user chooses Bond.
else:
    print("Perfect! We will help you with your Bond\n")
    # Ask inputs from user, to calculate the repayment of the bond.
    while True:
        try:
            value_house = float(input("What is the value of the house? "))
            rate_bond = float(input("Write the interest rate in number only without %"))
            rate_bond_user = (rate_bond / 100) / 12
            months = float(input("How many month to repay the Bond? "))
            print(f"The value of the house is {value_house},"
                  f"the rate is {rate_bond / 100}," 
                  f"months to repay are {months}")
            break
        except ValueError:
            print("Please insert a valid data")

    # Calculate the Bond repayment.
    monthly_payment = (rate_bond_user * value_house) / (1 -(1 + rate_bond_user) ** (- months))
    monthly_payment = round(monthly_payment, 2)
    print(f"This is you monthly payment: {monthly_payment}")

print(" ")
print("THANKS FOR USE OUR SERVICE")
