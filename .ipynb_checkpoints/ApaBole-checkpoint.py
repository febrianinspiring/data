data = []

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        data.append("ApaBole")
    elif i % 3 == 0:
        data.append("Apa")
    elif i % 5 == 0:
        data.append("Bole")
    else :
        data.append(i)
        
for x in data:
    print(x, end=' ')