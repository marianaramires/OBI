n = int(input())
m = int(input())
total = 0

lista = n,m
 
for i in range(len(lista)):
    if lista[i] <= 17:
        total += 15
    elif lista[i] >= 18 and lista[i] <= 59:
        total += 30
    elif lista[i] >= 60:
        total += 20

print(total)