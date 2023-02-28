#ex1
def my_gen(N):
    for i in range(N):
        yield i*i

y = my_gen(5)

while(True):
    try:
        print(next(y))
    except StopIteration:
        break
#ex2
def even_gen(N):
    for i in range(1,N):
        if(i%2==0):
            yield i
e = even_gen(10)

while(True):
    try:
        print(next(e), end= ', ')
    except StopIteration:
        break
print()
#ex3
def div_gen(N):
    for i in range(1,N):
        if(i%3==0 and i%4==0):
            yield i

d = div_gen(100)

while(True):
    try:
        print(next(d), end= ' ')
    except StopIteration:
        break
#ex4
def squares(a,b):
    for i in range(a,b+1):
        yield i*i
x = input("a:")
y = input("b:")
s = squares(int(x),int(y))
while(True):
    try:
        print(next(s), end= ' ')
    except StopIteration:
        break
print()
#ex5
def n_gen(N):
    while(N>=0):
        yield N
        N-=1

n = n_gen(100)
while(True):
    try:
        print(next(n), end= ' ')
    except StopIteration:
        break