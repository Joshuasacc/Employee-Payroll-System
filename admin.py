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

def PaySlip(name, ID, role, work_salary):
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
    while True:
        name = input("Enter Employee's Name: ")
        position = input("Enter your Position: ")

        ID = input("Enter your ID (6 digits only): ") 
        file = open("Data.txt", "r")

        is_duplicated = False
        for line in file:
            temp = line.strip().split(",")
            if(temp[0] == ID):
                is_duplicated = True
        file.close()
        if is_duplicated:
            PrintError("ID must be a 6-digit number")
            continue

        if len(ID) != 6:
            PrintError("ID must be a 6-digit number")
            continue
        
        work_Salary = input("Enter your Work Salary: ") 
        if not IsNumber(work_Salary): 
            PrintError("Work Salary must be a number")
            continue

        # Convert to integers after validation
        work_Salary = int(work_Salary)

        ID = int(ID)
        file = open("Data.txt", "a")
        if file:
            file.write(f"{ID},{name},{position},{work_Salary}\n")
            file.close()
            return True
        return False

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
                found = True
                break
        file.close()

        if not found:
            Error("696!! Employee Not Found!")
        else:
            PaySlip(name,ID,role, int(work_salary))
        break


def RemoveEmployee():
    remove_ID = input("Enter the Employee ID to remove: ")

    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    new_lines = []
    found = False

    for line in lines:
        data = line.strip().split(",")
        if data[0] != remove_ID:
            new_lines.append(line)
        else:
            found = True

    file = open("data.txt", "w")
    for line in new_lines:
        file.write(line)
    file.close()

    if found:
        print("\n✅ Employee successfully removed!")
    else:
        PrintError("Employee ID not found")

def EditEmployee():
    input_ID = input("Enter Employee ID (6 digits): ")

    file = open("Data.txt", "r")
    new_lines = []
    does_exists = False

    for line in file:
        temp = line.strip().split(",")
        if temp[0] == input_ID:
            print("Current data:")
            print("______________________\n")
            print(f"Name: {temp[1]}\nRole: {temp[2]}\nWork Salary: {temp[3]}")
            print("______________________")

            new_name = input("Enter new name: ")
            if new_name == "":
                new_name = temp[1]

            new_position = input("Enter new position: ")
            if new_position == "":
                new_position = temp[2]

            new_salary = input("Enter new salary: ")
            if new_salary == "":
                new_salary = temp[3]

            edited_line = f"{temp[0]},{new_name},{new_position},{new_salary}\n"
            new_lines.append(edited_line)
            does_exists = True
        else:
            new_lines.append(line)  # Keep unedited employee data

    file.close()

    if does_exists:
        file = open("Data.txt", "w")
        for line in new_lines:
            file.write(line)
        file.close()
        print("✅ Data successfully updated!")
    else:
        print("❌ Employee Not Found")


def ShowEmployeeData():
    file = open("Data.txt", "r")
    print("\nEmployee's Data:")
    print("________________________\n")
    count = 0
    for i in file:
        count += 1
        temp = i.strip().split(",")
        ID = temp[0]
        name = temp[1]
        print(f"{count}) Name: {name} | ID: {ID}")
    print("\n________________________")
def AdminChoice():
    choice = input("""
1) Add Employee
2) Remove Employee
3) Retrieve Employee Data
4) Edit Employee Data
5) Show all Employee
Enter: """)
    
    if choice == "1":
        AddEmployee()
    elif choice == "2":
        RemoveEmployee()
    elif choice == "3":
        RetrieveEmployee()
    elif choice == "4":
        EditEmployee()
    elif choice == "5":
        ShowEmployeeData()
    else:
        PrintError("Only digits 1-5 only")
        AdminChoice()
    
AdminChoice()