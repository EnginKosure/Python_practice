class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = f'{firstname} {lastname}'
        self.email = '{}.{}@company.com'.format(firstname, lastname).lower()


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
print(emp_1.fullname)  # "John Smith"

print(emp_2.email)  # "mary.sue@company.com"

emp_3.firstname  # "Antony"
