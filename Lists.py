numbers = [45,10,89,25,63,]
for index in range(len(numbers)):
    numbers[index] = numbers[index]+22
    print(numbers[index])

other_numbers = [89,855,46,72,1,6]
numbers.append(48)
for number in numbers:
    print(number)



print('You see, 48 has been added')
print(numbers+other_numbers)
print(numbers*2)
print(other_numbers.sort())
print(other_numbers.pop(1))
print(other_numbers)

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print(T[0])

print(T[1][2])

print(type(T))

#Lets use Python for loops to write out all the values
for i in T:
    for j in i:
        print(j, end=" ")
    print()
