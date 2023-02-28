from datetime import datetime
import datetime
#ex1

cur_date = datetime.date.today()
sub_date = datetime.timedelta(5)
cur_date = cur_date - sub_date
print(cur_date,"\n")
#ex2

cur_date = datetime.date.today()
i = -1
while(i<=1):
    print(cur_date+datetime.timedelta(i))
    i+=1
print()
#ex3
cur_date = datetime.datetime.today()
print(cur_date)
cur_date = cur_date.replace(microsecond = 0)
print(cur_date,'\n')


from datetime import datetime
#ex4
a_str = str(input("First date: "))
b_str = str(input("Second date: "))
a_date = datetime.strptime(a_str, '%Y-%m-%d %H:%M:%S')
b_date = datetime.strptime(b_str, '%Y-%m-%d %H:%M:%S')
diff = a_date -b_date
seconds = diff.days * 24 * 3600 + diff.seconds
print(seconds)