#Inheritance
class Calculator:
    def __int__ (self, name):
        print(f'Welcome {name}')

     def sum (self,x,y):
         print(x+y)

     def mul(self,x,y):
         print(x*y)



class SciCalculator(Calculator):
    def power(self,x,y):
        print (x**y)

s1=  SciCalculator('mahmoud')
s1.sum(2,3)
s1.mul(4,5)
s1.power(2,5)


#Polumorphism

class A :
    def do(self):
        print('in A')

class B (A):
    pass

class C :
    def do(self):
        print('in C')

class D(B,C) :
    pass


p1=D()
print(D.mro())
p1.do()


#Encapsulation
class Student:
    def __init__(self):
        self.marks=[]

    def print_marks(self):
        print(self.marks)
        
    def add_mark(self,mark):
        self.marks.append(mark)

s=Student()
s.add_mark(20)
s.add_mark(30)
s.add_mark(40)
s.add_mark(50)
s.add_mark(60)
s.add_mark(70)
s.add_mark(80)
s.add_mark(90)
s.add_mark(220)
s.add_mark(230)
s.add_mark(240)
s.add_mark(250)
s.add_mark(260)
s.print_marks()

d=Student()
d.add_mark(210)
d.add_mark(202)
d.add_mark(203)
d.add_mark(204)
d.add_mark(204)
d.add_mark(205)
d.add_mark(206)
d.add_mark(208)
d.add_mark(209)
d.add_mark(207)
d.add_mark(207)
d.add_mark(208)
d.add_mark(209)

d.print_marks()
