str1 = input("enter your first string")
str2 = input("enter your second string")

common=[]

for ch in str1:
    if ch in str2 and ch not in common :
        common.append(ch)
print("common characters are : ",common)