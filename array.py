from array import *

arr = array("i",[]);

n = int(input("Enter the length of the array: "));
for i in range(n):
	x = int(input("Enter the value: "));
	arr.append(x);


print(arr);


val = int(input("Enter the value for search: "));

k=0;
for j in arr:
	if j==val:
		print("Value found at index: ",k);
		break;

	k+=1;