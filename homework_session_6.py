# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
# from math import pi
#
#
# class Circle:
#     radius: int
#     color: str
#
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
#
#     def describe_circle(self):
#         print(f'Raza este {self.radius}, culoarea este {self.color}')
#
#     def circle_area(self):
#         circle_area = pi*self.radius**2
#         return circle_area
#
#     def circle_diameter(self):
#         circle_diameter = self.radius*2
#         return circle_diameter
#
#     def circle_circumference(self):
#         circle_circmference = 2*pi*self.radius
#         return circle_circmference
#
#
# circle1 = Circle(radius=3, color='blue')
# circle1.describe_circle()
# print(f'Aria cercului este: {circle1.circle_area()}')
# print(f'Diametrul cerului este: {circle1.circle_diameter()}')
# print(f'Circumferinta cercului este: {circle1.circle_circumference()}')


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
#
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

# class Rectangle:
#     length: int
#     width: int
#     color: str
#
#     def __init__(self, length: int, width: int, color: str):
#         self.length = length
#         self.width = width
#         self.color = color
#
#     def describe_rectangle(self):
#         print(f'Lungimea dreptunghiului este {self.length}, latimea este {self.width}, culoarea este {self.color}')
#
#     def rectangle_area(self):
#         rectangle_area = self.length*self.width
#         return rectangle_area
#
#     def rectangle_perimeter(self):
#         rectangle_perimeter = 2*(self.length+self.width)
#         return rectangle_perimeter
#
#     def change_the_color(self, new_color: str):
#         self.color = new_color
#
#
# rectangle1 = Rectangle(length=4, width=2, color='white')
# rectangle1.describe_rectangle()
# print(f'Aria dreptunghiului este {rectangle1.rectangle_area()}')
# print(f'Perimetrul dreptunghiului este {rectangle1.rectangle_perimeter()}')
# rectangle1.change_the_color(new_color='black')
# rectangle1.describe_rectangle()

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

# class Employee:
#     last_name: str
#     first_name: str
#     salary: int
#
#     def __init__(self, last_name: str, first_name: str, salary: int):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.salary = salary
#
#     def describe_employee(self):
#         print(f'Nume: {self.last_name}, prenume: {self.first_name}, salariu: {self.salary}')
#
#     def full_name(self):
#         print(f'Numele intreg este: {self.last_name} {self.first_name}')
#
#     def monthly_salary(self):
#         print(f'Salariul lunar este: {self.salary}')
#
#     def annual_salary(self):
#         print(f'Salariul anual este: {self.salary*12}')
#
#     def salary_increase(self, percent: int):
#         salary_increase = self.salary + (percent/100*self.salary)
#         print(f'Noul salariu dupa marirea cu {percent}% este: {salary_increase}')
#
#
# angajat1 = Employee(last_name='Dumitrascu', first_name='Andrei-Gabriel', salary=100)
# angajat1.describe_employee()
# angajat1.full_name()
# angajat1.monthly_salary()
# angajat1.annual_salary()
# angajat1.salary_increase(percent=20)

# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

# class BankAccount:
#     iban: str
#     account_holder: str
#     balance: int
#
#     def __init__(self, iban: str, account_holder: str, balance: int):
#         self.iban = iban
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def display_balance(self):
#         print(f'Titularul {self.account_holder} are in contul {self.iban} suma de {self.balance} lei')
#
#     def debiting_account(self, debit_amount: int):
#         new_sold = self.balance + debit_amount
#         print(new_sold)
#
#     def lending_account(self, lending_amount: int):
#         sold = self.balance - lending_amount
#         print(sold)
#
#
# titular1 = BankAccount(iban='RO12345', account_holder='Dumitrascu Andrei-Gabriel', balance=1000)
# titular1.display_balance()
# titular1.debiting_account(debit_amount=250)
# titular1.lending_account(lending_amount=600)

# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
#
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# from tabulate import tabulate
# from datetime import date
#
# class Invoice:
#     SERIES: str = 'x'
#     number: int
#     name_of_product: str
#     quantity: int
#     price_per_piece: int
#
#     def __init__(self, number: int, name_of_product: str, quantity: int, price_per_piece: int):
#         self.number = number
#         self.name_of_product = name_of_product
#         self.quantity = quantity
#         self.price_per_piece = price_per_piece
#
#     def change_quantity(self, quantity: int):
#         self.quantity = quantity
#         return quantity
#
#     def change_price(self, price: int):
#         self.price_per_piece = price
#         return price
#
#     def change_name_of_product(self, name: str):
#         self.name_of_product = name
#         return name
#
#     def generate_invoice(self):
#         print(f'Factura Seria {self.SERIES} Numar {self.number}')
#         today = date.today()
#         print(f'Data: {today}')
#         # Produs | cantitate | preț bucată | Total
#         my_data = [[self.name_of_product, self.quantity, self.price_per_piece, self.quantity*self.price_per_piece]]
#         header = ['Produs', 'Cantitate', 'Pret bucata', 'Total']
#         invoice1.change_name_of_product(name='Laptop')
#         invoice1.change_price(price=20)
#         invoice1.change_quantity(quantity=3)
#         my_data.append([self.name_of_product,self.price_per_piece,self.quantity, self.quantity*self.price_per_piece])
#         table = tabulate(tabular_data=my_data, headers=header)
#         print(table)
#
#
# invoice1 = Invoice(number= 123, name_of_product= 'Telefon', quantity= 10, price_per_piece= 50)
# invoice1.generate_invoice()

# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

# class Car:
#     brand: str = 'Dacia'
#     car_model: str
#     top_speed: int
#     current_speed: int = 0
#     color: str = 'Gray'
#     available_colors: set = {'White', 'Black', 'Blue', 'Green', 'Red', 'Yellow', 'Orange'}
#     certified: bool = False
#
#     def __init__(self, car_model: str, top_speed: int):
#         self.car_model = car_model
#         self.top_speed = top_speed
#
#     def describe(self):
#         print(f'{self.brand}, {self.car_model}, {self.color}, {self.top_speed},
#         {self.current_speed}, {self.certified}')
#
#     def certified_car(self):
#         self.certified = True
#         return self.certified
#
#     def paint(self, color: str):
#         assert color in self.available_colors
#         self.color = color
#         return self.color
#
#     def accelerate(self, speed: int):
#         assert 0 <= speed <= self.top_speed
#         while speed <= self.top_speed:
#             speed += 1
#
#     def car_brakes(self, speed: int):
#         while speed > 0:
#             speed -=1
#
# car1 = Car(car_model='Logan', top_speed= 150)
# car1.describe()
# print(car1.certified_car())
# print(car1.car_brakes(speed=-5))
# print(car1.accelerate(speed=120))
# print(car1.paint(color='Blue'))

# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
#
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
# dict


class ToDoList:
    todo: dict = {}

    def add_task(self, name: str, description: str):
        self.todo[name] = description
        return self.todo

    def finish_task(self, name):
        to_do_pop = self.todo.pop(name)
        return to_do_pop

    def display_to_do_list(self):
        to_do_keys = self.todo.keys()
        return to_do_keys

    def additional_details(self, name):
        if name not in self.todo:
            task_check = input('Vreti sa adaugati taskul?')
            if task_check == 'nu':
                print('La revedere')
            else:
                task_details = input('Adaugati detalii task')
                self.todo[name] = task_details
                print(self.todo)


task1 = ToDoList()
print(task1.add_task(name='invatare', description='citesc si retin informatii'))
print(task1.add_task(name='deplasare', description='merg pe jos la munca'))
task1.finish_task(name='deplasare')
print(task1.display_to_do_list())
task1.additional_details(name='curatenie')
