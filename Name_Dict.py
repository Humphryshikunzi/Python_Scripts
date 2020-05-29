name = 'HumphryShikunzi'.lower()

occurence = dict()

for c in name:
    if c not in occurence:
        occurence[c] = 1
    else:
        occurence[c] += 1


print(occurence)

