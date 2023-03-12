#ex1 
import os
path = os.getcwd()
files = os.listdir()
print(files)
print("Directories: ")
for i in files:
    if os.path.isdir(i):
        print(i)

print("Files: ")
for i in files:
    if os.path.isfile(i):
        print(i)

#ex2

path = os.getcwd()
d = os.access(path,os.F_OK)
r = os.access(path,os.R_OK)
w = os.access(path,os.W_OK)
ex = os.access(path,os.X_OK)
print("Exists: "+str(d))
print("Readable: "+str(r))
print("Writable: "+str(w))
print("Executable: "+str(ex))

#ex3

path = os.getcwd()
if(os.path.exists(path)):
    print("Path exists")
    print("Basename: " +str(os.path.basename(path)))
    print("Dirname: "+str(os.path.dirname(path)))
else:
    print("Doesn't exsist")

#ex4

with open(r"C:\Users\User\Desktop\Spring semester\pp2\tsis6\text.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Number of lines"', count + 1)


#ex5

items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open(r"C:\Users\User\Desktop\Spring semester\pp2\tsis6\text.txt",'w')
for item in items:
	file.write(item+"\n")
file.close()

#ex6

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
curr_path = os.getcwd()

path = os.path.join(curr_path, "letters")
if not(os.path.exists(path)):
    os.mkdir(path)
    for letter in alphabet:
        file_name = str(letter+".txt")
        file_path = os.path.join(path, file_name)
        with open(file_path, "w") as f:
            f.write("This text is written with Python.")

#ex7
cur_path = os.getcwd()  
first = r"C:\Users\User\Desktop\Spring semester\pp2\tsis6\text.txt"
second = r"C:\Users\User\Desktop\Spring semester\pp2\tsis6\text_1.txt"
with open(first,'r') as firstfile, open(second,'a') as secondfile:
    for line in firstfile:
             secondfile.write(line)

#ex8

if os.path.exists(r"C:\Users\User\Desktop\Spring semester\pp2\tsis6\text_1.txt"):
  os.remove(r"C:\Users\User\Desktop\Spring semester\pp2\tsis6\text_1.txt")
else:
  print("The file does not exist")