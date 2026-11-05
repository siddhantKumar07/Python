num = int(input("enter a number"))

try:
    print(10/num)
except Exception as e:
    print("error = ", e)
finally:
    print("this is finally block")