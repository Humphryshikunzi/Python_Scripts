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

