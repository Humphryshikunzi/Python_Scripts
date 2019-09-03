import  math
import  random


def random_class():
    for i in range(10):
        print(random.random())
    for i in range(5):
        x = random.randint(5, 50)
        print(random.randint(0, 12))
        print(x)
    print('Number from list')
    list = [4, 78, 85, 47, 6]
    print(random.choice(list))

def math_functions():
    print(math)
    print('Pi is', math.pi)
    print('Sine 60 is ', math.sin(60)*-1)
    print('Square of 9 is', math.pow(9,2))
    return 0

def while_loop():
    number = 10
    while number < 15:
        print(number)
        number = number+1

    print('\nLoop 2\n')
    second_number = 12
    while second_number > 1:
        print(second_number)
        second_number = second_number-1

    while True:
        number = input('Number is\n')
        if number=='#':
            continue
        if number == 'Done':
            break
        print(number)

    names = ['Humphry','Shikunzi','Morton','Frank']
    list_numbers=[1,78,52,100]
    print('Length of list is',len(names))
    print('The max value in list is',max(list_numbers))
    print('The min value in list is', min(list_numbers))
    print('The average value in list is',  )
    count = 0
    for name in names:
        count = count+1
        print(count,name)

def strings():
    string = 'Mantasinomics'
    sentance = ' Hey guys, here we go '

    email_outlook = 'humphry97@outlook.com'
    email_gmail = 'humphryshikunzi17@gmail.com'
    print(string[2])
    print(len(string))
    for letter in string:
        print(letter)

    print(string[:7])
    print(sentance.find('guys'))
    print(sentance)
    print(sentance.strip())
    print(string.upper().startswith('M'))
    print(string.capitalize())

    position_outlook_start = email_outlook.find('@')
    position_outlook_end = email_outlook.find('.')
    position_gmail_start = email_gmail.find('@')
    position_gmail_end = email_gmail.find('.')
    print("Email one is " ,email_outlook[position_outlook_start+1:position_outlook_end]);
    print('Email two is ', email_gmail[position_gmail_start+1:position_gmail_end])

    print('My name is %s, I am %d years old and my weight is %g'%('Humphry',22,65.9))



print(strings())
