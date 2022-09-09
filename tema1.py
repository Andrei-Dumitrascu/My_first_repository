# exercitiul 1
# variabila este o zona din memorie care stocheaza date; are un nume si o valoare
# exercitiul 2
animal = 'caine'
anNastere = 2011
viteza = 25.52236
adoptie = True
# exercitiul 3
print(type(animal))
print(type(anNastere))
print(type(viteza))
print(type(adoptie))
# exercitiul 4
viteza = round(viteza)
print(viteza)
print(type(viteza))
# exercitiul 5
print(f'Maria a adoptat un {animal}')
print(f'Cainele este nascut in {anNastere}')
print(f'Animalul alearga cu o viteza de {viteza}')
print(f'Cainele a fost adoptat? {adoptie}')
print(f'Maria are un {animal}, nascut in {anNastere}, care alearga cu viteza {viteza} si a fost adoptat {adoptie}')
# exercitiul 6
numele = input('Numele este: ')
prenumele = input('Prenumele este: ')
numeleComplet = numele + prenumele
print(numeleComplet)
nrCaractere = len(numele) + len(prenumele)
print(f'Numele complet este: {numele} {prenumele} si are {nrCaractere} caractere')
# exercitiul 7
lungimea = int(input('lungimea este:'))
latimea = int(input('latimea este: '))
x = lungimea * latimea
print(f'Aria dreptunghiului este: {x}')
# exercitiul 8, 9
# propozitie.count('the',0,-1)
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(propozitie.count(' the '))
# exercitiul 10
# print('a12345'.isnumeric())
# print('124256'.isnumeric())
# assert '12345'.isnumeric()
# print('e true')
# print('12456'.isdigit())
# print('2416'.isdecimal())
assert propozitie.isnumeric()
print('Stringul contine doar numere')
# exercitiul 1
stringImpar = str(input('Stringul impar este: '))
caracterMijloc = stringImpar[len(stringImpar)//2]
print(f'caracterul din mijloc este: {caracterMijloc}')
# exercitiul 2
palindrom = 'sugus'
# print(palindrom[0:len(palindrom)])
assert palindrom[0:len(palindrom)] == palindrom[::-1]
print('sirul este palindrom')
# split()
# exercitiul 3
exercitiu3 = str(input('introdu stringul: ')); cuvant1 = 'alabala'; cuvant2 = 'portocala'; print(cuvant1, cuvant2)
# exercitiul 4
exercitiu4 = str(input('introdu stringul: '))
firstcharacter = exercitiu4[0]
# print(firstcharacter)
lastcharacter = exercitiu4[len(exercitiu4)-1]
# print(lastcharacter)
exercitiu = exercitiu4[1:len(exercitiu4)-1].replace(firstcharacter, firstcharacter.upper())
print(f'{firstcharacter}{exercitiu}{lastcharacter}')
print(firstcharacter+exercitiu+lastcharacter)
# exercitiul 5
user = input('Userul este: ')
password = input('parola este: ')
nrCaractere = len(password)
# password = str(password)
final_password = ''
for i in range(0, len(password)):
    final_password += '*'
print(f'Parola pentru userul {user} este {final_password} si are {nrCaractere} caractere')
