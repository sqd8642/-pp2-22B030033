import re

#ex1
def text_match(text):
        pattern = '^a(b*)$'
        if re.search(pattern, text):
                return True
        else:
                return False
    
print(text_match("ab"))
print(text_match("aaa"))

#ex2

string = input("Ex2: ")
pattern = re.compile('ab{2,3}?')
flag = pattern.search(str(string))
if flag:
    print("Match!")
else:
    print('No match')


#ex3

string = input("Ex3: ")
pattern = re.compile('[a-z]+_[a-z]+')
flag = pattern.search(string)
if flag:
    print("Match!")
else:
    print('No match')


#ex4

string = input("Ex4: ")
pattern = re.compile('[A-Z]+[a-z]+')
flag = pattern.search(string)
if flag:
    print("Match!")
else:
    print('No match')

#ex5

string = input("Ex5: ")
p = re.compile('a.*?b$')
flag = pattern.search(string)
if flag:
    print("Match!")
else:
    print('No match')

#ex6

string = input("Ex6: ")
m = re.sub('\s', ':', string)
m1 = re.sub(',', ':', m)
m2 = re.sub("\.", ':', m1)
print(m2)

#ex7

string = input("Ex7: ")
m = string.split('_')
res = m[0] + ''.join(i.title() for i in m[1:])
print(str(res))

#ex8

string= input("Ex8: ")
str1 = re.sub( r"([A-Z])", r" \1", string).split()
for i in str1:
     print(i,end=' ')
else:
     print()

#ex9

string = input("Ex9: ")
str1 = re.sub(r"(\w)([A-Z])", r"\1 \2", string)
print(str1)

#ex10

string = input("Ex10: ")
str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
str2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()