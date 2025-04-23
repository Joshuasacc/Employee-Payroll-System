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

def Error(error_name):
    print("_________________________________________")
    print(f"\n   {error_name}!! Press Enter to try again")
    input("_________________________________________\n")

def PrintError(error_name):
    Error(error_name)
    ClearScreen()
    Introduction()

def ClearScreen():
    """Clears the console screen in a cross-platform way"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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

def IsEmpty(input_str):
    if len(input_str) == 0:
        return True
    for char in input_str:
        if char != ' ':
            return False
    return True

class EmployeeSystem:
    def __init__(self):
        self.filename = "Data.txt"
        self.employees = {}
        self.LoadEmployees()
        
    def LoadEmployees(self):
        if os.path.exists(self.filename):
            file = open(self.filename, "r")
            current_id = None
            current_employee = {}
            for line in file:
                if line.startswith("ID: "):
                    if current_id is not None:
                        self.employees[current_id] = current_employee
                    current_id = int(line[4:].strip())
                    current_employee = {}
                elif line.startswith("Name: "):
                    current_employee['name'] = line[6:].strip()
                elif line.startswith("Position: "):
                    current_employee['position'] = line[10:].strip()
                elif line.startswith("Work Salary: "):
                    current_employee['work_salary'] = int(line[13:].strip())
                elif line.startswith("Per Rate: "):
                    current_employee['salary_rate'] = int(line[10:].strip())
            if current_id is not None:
                self.employees[current_id] = current_employee
            file.close()
        else:
            open(self.filename, "w").close()
    
    def SaveEmployees(self):
        file = open(self.filename, "w")
        for emp_id, employee in self.employees.items():
            file.write("ID: " + str(emp_id) + "\n")
            file.write("Name: " + employee['name'] + "\n")
            file.write("Position: " + employee['position'] + "\n")
            file.write("Work Salary: " + str(employee['work_salary']) + "\n")
            file.write("Per Rate: " + str(employee['salary_rate']) + "\n\n")
        file.close()

    def AddEmployee(self):
        while True:
            name = input("Enter your Name: ")
            if IsEmpty(name):
                PrintError("Name cannot be empty")
                continue
                
            position = input("Enter your Position: ")
            if IsEmpty(position):
                PrintError("Position cannot be empty")
                continue

            ID = input("Enter your ID (6 digits only): ") 
            if not (IsNumber(ID) and len(ID) == 6):
                PrintError("ID must be 6 digits")
                continue
            
            if int(ID) in self.employees:
                PrintError("Employee ID already exists")
                continue

            work_salary = input("Enter your Work Salary: ") 
            if not IsNumber(work_salary): 
                PrintError("Work Salary must be a number")
                continue

            salary_rate = input("Enter your Per Rate: ") 
            if not IsNumber(salary_rate):
                PrintError("Per Rate must be a number")
                continue

            self.employees[int(ID)] = {
                'name': name,
                'position': position,
                'work_salary': int(work_salary),
                'salary_rate': int(salary_rate)
            }
            self.SaveEmployees()
            print("\nEmployee " + name + " added successfully!")
            break

    def RemoveEmployee(self):
        while True:
            ID = input("Enter the Employee ID to remove: ")
            if not IsNumber(ID):
                PrintError("ID must be a number")
                continue
                
            ID = int(ID)
            if ID not in self.employees:
                PrintError("Employee ID not found")
                continue
                
            name = self.employees[ID]['name']
            del self.employees[ID]
            self.SaveEmployees()
            print("\nEmployee " + name + " (ID: " + str(ID) + ") has been removed.")
            break

    def RetrieveEmployee(self):
        while True:
            ID = input("Enter the Employee ID to retrieve: ")
            if not IsNumber(ID):
                PrintError("ID must be a number")
                continue
                
            ID = int(ID)
            if ID not in self.employees:
                PrintError("Employee ID not found")
                continue
                
            employee = self.employees[ID]
            print("\nEmployee Details:")
            print("ID: " + str(ID))
            print("Name: " + employee['name'])
            print("Position: " + employee['position'])
            print("Work Salary: " + str(employee['work_salary']))
            print("Per Rate: " + str(employee['salary_rate']))
            print("Gross Salary: " + str(self.CalculateGrossSalary(ID)))
            break

    def EditEmployee(self):
        while True:
            ID = input("Enter the Employee ID to edit: ")
            if not IsNumber(ID):
                PrintError("ID must be a number")
                continue
                
            ID = int(ID)
            if ID not in self.employees:
                PrintError("Employee ID not found")
                continue
                
            employee = self.employees[ID]
            print("\nCurrent Details:")
            print("1) Name: " + employee['name'])
            print("2) Position: " + employee['position'])
            print("3) Work Salary: " + str(employee['work_salary']))
            print("4) Per Rate: " + str(employee['salary_rate']))
            
            field = input("\nEnter the number of field to edit (1-4) or '0' to cancel: ")
            if field == '0':
                break
                
            if field == '1':
                new_value = input("Enter new Name: ")
                if IsEmpty(new_value):
                    PrintError("Name cannot be empty")
                    continue
                employee['name'] = new_value
            elif field == '2':
                new_value = input("Enter new Position: ")
                if IsEmpty(new_value):
                    PrintError("Position cannot be empty")
                    continue
                employee['position'] = new_value
            elif field == '3':
                new_value = input("Enter new Work Salary: ")
                if not IsNumber(new_value):
                    PrintError("Work Salary must be a number")
                    continue
                employee['work_salary'] = int(new_value)
            elif field == '4':
                new_value = input("Enter new Per Rate: ")
                if not IsNumber(new_value):
                    PrintError("Per Rate must be a number")
                    continue
                employee['salary_rate'] = int(new_value)
            else:
                PrintError("Invalid choice")
                continue
                
            self.SaveEmployees()
            print("\nEmployee details updated successfully!")
            break

    def CalculateGrossSalary(self, employee_id):
        employee = self.employees[employee_id]
        return employee['work_salary'] * employee['salary_rate']

    def AdminChoice(self):
        while True:
            choice = input("""
1) Add Employee
2) Remove Employee
3) Retrieve Employee Data
4) Edit Employee Data
5) Exit

Enter your choice (1-5): """)
            
            if choice == '1':
                self.AddEmployee()
            elif choice == '2':
                self.RemoveEmployee()
            elif choice == '3':
                self.RetrieveEmployee()
            elif choice == '4':
                self.EditEmployee()
            elif choice == '5':
                print("\nExiting the system. Goodbye!")
                break
            else:
                PrintError("Invalid choice. Please enter a number between 1-5")
            
            input("\nPress Enter to continue...")
            ClearScreen()
            Introduction()

# Main program execution
if __name__ == "__main__":
    ClearScreen()
    Introduction()
    system = EmployeeSystem()
    system.AdminChoice()
