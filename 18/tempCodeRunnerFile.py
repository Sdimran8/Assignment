class Employee:
    a=11
    def __init__(self):
        self.b = 40

e1 = Employee()       
e1.b = 22
e1.c =90
Employee.a =67

e2 = Employee()
print(e1.a,e1.b,e1.c)
print(e2.a,e2.b)