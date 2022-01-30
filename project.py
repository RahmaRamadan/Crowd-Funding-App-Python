import time
# global variables
login_valid = False
projectData_valid = False
search_input_project = False

#-------------------------Project Functions-----------------------------
def viewAllProjects():
    with open("projectData", "r") as projects:
        lines = projects.readlines()
        print("\nTitle , FirstName , LastName , Budget , Start Date , End Date")
        print("================================================================")
        for field in lines[1:]:
            print(field.split()[1:])
            print("\n")
#-----------------------------------------------------------------------

def searchProjectByName(name):
    found = False
    with open("projectData", "r") as projects:
        lines = projects.readlines()
        print("\nTitle , FirstName , LastName , Budget , Start Date , End Date")
        print("================================================================")
        for field in lines[1:]:
            if name == field.split()[1]:
                print(field[0:])
                found = True
        if found == False:
            print("Didn't find any projects with this name!\n")
#-----------------------------------------------------------------------

def searchProjectByStartDate(start_date):
    found = False
    with open("projectData", "r") as projects:
        lines = projects.readlines()
        print("\nTitle , FirstName , LastName , Budget , Start Date , End Date")
        print("================================================================")
        for field in lines[1:]:
            if start_date == field.split()[5]:
                print(field[0:])
                found = True
        if found == False:
            print("Didn't find any projects with this start date!\n")
#-----------------------------------------------------------------------

def deleteProject(user_email):
    found = False
    del_lines = []
    with open("projectData", "r") as projects:
        lines = projects.readlines()
        for i, field in enumerate(lines):
            if user_email == field.split()[0]:
                # del lines[i]
                del_lines.append(i)
                found = True
        for i in sorted(del_lines, reverse=True):
            del lines[i]
    if found == False:
        print("Didn't find any projects created with this user email!\n")
    else:
        with open("projectData", "w+") as newProjects:
            for line in lines:
                newProjects.write(line)

        print("Projects Deleted Successfully :D\n")
#-----------------------------------------------------------------------

def createNewProject(login_email_input):
    global login_valid, projectData_valid
    title = input("Enter your project title: ")
    details = input("Enter your project details: ")
    total_valid = False
    while total_valid == False:
        total_budget = input(
            "Enter your total budget: ")
        if total_budget.isdigit():
            total_valid = True
        else:
            print("Total budget must be integer!\n")
            total_valid = False
    print(
        "Enter Project Start Date and End Date in Day/Month/Year Format\n")
    slash = "/"
    projectData_valid = False
    while projectData_valid == False:
        start_date = input(
            "Enter start date of the project: ")
        end_date = input(
            "Enter end date of the project: ")
        if (start_date.count(slash) < 2) or (end_date.count(slash) < 2) or (start_date.count(slash) > 2) or (end_date.count(slash) > 2):
            print(
                "Invalid Start Date or End Date Format!\n")
            projectData_valid = False
        else:
            projectDateValidation(start_date, end_date)
    if (total_valid and projectData_valid and login_valid == True):
        with open('projectData', 'a') as projectFile:
            input_project_data = [login_email_input, " ", title,
                                  " ", details, " ", total_budget, " ", start_date, " ", end_date, "\n"]
            projectFile.writelines(input_project_data)
#-----------------------------------------------------------------------

def searchForProject():
    global search_input_project
    search_input_project = False
    while search_input_project == False:
        search_input_str = input(
            "1- Search Project By Name\n2- Search Project By Start Date\nEnter Your choice: ")
        search_input = int(search_input_str)
        if search_input == 1:
            search_input_project = True
            pname = input("Enter Project Name: ")
            searchProjectByName(pname)
        elif search_input == 2:
            search_input_project = True
            pstart_date = input(
                "Enter Project Start Date: ")
            searchProjectByStartDate(pstart_date)
        elif search_input_project != True:
            print(
                "\nInvalid Choice, Please Enter 1 or 2\n")
#-----------------------------------------------------------------------

def projectDateValidation(startDateStr, endDateStr):
    global projectData_valid
    startDate = time.mktime(time.strptime(startDateStr, "%d/%m/%Y"))
    endDate = time.mktime(time.strptime(endDateStr, "%d/%m/%Y"))
    if startDate > endDate:
        print("Start Date Must be less than end date!\n")
        projectData_valid = False
    else:
        print("Valid date format :D\n")
        projectData_valid = True
