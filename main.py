#import modules
from user import registerUser, loginUser

# start program function
def startPage():
    print("\n--------Welcome To Crownd-Funding Application-------")
    while True:
        try:
            print("1- Sign Up\n2- Login\n3-Exit\n")
            account = int(input("Enter Your Choice: "))
            if (account == 1):
                is_valid = True
                registerUser()
            elif (account == 2):
                is_valid = True
                loginUser()
            elif account == 3:
                break
            elif is_valid != True:
                print("\nInvalid Choice, Please Enter 1 or 2 or 3\n")
        except ValueError:
            print("\nInvalid Choice, Please Enter 1 or 2 or 3\n")


# run the program
startPage()
