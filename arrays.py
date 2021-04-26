# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
arr1 = [20,30,40]
print(arr1)
print(type(arr1))

from array import *
arr2 = array('i', [20,30,40])
print(type(arr2))
print(arr2[2])

#insert element into array
arr2.insert(3,65)

for i in arr2:
    print(i)

#remove element from array    
arr2.remove(30)
print(arr2)

#update element in an array
arr2[2] = 78
print(arr2)

#search element in array
print(arr2.index(78))
