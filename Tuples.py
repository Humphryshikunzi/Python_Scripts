names = 'Collins','Bram'
print(type(names))
print(names)
print(names[0])

tuple1 = (4,1,2)
tuple2 = (1,2,9)
print(tuple1 < tuple2)
#tuple assignments
names2 = ["Clevarance",'Faith']
a, b = names2
def fib( a ):
    count = 0;
    start1 = 1;
    start2 = 1;
    while count < a:
        start1 = start2;
        ans = start1 + start2;
        start2 = ans;

        print( ans )
        count += 1
fib(7)