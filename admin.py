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

def PaySlip(name, ID, role, salary_rate, work_salary):
    gross_salary = work_salary * salary_rate
    tax_deduction = gross_salary * 4 / 100
    net_salary = gross_salary - tax_deduction

    table = f""" 
                                    ============================================================
                                                        EMPLOYEE PAYSLIP
                                    ============================================================
                                    Employee ID      : {ID}
                                    Name             : {name}
                                    Position         : {role}

                                    --------------------- SALARY DETAILS -----------------------
                                    Work Salary       : {work_salary} (hours)
                                    Rate per Hour     : ₱{salary_rate}
                                    Gross Salary      : ₱{gross_salary}
                                    Tax Deduction (4%): ₱{tax_deduction}
                                    ------------------------------------------------------------
                                    NET SALARY        : ₱{net_salary}
                                    ============================================================
                                            THIS IS A SAMPLE PAYSLIP FOR EMPLOYEE
                                    ============================================================
    """
    print(table)

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
    while True:
        employee_ID = input("Enter Employee's ID (6-digits only): ")
        if len(employee_ID) != 6:
            Error("Error!! It might be not enough length or employee does not exists")
            CLearScreen()
            Introduction()
            continue

        # Initialize default state
        found = False
        file = open("Data.txt", "r")
        for line in file:
            info = line.strip().split(",")
            if info[0] == employee_ID:
                ID = info[0]
                name = info[1]
                role = info[2]
                work_salary = info[3]
                salary_rate = info[4]
                found = True
                break
        file.close()

        if not found:
            print("696!! Employee Not Found!")
        else:
            PaySlip(name,ID,role,int(salary_rate), int(work_salary))
        break


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