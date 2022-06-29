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
