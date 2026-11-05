def hello():
    print("hello world")

hello()

def add(a,b):
    return a+b
sum =add(5 ,4 )
print(sum)


#args 

def add2(*args):
    sum=0
    for i in args:
      sum+=i
    return sum
print(add2(4,5,6,2,7,8,8,6,1,2,5,4,6))

#kwargs

def keyval(**kwargs):
    print(kwargs["lastName"])

keyval(name="siddhant",lastName="kumar")

a = lambda x,y : x+y
print(a(5,6))

b = lambda : print("hello world")

b()