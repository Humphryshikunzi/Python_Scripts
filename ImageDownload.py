import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    infor = img.read(100000)
    if len(infor) < 1 : 
        break
    size = size + len(infor)
    fhand.write(infor)

print(size, ' characters that have been copied')
fhand.close()

print('Now customized')

img = urllib.request.urlopen('https://menopuseimages.blob.core.windows.net/faces/FacePictures/2fdd2bfd-435d-4e1e-80e9-db4c423c9312.jpg')
fhand = open('2fdd2bfd-435d-4e1e-80e9-db4c423c9312.jpg', 'wb')
size = 0
while True:
    infor = img.read(100000)
    if len(infor) < 1 : 
        break
    size = size + len(infor)
    fhand.write(infor)

print(size, ' characters that have been copied')
fhand.close()