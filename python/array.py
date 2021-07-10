import array 
""" import array """
arr=array.array('i',[])
s=int(input("enter the array size : "))
for i in range(s):
    v=int(input("enter the value : "))
    arr.append(v)
I=int(input("enter the index : "))
v=int(input("update the value : "))
arr[I]=v
print(arr)