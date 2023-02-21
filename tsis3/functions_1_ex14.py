import math
import random
from functions_1 import grams_to_ounces,centi_to_farenheit,solve,filter_primes
from functions_1 import permute,reverse,sol,has_33,sphere_vol,unique
from functions_1 import is_palindrom,histogram,ex14,spy

grams_to_ounces(100)
centi_to_farenheit(100)
solve(35,94)
n = [1,2,3,4,5,6,7,8,9,10,11]
n1 = filter_primes(n)
print(*n1)
string = "KBTU"
permute(list(string),0,len(string))
words = "TSIS3 PP2"
print(''.join(sol(list(words),len(words))))
print(has_33([3,3]))
print(has_33([1,2,3]))
print(spy([0,0,7]))
print(spy([0,0,0]))
print(sphere_vol(3))
print(unique([1,1,1,0]))
print(is_palindrom("qwerty"))
print(is_palindrom("qweewq"))
histogram([1,3,5,])
ex14()

