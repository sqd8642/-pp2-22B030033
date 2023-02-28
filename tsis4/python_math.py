import math

#ex1
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

degrees = input("Input degrees: ")
radians = math.radians(float(degrees))
print("Radians: "+toFixed(radians,6))

#ex2

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
Area_tr = 0.5*(a+b)*h
print("Area is: " + str(Area_tr))

#ex3

n = int(input("Input number of sides: "))
side = int(input("Input the legth of a side: "))
p = n*side
a_ = side/(2*math.tan(math.radians(180/n)))
Area_p = p*a_/2
print("Area of polygon is: "+str(Area_p))


#ex4

base = float(input("Length base: "))
height_p = float(input("Height if parallelogram: "))
Area_par = base*height_p
print("Area is: "+str(Area_par))