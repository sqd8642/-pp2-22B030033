import math
import random

#ex1

def grams_to_ounces(num):
    return num/28.3495231
#ex2

def centi_to_farenheit(num):
    return (5 / 9) * (num - 32)

#ex3

def solve(heads,legs):
    i = 0
    j = heads
    k = lambda i,j:4*i+2*j
    while(i<=heads and j>=0):
        if(k(i,j)!=legs):
            i=i+1
            j=j-1
        else:
            print("Solved!")
            print("Rabbits-",i)
            print("Chikens-",j)
            break


#ex4

def filter_primes(nums):
    primes = []
    for i in nums:
        if(i==1):
            continue
        flag = True
        for j in range(2,int(math.sqrt(i)) + 1):
            if(i%j==0):
                flag = False
        if(flag==True):
            primes.append(i)    
    return primes

#ex5

def permute(string,l,r):
    if(l==r):
        print(''.join(string))
    else:
        for i in range(l,r):
            string[l],string[i]=string[i],string[l]
            permute(string,l+1,r)
            string[l],string[i]=string[i],string[l]

#ex6

def reverse(string, l, r):
    while(l!=r):
        string[l],string[r] = string[r],string[l]
        l=l+1
        r=r-1
    return string

def sol(text, n):
    start = 0
    while True:
        try:
            end = text.index(' ',start)
            text = reverse(text, start,end-1)
            start = end+1
        except ValueError:
            text = reverse(text, start,n-1)
            break
    text = reverse(text, 0, n-1)
    return text

#ex7

def has_33(nums):
    for i in range(0,len(nums)-1):
        if(nums[i]==3 and nums[i+1]==3):
           return True
     
    return False


#ex8

def spy(nums):
    for i in range(0,len(nums)-2):
        if(nums[i]==0 and nums[i+1]==0 and nums[i+2]==7):
           return True
     
    return False

#ex9

def sphere_vol(radius):
    return (4*pow(radius,3)*3.14)/3

#ex10

def unique(data):
    new_data = []
    i=0
    while(i<len(data)):
        try:
            new_data.index(data[i],0)
            i=i+1
        except ValueError:
            new_data.append(data[i])
            i=i+1
    return new_data

#ex11

def is_palindrom(word):
    word = str(word.lower())
    l = 0
    word = list(word)
    r = len(word)-1
    while(l<r):
        if(word[l]!=word[r]):
            return False
        else:
            l=l+1
            r=r-1
    return True
#ex12

def histogram(nums):
    for i in range(0,len(nums)):
        for j in range(0,nums[i]):
             print('*', end = ' ')
        print()

#ex13

def ex14():
    print("Hello! What is your name?")
    name = input()
    print("Well, "+name+", I am thinking of a number between 1 and 20.")
    print("Take a Guess")
    gx = -1
    y = random.randint(1,20)
    guesses = 0
    while(int(gx)!=y):
        gx = input()
        if(int(gx)>y):
            print("Your guess is too high.")
        elif(int(gx)<y):
            print("Your guess is too low.")
        guesses = guesses+1
    
    print("Good job " +name+ "! You guessed my number in "+str(guesses)+" guesses!")

