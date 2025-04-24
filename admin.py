import os
if not os.path.exists("Data.txt"):
    file = open("Data.txt", "w")
    file.close()

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

def PaySlip(name, ID, role, work_salary, salary_rate):
    standard_hours = 160 # Standard rate
    salary_rate = work_salary // standard_hours  # Integer division
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
    name = input("Enter Employee's Name: ")
    position = input("Enter your Position: ")

    while True:
        ID = input("Enter your ID (6 digits only): ") 
        if len(ID) == 6 and IsNumber(ID):
            file = open("Data.txt", "r")
            is_registered = False
            for line in file:
                temp = line.strip().split(",")
                if temp[0] == ID:
                    is_registered = True
                    break
            file.close()
            if not is_registered:
                break
            else:
                Error("ID already exists. Please enter a unique ID.")
        else:
            Error("ID must be 6 digits and numeric.")

    file = open("Data.txt", "r")
    for line in file:
        temp = line.strip().split(",")
        if(temp[0] == ID):
            Error("ID Already existed")
            AddEmployee()
            continue

    while True:
        work_Salary = input("Enter your Work Salary: ") 
        if not IsNumber(work_Salary): 
            Error("Work Salary must be a number")
            continue

        salary_rate = input("Enter Employee Salary Rate: ") 
        if not IsNumber(salary_rate): 
            Error("Salary Rate must be a number")
            continue
        
        if salary_rate == "" or work_Salary == "":
            salary_rate = 0
            work_Salary = 0
        salary_rate = int(salary_rate)
        work_Salary = int(work_Salary)
        if work_Salary <= salary_rate:
            Error("Wrong salary distribution")
            continue
        else: break
    # Convert to integers after validation
    ID = int(ID)
    file = open("Data.txt", "a")
    if file:
        file.write(f"{ID},{name},{position},{work_Salary},{salary_rate}\n")
        file.close()
        return True
    return False

def RetrieveEmployee():
    employee_ID = input("Enter Employee's ID (6-digits only): ")
    if len(employee_ID) != 6:
        Error("Error!! It might be not enough length or employee does not exists")
        RetrieveEmployee()

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
        Error("69!! Employee Not Found")
        RetrieveEmployee()
        
    else:
        PaySlip(name,ID,role, int(work_salary), int(salary_rate))

def RemoveEmployee(): # Re-structured this
    remove_ID = input("Enter the Employee ID to remove: ")

    file = open("Data.txt", "r")
    new_lines = []
    found = False

    for line in file:
        data = line.strip().split(",")
        if data[0] != remove_ID:
            new_lines.append(line)
        else:
            found = True

    file.close()

    file = open("Data.txt", "w")
    for line in new_lines:
        file.write(line)
    file.close()

    if found:
        print("\n✅ Employee successfully removed!")
    else:
        Error("Employee ID not found")
        RemoveEmployee()


def EditEmployee():
    while True:
        input_ID = input("Enter Employee ID (6 digits): ")

        file = open("Data.txt", "r")
        lines = file.readlines()
        file.close()

        new_lines = []
        does_exist = False

        for line in lines:
            temp = line.strip().split(",")
            if temp[0] == input_ID:
                print("Current data:", temp)

                new_name = input("Enter new name: ").strip()
                if new_name == "":
                    new_name = temp[1]

                new_position = input("Enter new position: ").strip()
                if new_position == "":
                    new_position = temp[2]

                new_salary = input("Enter new salary: ").strip()
                if new_salary == "":
                    new_salary = temp[3]

                new_salary_rate = input("Enter new salary rate: ").strip()
                if new_salary_rate == "":
                    new_salary_rate = temp[4]

                edited_line = f"{temp[0]},{new_name},{new_position},{new_salary},{new_salary_rate}\n"
                new_lines.append(edited_line)
                does_exist = True
            else:
                new_lines.append(line)  # Keep unchanged lines

    if does_exist:
        file = open("Data.txt", "w")
        for line in new_lines:
            file.write(line)
        file.close()
        print("✅ Data successfully updated!")
    else:
        Error("Employee Not Found")



def ShowEmployeeData():
    file = open("Data.txt", "r")
    print("\nEmployees Data:")
    print("________________________\n")
    count = 0

    is_empty = ""
    for i in file:
        count += 1
        temp = i.strip().split(",")
        ID = temp[0]
        name = temp[1]
        is_empty += str(temp)
        print(f"{count}) Name: {name} | ID: {ID}")
    file.close()

    # Check if data is empty 
    if is_empty == "":
        print("Employee Not Found")
    print("\n________________________")
def AdminChoice():
    choice = input("""
1) Add Employee
2) Remove Employee
3) Retrieve Employee Data
4) Edit Employee Data
5) Show all Employee
6) Exit
                   
Enter: """)
    
    if choice == "1":
        AddEmployee()
        again = input("\nContinue? (y/n): ")
        if again.upper() == "Y":
            AdminChoice()
    elif choice == "2":
        RemoveEmployee()
        again = input("\nContinue? (y/n): ")
        if again.upper() == "Y":
            AdminChoice()
    elif choice == "3":
        RetrieveEmployee()
        again = input("\nContinue? (y/n): ")
        if again.upper() == "Y":
            AdminChoice()
    elif choice == "4":
        EditEmployee()
        again = input("\nContinue? (y/n): ")
        if again.upper() == "Y":
            AdminChoice()
    elif choice == "5":
        ShowEmployeeData()
        again = input("\nContinue? (y/n): ")
        if again.upper() == "Y":
            AdminChoice()
    elif choice == "6":
         while True:    
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == "y":
                print("Exiting program. Goodbye!")
                break
            elif confirm.lower() == "n":
                Introduction()
                AdminChoice()
                continue
    else:
        PrintError("Only digits 1-6 only")
        AdminChoice()
    
AdminChoice()
