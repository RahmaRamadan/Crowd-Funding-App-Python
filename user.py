#import modules
from project import createNewProject, viewAllProjects, searchForProject, deleteProject
# global variables
is_valid = False
email_valid = False
pass_valid = False
phone_valid = False
login_valid = False
project_input_valid = False
projectData_valid = False

#---------------------------Users Functions-----------------------------
def registerUser():
    global email_valid, pass_valid, phone_valid
    f_name = input("Enter Your First Name: ")
    l_name = input("Enter Your Last Name: ")
    phone_valid = False
    while phone_valid == False:
        phone = input("Enter your phone number: ")
        phoneValidation(phone)

    email_valid = False
    while email_valid == False:
        email = input("Enter Your Email: ")
        emailValidation(email)

    pass_valid = False
    while pass_valid == False:
        password = input("Enter Your Password: ")
        confirm_password = input("Enter Your Confirm Password: ")
        passValidation(password, confirm_password)
    if (email_valid and pass_valid and phone_valid == True):
        with open('data', 'a') as dataFile:
            input_data = [f_name, " ", l_name, " ",
                          email, " ", phone, " ", password, "\n"]
            dataFile.writelines(input_data)
#-----------------------------------------------------------------------

def loginUser():
    global login_valid, project_input_valid, projectData_valid
    login_valid = False
    while login_valid == False:
        login_email_input = input("Enter your email: ")
        login_pass_input = input("Enter your password: ")
        loginValidation(login_email_input, login_pass_input)

    if login_valid == True:
        while True:
            project_input_str = input(
                "1- Create a new project\n2- Show All Projects\n3- Search Project\n4- Delete Project\nEnter You Choice: ")
            project_input = int(project_input_str)
            if project_input == 1:
                project_input_valid = True
                createNewProject(login_email_input)
            elif project_input == 2:
                project_input_valid = True
                viewAllProjects()
            elif project_input == 3:
                project_input_valid = True
                searchForProject()
            elif project_input == 4:
                project_input_valid = True
                deleteProject(login_email_input)
            elif projectData_valid != True:
                print("\nInvalid Choice, Please Enter 1 or 2 or 3\n")
#-----------------------------------------------------------------------

def emailValidation(email):
    global email_valid
    found = False
    email = email.strip().lower()
    if not "@" in email:
        print("Invalid email format. Email must contain '@'!\n")
        email_valid = False
    elif not email[-4:] in ".com.org.edu.gov.net":
        print("Invalid email format. Email must contain 'dot'!\n")
        email_valid = False
    else:
        email_valid = True

    if email_valid == True:
        with open("data", "r") as output:
            lines = output.readlines()
            for field in lines[0:]:
                if email in field:
                    found = True
                    break
                else:
                    found = False
        if found == True:
            print("\nThis email already exists!\n")
            email_valid = False
        else:
            email_valid = True
#-----------------------------------------------------------------------

def passValidation(password, conpassword):
    global pass_valid
    if password == conpassword:
        pass_valid = True
    elif password != conpassword:
        print("Password and confirm password does not match!\n")
        pass_valid = False
#-----------------------------------------------------------------------

def loginValidation(email, password):
    global login_valid
    found = False
    with open("data", "r") as output:
        lines = output.readlines()
        for field in lines[1:]:
            if (email == field.split()[2]) and (password == field.split()[4]):
                found = True
                break
            else:
                found = False

    if found == True:
        print("Valid Email And Password :D\nLogin Successfully\n")
        login_valid = True
    else:
        print("Something Wrong In Your Email or Password, Try Again!\n")
        login_valid = False
#-----------------------------------------------------------------------

def phoneValidation(phone):
    global phone_valid
    if not(phone.isdigit()):
        print("Mobile only contains numbers!\n")
        phone_valid = False
    elif len(phone) < 11 and len(phone) > 11:
        print("Mobile must contain only 11 digits!\n")
        phone_valid = False
    elif (phone.startswith("010") or phone.startswith("011") or phone.startswith("012") or phone.startswith("015")) == False:
        print("Mobile must begin with '010' or '011' or '012' or '015'!\n")
        phone_valid = False
    else:
        phone_valid = True
