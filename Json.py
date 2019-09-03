import json
data ='''
[
    {
        "id":"001",
        "x":"2",
        "name":"Chuck"
    },
    {
        "id":"009",
        "x":"7",
        "name":"Bretty"
    }
]'''
infor = json.loads(data)
print('User count:',len(infor))
for item in infor:
    print('Name',item['name'])
print(type(data))

for id in infor:
    print('Id : ', id['x'])