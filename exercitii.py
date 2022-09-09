# x, y, z = 'banana', 'portocala', 123
# a = b = c = 234.20
# print(f'{x, y}, {z, a, b, c}')
#
# # functia type() ne expune tipul de date al variabilei date ca input
# nume = 'Andrei'
# print(type(nume))
# # functiile int(), str(), bool(), float() schimba tipul de date
# cifra = '3'
# print(type(cifra))
# cifra = int(cifra) #schimbam tipul de date/type casting
# print(type(cifra))
# nume = 'Dumitrascu'
# prenume = 'Andrei'
# print('numele este' +' ' + nume +' prenumele este' +' ' + prenume)
# varsta = 30
# print(f'ma numesc {nume} {prenume} si am {varsta} ani')
# #assert e o modalitate prin care facem verificari in programare
# a = int(input('valoarea pentru a este'))
# assert a == 1
# print('trec pe aici')
# #string (index, len(), slicing, metode)
propozitie = 'Andrei invata testare automata la it factory'
# print(len(propozitie))
# print(propozitie[2])
# print(propozitie[0:20:3])
print(propozitie[0:20])
# print(propozitie[::-1])
# print(propozitie.upper())
# print(propozitie.lower())
# print(propozitie.replace(propozitie, 'Andrei-Gabriel'))
# print(propozitie.count('a'))
# nume = 'Dumitrascu'
# prenume = 'Andrei-Gabriel'
# caractere_nume = len(nume + prenume)
# print(f'numele este {nume} {prenume} si are {caractere_nume} caractere ')
# pret = 350.54
# pret = round(pret)
# print(type(pret))
# lungimea = 14
# latimea =2
# print(lungimea * latimea)
# print(f'aria dreptunghiului este {lungimea * latimea}')
#  prop = 'Coral is either the stupidest animal or the smartest rock'
#  print(prop.count(' the '))
# print(type(prop))
# propozitie = '0 Coral is either the 1  0 stupidest animal or the smartest rock'
# listaNumere = ['0', '1', '2']
# n = len(propozitie)
# #for i in range(0, n) :
#     # print(
#
# for str in propozitie:
#     for nr in listaNumere:
#         assert (nr == str)
#         print(nr)
# stringExercitiu = input('introdu un string impar ')
# print(stringExercitiu[len(stringExercitiu)//2])
# exercitiu = 'alabala portocala'; cuvant1 = 'alabala'; cuvant2 = 'portocala'; print(cuvant1, cuvant2)
# print(exercitiu.upper())
# caracter1 = exercitiu[0]
# for i in range(1, len(exercitiu)-1):
#     if exercitiu[i] == caracter1:
#        replace = exercitiu.replace(exercitiu[i], exercitiu[i].upper())
#     else:
#         i = i + 1
# print(replace)
exercitiu = 'alabala portocalu'
replace = exercitiu[1:len(exercitiu)-1]
ultimulCaracter = exercitiu[::-1]
print(replace)
for i in range(0,len(replace)):
    if replace[i] == exercitiu[0]:
        replace = replace.replace(replace[i], replace[i].upper())
    else:
        i = i + 1
print(exercitiu[0] + replace + ultimulCaracter[0])