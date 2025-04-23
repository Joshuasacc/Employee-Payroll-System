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
        PaySlip(name, ID, role, int(work_salary))
    break
