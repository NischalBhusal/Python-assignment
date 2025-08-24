class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Salary: {self.salary}")

# Test the Employee class
if __name__ == "__main__":
    employee = Employee("Sita Kumari", 30, "E123", 50000)
    employee.display_employee()
