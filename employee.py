import os
if not os.path.exists("Data.txt"):
    file = open("Data.txt", "w")
    file.close()

def Introduction():
    introduction = """
    ███████╗███╗   ███╗██████╗ ██╗      ██████╗ ██╗   ██╗███████╗███████╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
    ██╔════╝████╗ ████║██╔══██╗██║     ██╔═══██╗╚██╗ ██╔╝██╔════╝██╔════╝    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
    █████╗  ██╔████╔██║██████╔╝██║     ██║   ██║ ╚████╔╝ █████╗  █████╗      ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██║   ██║  ╚██╔╝  ██╔══╝  ██╔══╝      ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
    ███████╗██║ ╚═╝ ██║██║     ███████╗╚██████╔╝   ██║   ███████╗███████╗    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
    ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
    """  
    print(introduction)

def CLearScreen():
    print("\n" * 100)

def Error(error_Name):
    print("_________________________________________________________________________________________________")
    print(f"\n   {error_Name}!! Press Enter to try again")
    error = input("_________________________________________________________________________________________________\n")

def PaySlip(name, ID, role, work_salary, salary_rate):
    standard_hours = 160  # Standard monthly working hours
    
    # Gross salary is the work salary provided
    gross_salary = work_salary

    # Dynamic tax based on income
    if gross_salary <= 5000:
        tax_rate = 4  # 4% tax for income up to ₱5000
    elif gross_salary <= 10000:
        tax_rate = 6  # 6% tax for income between ₱5001 and ₱10000
    else:
        tax_rate = 8  # 8% tax for income above ₱10000

    # Tax deduction and net salary calculation
    tax_deduction = gross_salary * tax_rate // 100  # Integer division for tax
    net_salary = gross_salary - tax_deduction

    # Formatting the payslip
    table = f""" 
                                    ============================================================
                                                        EMPLOYEE PAYSLIP
                                    ============================================================
                                    Employee ID      : {ID}
                                    Name             : {name}
                                    Position         : {role}

                                    --------------------- SALARY DETAILS -----------------------
                                    Work Salary       : ₱{work_salary} (monthly)
                                    Rate per Hour     : ₱{salary_rate}
                                    Gross Salary      : ₱{gross_salary}
                                    Tax Rate ({tax_rate}%)     : ₱{tax_deduction}
                                    ------------------------------------------------------------
                                    NET SALARY        : ₱{net_salary}
                                    ============================================================
                                            THANK YOU FOR YOUR HARD WORK THIS MONTH!
                                    ============================================================
    """
    print(table)


# Execution
CLearScreen()
Introduction()

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
        PaySlip(name, ID, role, int(work_salary), int(salary_rate))
    break