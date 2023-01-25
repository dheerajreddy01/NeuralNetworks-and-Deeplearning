# 1. Create a class Employee and then do the following
# • Create a data member to count the number of Employees
# • Create a constructor to initialize name, family, salary, department
# • Create a function to average salary
# • Create a Fulltime Employee class and it should inherit the properties of Employee class
# • Create the instances of Fulltime Employee class and Employee class and call their member functions.



#Employee class
class Employee:
    count=0 #contains the count of employees
    employees=[] #contains the list of employees 
    def __init__(self,name,family,salary,department):
        self.name=name
        self.family=family
        self.salary=salary
        self.department=department
        Employee.count=Employee.count+1 # count is incremented each time the employee instance is called 
        Employee.employees.append(self) # here we are adding the employee details to list 
        

        # method to calculate the average_salary of the employees
    def average_salary(self):
        return sum(employee.salary for employee in Employee.employees) / Employee.count
    
#FulltimeEmployee class inheriting the Employee class    
class Fulltime_Employee(Employee):
        pass
    

#creating instances for above classes 
employee1=Employee("harry potter","potter",80000,"IT")
employee2=Employee("ron weasly","weasly",70000,"Marketing")
fulltime_employee1 = Fulltime_Employee("albus james", "james", 70000, "Developer")


#Accessing the classes using instances 
print(employee1.average_salary())
print(employee2.average_salary())
print(fulltime_employee1.average_salary())






