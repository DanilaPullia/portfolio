"""
Create a program that take food order online
# the user can choose between different cuisine and plates
# in this casa to simplify I define just to cuisine and 2 plates for cuisine
# depend of how many plates he will buy, the program will provide the right receipt
"""

print("*"*80)
print("Welcome to your food order online")
print("")
print("*"*80)


# define menu
menu = [1, 2]

# define the list for the 2 different cuisine
italian_menu = ["carbonara", "matriciana"]
indian_menu = ["naan", "roti"]

ITALIAN_COST_PER_PLATE = 20
INDIAN_COST_PER_PLATE = 10

def get_cuisine_choice(cuisine_menu):
    """
    The function `get_cuisine_choice` prompts the user to choose a cuisine from a
    given menu and returns the user's choice if it is valid.
    
    :param cuisine_menu: A list of available cuisine options
    :return: the user's choice of cuisine from the given cuisine menu.
    """
    while True:
        menu_user_choice = input(f"Nice choice! You can now choose between {', '.join(cuisine_menu)}\n")
        menu_user_choice = menu_user_choice.lower()

        if menu_user_choice in cuisine_menu:
            return menu_user_choice
        else:
            print("Invalid choice. Please enter your choice again.")

# Function to get the quantity of plates
def get_quantity_plate():
    """
    The function get_quantity_plate is used to retrieve the quantity of plates.
    """
    while True:
        try:
            quantity = float(input("How many plates would you like? "))
            return quantity
        except ValueError:
            print("Please enter a valid number.")

# Function to calculate and print the order details
def print_order_details(choice, quantity, cost_per_plate):
    """
    The function takes in the choice of food, quantity, and cost per plate, and
    prints the order details.
    
    :param choice: The choice parameter represents the item that the customer has
    chosen to order. It could be a food item, a product, or any other item that the
    customer wants to purchase
    :param quantity: The quantity parameter represents the number of plates ordered
    :param cost_per_plate: The cost per plate is the price of each plate or item in
    the order
    """
    total_cost = cost_per_plate * quantity
    print("\nOrder Details:")
    print("Your choice:", choice)
    print("Quantity:", quantity)
    print("Total to pay: £", total_cost)

# Main program
print("*" * 80)
print("Welcome to your food order online")
print("*" * 80)

# Display cuisine options
print("Which kind of cuisine would you like to order today?\n")
print("1 - Italian")
print("2 - Indian\n")

# Get user input for cuisine choice
user_cuisine_choice = None
while user_cuisine_choice not in menu:
    try:
        user_cuisine_choice = int(input("Choose the cuisine you prefer by entering the relative number: "))
        if user_cuisine_choice not in menu:
            print("Sorry, we need a number between 1 and 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Process user's choice
if user_cuisine_choice == 1:
    user_choice = get_cuisine_choice(italian_menu)
    quantity_plate = get_quantity_plate()
    print_order_details(user_choice, quantity_plate, ITALIAN_COST_PER_PLATE)

elif user_cuisine_choice == 2:
    user_choice = get_cuisine_choice(indian_menu)
    quantity_plate = get_quantity_plate()
    print_order_details(user_choice, quantity_plate, INDIAN_COST_PER_PLATE)

