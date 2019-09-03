names = ['Collins','Bramwel','Clarence','Faith']
students = {}
number = 0;
while number < 4:
    students[names[number]] = number;
    number = number + 1;
    print(students.values())