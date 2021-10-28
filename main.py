for i in range(3, 6):
    for j in range(4, 10):
         print(i, "*", j, "=", i * j)

n = int(input())

suma = 0
mult = 1

for symbol in n:
    suma += int(symbol)
    mult *= int(symbol)
    n = n + 10
    print(suma)
    print(mult)

a = [1, 2, 3, 4, 5]
for i in range(0, 5):
    print(a[i])

obj = {
	'Минск': 'Беларусь',
	'Москва': 'Россия',
	'Киев': 'Украина'
}
for key in obj:
    print(key + ' - это ' + obj[key] + ' . ')
















