import math

#ex1

class Printer(object):
    def __init__(self):
        self.String = " "

    def getString(self):
        self.String = str(input())

    def printString(self):
        print(self.String.upper())

a = Printer()
a.getString()
a.printString()

#ex2

class Shape():
    def __init__(self):
        pass

    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, len = 0):
        Shape.__init__(self)
        self.len = len

    def area(self):
        print(self.len*self.len)

s = Shape()
s.area()
y = Square(4)
y.area()

#ex3

class Rectangle(Shape):
    def __init__(self, width=0, length=0):
        Shape.__init__(self)
        self.width = width
        self.length = length

    def area(self):
        print(self.width*self.length)

z = Rectangle(4,5)
z.area()

#ex4

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def show(self):
        print(self.x,self.y)

    def move(self):
        x1 = int(input())
        y1 = int(input())
        self.x = x1
        self.y = y1

    def dist(self):
        x1 = int(input())
        y1 = int(input())
        z = (x1+self.x)*(x1+self.x)+(y1+self.y)*(y1+self.y)
        print(math.sqrt(z))
    
p = Point(1,1)
p.show()
p.move()
p.show()
p.dist()

#ex5 

class BankAcc():
    def __init__(self,owner = "Jhon Doe",balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        print(self.balance)
    def withdrawal(self):
        amount = int(input())
        if(self.balance-amount>=0):
            self.balance = self.balance-amount
            print("Succes!")
            print("Now balance is", self.balance)
        else:
            print("Error!")
            print("Insuficient funds, your balance is", self.balance)

pk = BankAcc("Pavel Kan", 100)
pk.deposit()
pk.withdrawal()
pk.withdrawal()

#ex6
f = lambda arg : arg+1
def fun(num):
    i=2
    if(num <=1):
        return False
    while (i<int(math.sqrt(num)) + 1):
        if (num%i==0):
           return False
        else:
            i = int(f(i))
    return True
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
prime_nums = filter(fun,numbers)
print(*prime_nums)
            








        