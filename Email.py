file = open('Email.txt')
file_write_to = open('writefile.txt','w')
for line in file:
    print(line.strip())
    file_write_to.write(line)