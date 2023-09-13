file=open("data.txt", "r");
print(file.read());

file1=open("abc.txt","w");
file1.write("something");
file1=open("abc.txt","r");
print(file1.read());