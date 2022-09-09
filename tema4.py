# exercitiul 1
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(cars)):
#     print(f'Masina mea preferata este {cars[i]}')
# for car in cars:
#     print(f'Masina mea preferata este {car}')
# j = 0
# while j < len(cars):
#     print(f'Masina mea preferata este {cars[j]}')
#     j += 1
# exercitiul 2
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(1, len(cars) - 1):
#     cars[i] = cars[i].upper()
# #   print(cars[i])
# else:
#     print(cars)
# exercitiul 3
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for car in cars:
#     if car == 'Mercedes':
#         print('Am gasit masina dorita de dumneavoastra')
#         break
#     else:
#         print(f'Am gasit masina {car}. Mai cautam')
# exercitiul 4
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for rich_car in cars:
#     if rich_car == 'Trabant' or rich_car == 'Lăstun':
#         continue
#     print(f'S-ar putea sa va placa masina {rich_car}')
# exercitiul 5
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# old_cars = []
# for i in range(len(cars)):
#     if cars[i] == 'Lăstun' or cars[i] == 'Trabant':
#         old_cars.append(cars[i])
#         cars[i] = 'Tesla'
# print(f'Modele vechi: {old_cars}, modele noi: {cars}')
# exercitiul 6
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.
# car_price = {'Dacia': 6800, 'Lăstun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}
# masini_ieftine = []
# for i in car_price:
#     if car_price[i] <= 15000:
#         masini_ieftine.append(i)
# print(f'Masinile care se incadreaza in acest buget: {masini_ieftine}')
# cheap_cars = []
# for key, value in car_price.items():
#     print(f'Masina este {key} si pretul este: {value}')
#     if value <= 15000:
#         print(f'Pentru un buget de sub 15000 euro puteti alege masina {key}')
#         cheap_cars.append(key)
# print(cheap_cars)
# exercitiul 7
# i = 0
# while i <= len(numere)-1:
#     print(numere[i])
#     i += 1
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# counter = 0
# for i in range(len(numere)):
#     print(numere[i])
#     if numere[i] == 3:
#         counter += 1
# print(f'Nr 3 apare de: {counter} ori')
# Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).
# exercitiul 8
# Aceeași listă:
# ● Iterează prin ea
# Calculează și afișează suma numerelor (nu ai voie să folosești sum).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma = 0
# for i in range(len(numere)):
#     suma += numere[i]
# print(suma)
# exercitiul 9
# Iterează prin ea.
# Afișază cel mai mare număr (nu ai voie să folosești max).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# maxim = 0
# for numar in numere:
#     if numar > maxim:
#         maxim = numar
# print(maxim)
# exercitiul 10
# Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# Afișază noua listă.
# numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         numbers[i] = -numbers[i]
# print(numbers)

# exercitii optionale
# exercitiul 1
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final
# other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# even_numbers = []
# odd_numbers = []
# positive_numbers = []
# negative_numbers = []
# for number in other_numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
#     else:
#         odd_numbers.append(number)
#     if number > 0:
#         positive_numbers.append(number)
#     else:
#         negative_numbers.append(number)
# else:
#     print(f'Lista nr pare: {even_numbers}')
#     print(f'Lista nr impare: {odd_numbers}')
#     print(f'Lista nr pozitive: {positive_numbers}')
#     print(f'Lista nr negative: {negative_numbers}')
# exercitiul 2
# Ordonează crescător lista fară să folosești sort.
# other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# new_list = []
# while other_numbers:
#     minim = other_numbers[0]
#     for number in other_numbers:
#         if number < minim:
#             minim = number
#     new_list.append(minim)
#     other_numbers.remove(minim)
# print(new_list)
# exercitiul 3
# Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
#
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!
# import random
# secret_number = random.randint(1, 30)
# print(secret_number)
# guessed_number = 0
# while guessed_number != secret_number:
#     guessed_number = int(input('Alege numarul: '))
#     if guessed_number < secret_number:
#         print('Nr secret e mai mare')
#     if guessed_number > secret_number:
#         print('Nr secret este mai mic')
# else:
#      print('Felicitari! Ai ghicit!')
# exercitiul 4
# Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333
# choose_number = int(input('Alege numarul de linii: '))
# for i in range(1, choose_number+1):
#     for j in range(1, i+1):
#         print(i, end = '')
#     print()
# exercitiul 5
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
# phone_keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
# for i in range(len(phone_keyboard)):
#     for j in range(len(phone_keyboard[i])):
#         print(f'Cifra curenta este: {phone_keyboard[i][j]}')

# sa facem o lista goala, adaugam in lista fibonacci pana la 1000, printam la final lista
# p = 0
# q = 1
# i = 2
# fibonacci = [p, q]
# while p + q <= 1000:
#     fibo = p + q
#     fibonacci.append(fibo)
#     p = q
#     q = fibo
#     i += 1
# print(fibonacci)