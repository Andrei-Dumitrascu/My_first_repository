import random
# Exercitiul 1
# if este un flow control, precede o conditie care daca e indeplinita codul curge intr-o directie
# else nu mai are nevoie de conditie, e celalalt caz
# Exercitiul 2
x = int(input('valoarea lui x este: '))
if x >= 0:
    print(f'nr {x} este natural')
else:
    print(f'nr {x} nu este natural')
# print(isinstance(x, int))
# Exercitiul 3
if x > 0:
    print(f'nr {x} este pozitiv')
elif x == 0:
    print(f'nr {x} este neutru')
else:
    print(f'nr {x} este negativ')
# Exercitiul 4
if -2 < x < 13:
    print(f'nr {x} este intre -2 si 13')
else:
    print(f'nr {x} NU este intre -2 si 13')
# Exercitiul 5
y = int(input('Valoarea lui y este: '))
if (x-y) < 5:
    print('Adevarat')
else:
    print('Fals')
# Exercitiul 6
if not 5 < x < 27:
    print(f'{x} nu este intre 5 si 27')
else:
    print(f'{x} este intre 5 si 27')
# Exercitiul 7
if x == y:
    print('nr sunt egale')
elif x > y:
    print(f'{x} este mai mare ca {y}')
else:
    print(f'{y} este mai mare decat {x}')
# Exercitiul 8
z = int(input('Valoarea lu z este: '))
if x == y == z:
    print('Triunghi echilateral')
elif x != y and x != z and y != z:
    print('Triunghi oarecare')
else:
    print('Triunghi isoscel')
# Exercitiul 9
litera = str(input('Introdu litera: '))
if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
    print(f'Litera {litera} este vocala')
else:
    print(f'Litera {litera} este consoana')
# Exercitiul 10
nota = float(input('Nota este: '))
nota_noua = ''
if nota > 9:
    nota_noua = 'A'
elif nota > 8:
    nota_noua = 'B'
elif nota > 7:
    nota_noua = 'C'
elif nota > 6:
    nota_noua = 'D'
elif nota > 4:
    nota_noua = 'E'
else:
    nota_noua = 'F'
print(f'Noua nota este: {nota_noua}')
# Exercitiul 1
X = int(input('Introdu nr X: '))
length = len(str(X))
print(length)
if length >= 4:
    print(f'nr {X} are minim 4 cifre')
else:
    print(f'nr {X} are mai putin de 4 cifre')
# Exercitiul 2
if length == 6:
    print(f'nr {X} are exact 6 cifre')
else:
    print(f'nr {X} nu are 6 cifre')
# Exercitiul 3
if X % 2 == 0:
    print(f'Nr {X} este par')
else:
    print(f'Nr {X} este impar')
# Exercitiul 4
Y = int(input('Introdu nr y: '))
Z = int(input('Introdu nr z: '))
if Z < Y < X or Y < Z < X:
    print(f'nr {X} este cel mai mare')
elif X < Z < Y or Z < X < Y:
    print(f'Nr {Y} este cel mai mare')
else:
    print(f'Nr {Z} este cel mai mare')
# Exercitiul 5
if (X+Y+Z) == 180:
    print('Triunghiul este valabil')
else:
    print('Triunghiul nu este valabil')
# Exercitiul 6
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(propozitie[0:len(propozitie)-x])
# Exercitiul 7
newString = propozitie[:5] + propozitie[-5:]
print(newString)
# Exercitiul 8
firstIndex = propozitie.find('rock')
print(firstIndex)
print(propozitie[0:firstIndex])
# Exercitiul 9
string9 = str(input('Introdu stringul: ')).lower()
assert string9[0] == string9[-1]
# Exercitiul 10
string1 = '0123456789'
print(string1[0:])
odd = ''
even = ''
for i in range(0, len(string1)):
    if int(string1[i]) % 2 == 0:
        even += string1[i]
        i += 1
    else:
        odd += string1[i]
        i += 1
print(even)
print(odd)
# Exercitiul 11
dice_roll = random.randint(1, 6)
nr_guess = int(input('Introdu nr: '))
if nr_guess < dice_roll:
    print(f'Ai ales un nr mai mic. Ai ales {nr_guess}, dar a fost {dice_roll}')
elif nr_guess > dice_roll:
    print(f'Ai ales un nr mai mare. Ai ales  {nr_guess}, dar a fost {dice_roll}')
else:
    print(f'Felicitari! Ai ales {nr_guess} si zarul a fost {dice_roll}')
