menor = int(input())
maior = int(input())
s = int(input())
soma = 0
resul = -1

for i in range(menor, maior+1):
    num = str(i)
    soma = 0
    for j in range(len(num)):
        soma += int(num[j])
    if soma == s:
        resul = i

print(resul)