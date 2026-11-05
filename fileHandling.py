files = open("demo.txt",'w')

files.write("Hello World\n")
files.write("This is a demo file\n")
read = open("demo.txt",'r')
print(read.read())