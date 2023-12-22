employee_list=[]

def add_employee():
    name=input("Enter Name : ")
    age=int(input("Enter Age : "))
    position=input("Enter Job Position : ")
    salary=int(input("Enter Salary : "))
    
    employee={"Name": name, "Age": age, "Position" : position, "Salary" :salary}
    employee_list.append(employee)
    print("Employee added successfully")
    
def view_employee():
    for employee in employee_list:
        print(f"Name : {employee['Name']}, Age : {employee['Age']}, Position : {employee['Position']}, Salary : {employee['Salary']}")
    
def search_employee():
    search_name=input("Enter the name you want to search for : ")
    for employee in employee_list:
        if employee["Name"]==search_name:
          print(f"Employee Found \n Name : {employee['Name']}, Age : {employee['Age']}, Position : {employee['Position']}, Salary : {employee['Salary']}")
           
def remove_employee():
    remove_name=input("Enter the name that you want to delete : ")
    for employee in employee_list:
        if employee["Name"]==remove_name:
           print("Successfully Removed") 
           
def main():
    while True:
        print("****EMPLOYEE MANAGEMENT SYSTEM****")
        print("1.Add an employee")
        print("2.Display employees")
        print("3.Search employee")
        print("4.Remove eployee")
        print("5.Exit")
        
        choice=input("Enter your choice : ")
        
        if choice=="1":
            add_employee()
            
        elif choice=="2":
            view_employee()
            
        elif choice=="3":
            search_employee()
            
        elif choice=="4":
            remove_employee()
            
        elif choice=="5":
            print("THANK YOU")
            
        else:
            print("invalid choice. Please try again.")
            break

if __name__=="__main__":
    main()