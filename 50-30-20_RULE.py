# I want to create a program that help the user managing them salary base on the rule 50-30-20.
"""The user will enter their monthly salary and actual spending 
for three categories: needs, wants, and savings. 
Following the 50-30-20 rule, the program will inform the user
about the recommended allocation for each category and calculate
the variance between the recommended and actual spending."""

# Information for the user about the rule 50-30-20.

print("\n*\n"*80)
print("The most accreditee Economist"
      "suggest that we should allocate our spending budget in 3 category: \n"
      "50% in NEED,\n30% in WANT,\n20% in SAVING \n"
      "Need include essential as Rent/Mortgage, bills, food and transport \n"
      "Want include not essential as eating out, shopping, trip etc. \n"
      "Saving is the budget dedicate to the future: saving, pension or pay debt\n")
print("\n*\n"*80)
print("The follow program will tell you if you are allocate your salary in a healthy way")
print("\n*\n"*80)


# Ask the user's salary and how his distribute inside the different categories.
# Loop function will keep asking user to enter valid date.
# The second loop make sure the salary's input is a valid data (a number different from 0).
while True:
    user_salary = input("to use the program we need to know your monthly salary after tax? \n")
    while True:
        if not user_salary.isdigit() or int(user_salary) <= 0:
            user_salary = input("Please enter a valid positive number for your salary? \n")
            continue
        else:
            print(f"your monthly salary is {user_salary}")
            break
    need = int(user_salary)*(50/100)
    want = int(user_salary)*(30/100)
    saving = int(user_salary)*(20/100)

    # Ask user how he is allocating his salary for the different category:
    print("*"*80)
    print("now we need to know how much you spend for each category monthly")
    print("")
    user_need = int(input("please enter your monthly spending for the category need:\n"))
    user_want = int(input("please enter your monthly spending for the category want:\n"))
    user_saving = int(input("please enter your monthly spending for the category saving:\n"))
    # We create the follow variable to verify if he is spending more/less or all his salary.
    total_user_spending = user_need + user_want + user_saving

    # Display if them allocation as perceptual is matching the rule 50-30-20.
    
    print("\nUsing the data you provide: \n")
    need_comparator = (user_need - need) / need * 100
    print(f"Your NEED category is {user_need},"
          f"which is {need_comparator:.2f}% "
          f"{'more' if need_comparator > 0 else 'less'} "
          "than recommended.")
    want_comparator = (user_want - want) / want * 100
    print(f"your WANT category is {user_want},"
          f"which is {want_comparator:.2f}% "
          f"{'more' if want_comparator > 0 else 'less'} than recommended")
    saving_comparator = (user_saving - saving) / saving * 100
    print(f"your SAVING category is {user_saving},"
          f"which is {saving_comparator:.2f}% "
          f"{'more' if saving_comparator > 0 else 'less'} than recommended")

    print("\n*\n"*80)
    # Display how suppose to be the ideal distribution of the salary.
    print("Base on your salary you ideal amount for the different category is:\n")
    print(f"Need = {need}")
    print(f"Want = {want}")
    print(f"Saving = {saving}\n")

    # This section is checking if the user has entered a saving amount
    # that is higher than their monthly salary.
    # If this condition is true, it means that the user has entered incorrect data, as
    # it is not possible to save more money than what they earn.
    # The program then asks the user to enter the correct salary amount."""

    if int(user_salary) <= int(user_saving) and int(user_salary) > int(user_need) and int(user_salary) > int(user_want):
        print("Your saving are more than your salary."
              "this is possible only if your entrance are more than what you declare")
        restart_program = input("Do you want to restart the program"
                                "to input the right entrance? (yes/no): ")
        if restart_program.lower() == "yes":
            continue
        else:
            break
    # The last part of the program will suggest some tips to the user
    if user_need == need and user_want == want and user_saving == saving:
        print("Well done, your monthly spending is well managing!!")
    elif total_user_spending > int(user_salary):
        print("Danger: you are spending over your salary, "
              "this will create a DEBT and will require more saving")
    elif total_user_spending < int(user_salary):
        print("Your are spending less than your salary. "
              "Where are the rest of the money? "
              "If your spending is less, try to allocate the rest of the salary on saving")
    elif user_need > need:
        print("Your Need category is too high, you have few option as ex."
              "re-negotiate your rent or change provider for your bills")
    elif user_need < need:
        print("Your Need category is lower than 50%,"
              "you can save more money for the future")
    elif user_need == need:
        print("Your Need category is well managed")
    elif user_want < saving:
        print("Is admirable how much you are saving, but don't forget to enjoy your life")
    break

# Display, with the user_saving category, how much the user will have when he'll retire.
# Ask two info: age of the user and age of retire
while True:
    age_user =input("How old are you?")
    if not age_user.isdigit() or int(age_user) <= 0:
        print("-- Invalid number")
        continue
    age_retire=input("at what age you will retire? ")
    if not age_retire.isdigit() or int(age_retire) <= 0:
        print("-- Invalid number")
        continue
    else:
        saving_retire = user_saving * (int(age_retire) - int(age_user))
        print(f"your total saving, "
              "without considering interest or other form of income, "
              f"at {age_retire} years old, will be: {round(saving_retire,2)}")
    break
print("")

