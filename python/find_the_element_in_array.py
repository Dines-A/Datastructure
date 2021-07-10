import array 
arr=array.array('i',[])
s=int(input("enter the array size : "))
for i in range(s):
    v=int(input("enter the value : "))
    arr.append(v)
v1=int(input("enter the value to find the value : "))
if arr[i]==v1:
    print("the value is here that u have enterd:)")
        #how would you find the value of index that you have entered
        #do this program using function
else:
        print("oops")