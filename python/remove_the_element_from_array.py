import array 
arr=array.array('i',[])
s=int(input("enter the array size : "))
for i in range(s):
    v=int(input("enter the value : "))
    arr.append(v)
print(f"befor remove the element {arr}")
v1=int(input("enter the value to remove the value : "))
if arr[i]==v1:
    arr.remove(arr[i])
    print(f"after remove the element {arr}")
else:
    print("oops:)")