import os

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

def Error():
    print("_________________________________________")
    print("\n   ERROR!! Press Enter to try again")
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

def Main():
    name = input("Enter your Name: ")
    position = input("Enter your Position: ")
    work_Salary = input("Enter your Work Salary: ")
    salary_Rate = input("Enter your Salary Rate: ")
    ID = input("Enter your ID: ")
    temp = str(work_Salary + salary_Rate + ID)

    if not IsNumber(temp):
        Error()
        CLearScreen()
        print(introduction)
        Main()
Main()