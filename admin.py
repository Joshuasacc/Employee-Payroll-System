import os

def Introduction():
    introduction = """
     █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
    ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
    ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║    ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
    ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║    ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
    ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
    ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝                                                                                   
    """  
    print(introduction)
Introduction()

# Standard Naming Convention
# if the variable holds Function, the first letter must be Capitalized and dont use snake method.(Ex. "MyName" or if one word "Name")
# if the variable holds inside function, use snake method. (Ex. "my_Name" or if one word "name")

def Error(error_Name):
    print("_________________________________________")
    print(f"\n   {error_Name}!! Press Enter to try again")
    error = input("_________________________________________\n")

def PrintError(error_name):
    Error(error_name)
    CLearScreen()
    Introduction()
                                                                                                                                                                                                
def CLearScreen():
    print("\n" * 100)

def IsNumber(str_number):
    numbers = "0123456789"
    for char in str_number:
        found = False
        for num in numbers:
            if char == num:
                found = True
                break
        if not found:
            return False
    return True

def AddEmployee():
    while True:
        name = input("Enter your Name: ")
        position = input("Enter your Position: ")

        ID = input("Enter your ID (6 digits only): ") 
        if len(ID) != 6:
            PrintError("ID must be a 6-digit number")
            continue
        
        work_Salary = input("Enter your Work Salary: ") 
        if not IsNumber(work_Salary): 
            PrintError("Work Salary must be a number")
            continue

        salary_Rate = input("Enter your Salary Rate: ") 
        if not IsNumber(salary_Rate):
            PrintError("Salary Rate must be a number")
            continue

        # Convert to integers after validation
        work_Salary = int(work_Salary)
        salary_Rate = int(salary_Rate)
        ID = int(ID)
        file = open("Data.txt", "a")
        if file:
            file.write(f"{ID},{name},{position},{work_Salary},{salary_Rate}\n")
            file.close()
            return True
        return False
        break

def RemoveEmployee():
    pass

def RetrieveEmployee():
    pass

def EditEmployee():
    pass

def AdminChoice():
    choice = input("""
1) Add Employee
2) Remove Employee
3) Retrieve Employee Data
4) Edit Employee Data

Enter: """)
    if choice:
        if choice == "1":
            AddEmployee()
        elif choice == "2":
            RemoveEmployee()
        elif choice == "3":
            RetrieveEmployee()
        elif choice == "4":
            EditEmployee()
        else:
            PrintError("Only digits 1-4 only")
            AdminChoice()
    else:
        PrintError("Wrong input!! Please Try Again")
        AdminChoice()
        
AdminChoice()