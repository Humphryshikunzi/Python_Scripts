def square_sum(numbers):
    sum = 0
    for value in numbers:
        sum = sum + value*value;
    return sum;
print (square_sum([1,2,4]));
