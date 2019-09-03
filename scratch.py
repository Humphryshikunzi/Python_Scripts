names=['Collins','Bramwel','Clarence','Faith']
students={}
for index, name in enumerate(names):
    students[name] = index + 1
    print(students)
for key in students:
    print(key)

print('Collins' in students)