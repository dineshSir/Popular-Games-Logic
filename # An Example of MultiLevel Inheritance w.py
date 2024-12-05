# An Example of MultiLevel Inheritance with @property Decorator.

import datetime


class Person:
    def __init__(self, f_name, l_name, year, month, day, email):
        self.f_name = f_name
        self.l_name = l_name
        self.dob = datetime.date(year, month, day)
        self.email = email

    @property
    def age(self):
        present_date = datetime.datetime.now().date()
        age = (present_date - self.dob).days // 365
        return age
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class Employee(Person):
    def __init__(self, f_name, l_name, year, month, day, email, company, department, position):
        Person.__init__(self, f_name, l_name, year, month, day, email)
        self.company = company
        self.department = department
        self.position = position


class PartTimeEmployee(Employee):
    hourly_pay = 800
    def __init__(self, f_name, l_name, year, month, day, email, company, department, position, working_hours_per_month):
        Employee.__init__(self, f_name, l_name, year, month, day, email, company, department, position)
        self.working_hours_per_month = working_hours_per_month
        self.monthly_salary = working_hours_per_month * self.hourly_pay

    @property
    def yearly_salary(self):
        return self.monthly_salary * 12

    @yearly_salary.setter
    def yearly_salary(self, amount):
        if amount <= 0:
            raise ValueError ("The Amount should be greater than Zero.")
        else:
            self.monthly_salary = amount / 12 
            self.working_hours_per_month = self.monthly_salary/ 800

    @property
    def monthly_tax(self):
        return self.monthly_salary * 0.01


class FullTimeEmployee(Employee):
    def __init__(self, f_name, l_name, year, month, day, email, company, department, position, monthly_salary):
        Employee.__init__(self, f_name, l_name, year, month, day, email, company, department, position)
        self.monthly_salary = monthly_salary

    @property
    def yearly_salary(self):
        return self.monthly_salary * 13

    @yearly_salary.setter
    def yearly_salary(self, amount):
        if amount <= 0:
            raise ValueError ("Yearly salary must be greater than zero.")
        else:
            self.monthly_salary = amount / 13

    @property
    def monthly_tax(self):
        return self.monthly_salary * 0.01
        

aseem = FullTimeEmployee("Aseem", "Ghimire", 1994, 10, 21, "helloaseem007@gmail.com", "Infinite Software Services Nepal", "RND-2", "Software Engineer - I", 55000)
bimal = PartTimeEmployee("Bimal", "Ojha", 1997, 3, 12, "bimal.ojha009@gmail.com", "Universal Engineering College", "Civil", "Lecturer", 140)

print("Details Of Aseem:")
print()
print(aseem.monthly_salary)
print(aseem.yearly_salary)
print(aseem.monthly_tax)
aseem.yearly_salary = 800000
print()
print("Updated:")
print(aseem.monthly_salary)
print(aseem.yearly_salary)
print(aseem.monthly_tax)
print("------------------")

print("Details Of Bimal:")
print()
print(bimal.monthly_salary)
print(bimal.yearly_salary)
print(bimal.monthly_tax)
print(bimal.working_hours_per_month)
print()
print("Updated: ")
print()
bimal.yearly_salary = 1500000
print(bimal.monthly_salary)
print(bimal.yearly_salary)
print(bimal.monthly_tax)
print(bimal.working_hours_per_month)