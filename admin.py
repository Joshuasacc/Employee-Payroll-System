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

def IsNumber(str_Number):
    array_Number = [0,1,2,3,4,5,6,7,8,9]
    for i in range(0, len(str_Number)):
        temp = False
        for k in range(0, len(array_Number)):
            if str_Number[i] == str(array_Number[k]):
                temp = True
                break
        if temp == False: return False
    return True

def AddEmployee():
    def GrossSalary(work_Salary, salary_Rate):
        return work_Salary * salary_Rate

    def Main():
        name = input("Enter your Name: ")
        position = input("Enter your Position: ")

        ID = input("Enter your ID (6 digits only): ") 
        if not IsNumber(ID):
            PrintError("Number ERROR")
            Main()
            return False
        
        work_Salary = input("Enter your Work Salary: ") 
        if not IsNumber(work_Salary): 
            PrintError("Number ERROR")
            Main()
            return False

        salary_Rate = input("Enter your Salary Rate: ") 
        if not IsNumber(salary_Rate):
            PrintError("Number ERROR")
            Main()
            return False

        work_Salary = int(work_Salary)
        salary_Rate = int(salary_Rate)
        ID = int(ID)
        
        return True
    Main()

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
    if IsNumber(choice):
        choice = int(choice)
        if choice == 1:
            AddEmployee()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            PrintError("Only digits 1-4 only")
            AdminChoice()
    else:
        PrintError("Wrong input!! Please Try Again")
        AdminChoice()
        
AdminChoice()