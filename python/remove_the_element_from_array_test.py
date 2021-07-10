import array 
arr=array.array('i',[])
s=int(input("enter the array size : "))
for i in range(s):
    v=int(input("enter the value : "))
    arr.append(v)
print(f"befor remove the element {arr}")
I=int(input("enter the  value to remove the value : "))
if arr[i]==I:
    arr.remove(arr[i])
    #arr[i]=arr[i+1]
    print(f"after remove the element {arr}")
    #print(f"index : {index(v)}")
    #print("removerd array : ",arr[i])
    #this is not working
else:
    print("oops:)")