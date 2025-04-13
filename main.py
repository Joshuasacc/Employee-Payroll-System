import os

def Introduction():
    introduction = """
    ███████╗███╗   ███╗██████╗ ██╗      ██████╗ ██╗   ██╗███████╗███████╗    ██████╗  █████╗ ██╗   ██╗██████╗  ██████╗ ██╗     ██╗     
    ██╔════╝████╗ ████║██╔══██╗██║     ██╔═══██╗╚██╗ ██╔╝██╔════╝██╔════╝    ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗██║     ██║     
    █████╗  ██╔████╔██║██████╔╝██║     ██║   ██║ ╚████╔╝ █████╗  █████╗      ██████╔╝███████║ ╚████╔╝ ██████╔╝██║   ██║██║     ██║     
    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██║   ██║  ╚██╔╝  ██╔══╝  ██╔══╝      ██╔═══╝ ██╔══██║  ╚██╔╝  ██╔══██╗██║   ██║██║     ██║     
    ███████╗██║ ╚═╝ ██║██║     ███████╗╚██████╔╝   ██║   ███████╗███████╗    ██║     ██║  ██║   ██║   ██║  ██║╚██████╔╝███████╗███████╗
    ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
                                                                                                                                    
    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗                                                                              
    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║                                                                              
    ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║                                                                              
    ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║                                                                              
    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║                                                                              
    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝                 
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

def PrintError(error_name):
    CLearScreen()
    Introduction()
    Main()

def Main():
    name = input("Enter your Name: ")
    position = input("Enter your Position: ")

    work_Salary = input("Enter your Work Salary: ") 
    if not IsNumber(work_Salary): # checks if only contains integer
        PrintError("Number ERROR")
        return False

    salary_Rate = input("Enter your Salary Rate: ") # checks if only contains integer
    if not IsNumber(salary_Rate):
        PrintError("Number ERROR")
        return False

    ID = input("Enter your ID (6 digits only): ") # checks if only contains integer
    if not IsNumber(ID):
        PrintError("Number ERROR")
        return False

    work_Salary = int(work_Salary)
    salary_Rate = int(salary_Rate)
    ID = int(ID)
    print("SUCCESS")
    return True
#Program Starts
Main()