# for i in range(1, 20, 3):
#     print(i)
# # n = 375; 3*100+7*10+5
# # x = n%10-1
# # y = n//10-1
# # z = n//1000-1
# # print(z*100+y*10+x)
# n = 368
# x = n%10-1
# y = (n//10)%10-1
# z = n//100-1
# print(z*100+y*10+x)
# m = 34
# s = m%10
# t = m//10
# print(s**3+t**3)
# nume = input('Numele este ')
# parola = input('Parola este ')
# parola = str(parola)
# parola[0] = '*'
# print(parola)
parola = 1234
parola = str(parola)
x = len(parola)

# for i in range(0, len(parola)):
#     password = parola.replace(parola[i],'*')
# # print(password)
# x = '*'
# parola[0:len(parola),1] = x
# print(parola[0:len(parola):1])
# name = input("Enter a username: ")
#
# for c in range(len(name)):
# 	if not name[c].isnumeric():
# 		name[c] = ""
#
# print(name)
# name = input("Enter a username: ")
# password = 378
# password = str(password)
# final_password = ''
# for i in range(0, len(password)):
#     final_password +='*'
# y = final_password
# print(y)
nume = 'Andrei'
print(id(nume))
nume = 'Gabriel'
print(id(nume))