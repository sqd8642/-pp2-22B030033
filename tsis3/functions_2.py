movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def fun(movie):
    if(movie["imdb"]>5.5):
        return True
    
    return False

def fun_1():
    sublist =[]
    for i in range(0,len(movies)):
        if(movies[i]["imdb"]>5.5):
            sublist.append(movies[i])
    return sublist

def fun_2(category):
    sublist =[]
    for i in movies:
        if(i["category"]==category):
            sublist.append(i)
    return sublist

def fun_3():
    s = 0
    for i in movies:
        s = s +i["imdb"]
    return s/len(movies)

def fun_4(category):
    sublist = fun_2(movies,category)
    return fun_2(sublist)
        
print(fun(movies[1]))
print()
print(*fun_1(), sep = "\n")
print()
print(*fun_2("Romance"),sep = "\n")
print()
print(fun_3())
print()
print(*fun_2("Romance"),sep = "\n")
