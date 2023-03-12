#ex1 

n = int(input("Enter number of elements : "))
a = list(map(int,input().split(" ")))
rez = 1
for i in range (0,len(a)):
    rez = rez* a[i]
print("Rezult: "+str(rez))

#ex2

s = input("Enter a string: ")
l = 0
u = 0
for i in range(len(s)):
    if(s[int(i)].islower()):
        l+=1
    elif(s[i].isupper()):
        u+=1
print("Upper: "+str(u))
print("Lower: "+str(l))

#ex3

s = input("Enter a string: ")
s = s.lower()
rs = list(reversed(s))
if(list(rs) == list(s)):
    print("Palindrome")
else:
    print("Not a polindrome")

#ex4

import time
import math
n = input("Input number: ")
dt = input("Input delay time: ")
time.sleep(float(int(dt)/1000))
print("Square root of "+str(n)+" after "+str(dt)+" miliseconds is "+str(math.sqrt(int(n))))

#ex5

n = int(input("Enter number of elements : "))
a = tuple(map(int,input().split(" ")))
if(all(a)):
    print("True")
else:
    print("False")




