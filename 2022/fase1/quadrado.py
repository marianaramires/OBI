n = int(input())
l = 0
c = 0
cont = 0
zero = 0
soma = 0

for i in range(n):
    linha = input().split()
    if '0' in linha:
        for j in range(n):
            zero += int(linha[j])
            if linha[j] == '0':
                c = j + 1
        l = i + 1
    elif '0' not in linha and cont == 0:
        for j in range(n):
            soma += int(linha[j])
            cont += 1

diff = soma - zero

print(diff)
print(l)
print(c)
