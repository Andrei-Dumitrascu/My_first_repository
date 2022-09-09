# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)
# print(note_muzicale.count('do'))
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
# # 1 varianta
list1.extend(list2)
# print(list1)
# # a 2-a varianta
# list1 = list1 + list2
# print(list1)
# # a 3-a varianta
# for x in list2:
#     list1.append(x)
# print(list1)
# list1.sort(reverse = True)
# list1.sort()
# print(list1)
# print(list1.pop(0))
# print(list1)
# list1.sort()
# print(list1)
# print(list1.pop(0))
# list1.remove(1)
# print(list1)
# list3 = []
# if list1:
#     print('lista nu este goala')
# else:
#     print('lista este goala')
# sau
# if bool(list1):
#     print('list is not empty')
# else:
#     print('list is empty')
# sau
# if len(list1):
#     print('lista nu este goala')
# else:
#     print('lista este goala')
# list1.clear()
# print(list1)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# print(dict1.keys())
# x = dict1['Ana']
# y = dict1['Gigel']
# z = dict1['Dorel']
# print(f'Ana a luat nota {x}')
# print(f'Gigel a luat nota {y}')
# print(f'Dorel a luat nota {z}')
# dict1['Dorel'] = 6
# print(dict1)
# dict1.pop('Gigel')
# print(dict1)
# dict1['Ionica'] = 9
# print(dict1)
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# print(zile_sapt)
# zile_sapt.add('luni')
# print(zile_sapt)
# no duplicate
# weekend = {'sâmbăta', 'duminică'}
# if weekend.issubset(zile_sapt):
#     print('weekend este un subset')
# else:
#     print('weekend NU este un subset')
# print(zile_sapt.difference(weekend))
# print(zile_sapt.intersection(weekend))
# # data = ['Python', '5', 'Golang', '4', 'PHP', '3']
# # print("The original list : " + str(data))
# # res = [item.replace('4', '5') for item in data]
# # print("The list after substring replacement : " + str(res))
echipa = ['Andrei', 'Stefan', 'Doru', 'Valentin', 'Cosmin']
schimbari_efectuate = 0
schimbari_max = 3
while schimbari_efectuate < schimbari_max:
    x = input('Jucatorul schimbat: ')
    y = input('Jucatorul introdus: ')
    if x in echipa:
        print(f'jucatorul {x} este in echipa')
        echipa.remove(x)
        echipa.append(y)
        schimbari_efectuate += 1
        print(f'jucatorul {x} a fost inlocuit cu jucatorul {y} si mai ai {schimbari_max-schimbari_efectuate} schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {x} nu este pe teren')
        print(f'mai ai {schimbari_max-schimbari_efectuate} schimbari')
else:
    print('Nu mai ai schimbari disponibile')
print(echipa)
