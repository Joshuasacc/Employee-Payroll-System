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
        print(f"Name: {name}")
        print(f"ID: {ID}")
        print(f"Role: {role}")
        print(f"Work Salary: {work_salary}")
        print(f"Salary Rate: {salary_rate}")
    break
