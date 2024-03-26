'''### --- OOP Email Simulator --- ###'''

# Create a class for emails
class Email:
    """
    The `class Email` defines a blueprint for creating email objects. 
    Within the class:`has_been_read = False` is a variable that is set to `False` by default.
    This variable is used to track whether an email has been read or not.
    - The `__init__` method is the constructor that initializes an Email object
    with the provided `email_address`, `subject_line`, and `email_content`.
    - The `mark_has_read` method is used to change the `has_been_read` variable 
    of an Email object from `False` to `True` when called.
    """
    has_been_read = False
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content


    # method to change the variable to True
    def mark_has_read(self):
        '''The `def mark_has_read(self):` method within the `Email` class 
        is a member function that changes the value of the `has_been_read` attribute 
        of an Email object from `False` to `True` when it is called.
        This method is used to mark an email as read,
        indicating that the recipient has viewed the email content.'''
        self.has_been_read = True


danila = Email("danila@gmail.com", "Test", "testing the functionality of the program")
seema = Email("seema@yahoo.com", "important", "read and share with the staff")
carla = Email("carla@mail.com", "new structure", "From now on the CCO will be Bruce White")

inbox = []
list_email = [danila, seema, carla]


def populate_inbox():
    """
    The `def populate_inbox():` function is responsible for populating the 
    `inbox` list with the email objects created earlier (danila, seema, carla)
    """
    inbox.extend(list_email)


def read_email(index):
    """
    The function `read_email(index)` reads the email at the given index in the inbox.
    It prints out the details of the email and marks it as read.
    """
    selected_email = inbox[index - 1]
    print("======================")
    print("Email Address:\t\t", selected_email.email_address)
    print("Subject:\t\t", selected_email.subject_line)
    print("Content:\t\t", selected_email.email_content)
    print("======================")


populate_inbox()


def list_emails():
    '''The `def list_emails():` function is responsible for displaying a list
    of emails in the inbox. 
    It iterates over the `inbox` list using the `enumerate` function to get 
    both the index and the email object.'''
    print("======================")
    for index, email in enumerate(inbox,1):
        print("Email Number:\t\t", index)
        print("Subject:\t\t", email.subject_line)
        print("======================")


MENU = True

while MENU is True:
    try:
        user_choice = int(input('''\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application

Enter selection: '''))
    except ValueError:
        print("Please insert a valid number")
        continue
    if user_choice < 1 or user_choice > 3:
        print("Please insert a valid number")

    elif user_choice == 1:
        list_emails()
        while True:
            num_choose = int(input("choose the email to read by"
                                   "selected the correspondent number: "))
            if num_choose < 0 or num_choose > len(inbox):
                print("please insert a valid number")
                continue
            else:
                read_email(num_choose)
                # Inside the loop where you mark the email as read
                inbox[num_choose - 1].mark_has_read()
                break

    elif user_choice == 2:
        unread_email = False
        for email in inbox:
            if not email.has_been_read:
                print("Subject:\t\t", email.subject_line)
                unread_email = True

    elif user_choice == 3:
        # Logic to exit the application
        print("Quitting application. Have a great day!")
        MENU = False

    else:
        print("Oops - incorrect input.")
