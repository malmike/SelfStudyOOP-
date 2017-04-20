from employer import Employer
from employee import Employee

def main():
    employer = Employer('Male Michael', 25, 'male', 'Manager')
    #add subordinates
    employee = Employee('Bruce Lee', 22, 'male', 'Cleaner');
    employer.hire(employee)
    employer.hire(Employee('Bruce Lee', 22, 'male', 'Cleaner'))
    employer.hire(Employee('Bruce Tony', 18, 'male', 'Technician'))
    employer.hire(Employee('Bruce Cree', 19, 'male', 'Security guard'))
    employer.hire(Employee('Bruce Lorry', 20, 'male', 'Cleaner'))
    print ("Details of employer:" )
    print ("Name: "+ employer.name)
    print ("Age: "+ str(employer.age))
    print ("Gender: "+ employer.gender)
    print ("Title: "+ employer.title)
    print ("Number of subordinates:"+ str(len(employer.subordinates)))
    print ("Show polymorphism:")
    print ("Message for employee:"+employee.message())
    print ("Message for employer:"+employer.message())

if __name__ == "__main__":
    main()

