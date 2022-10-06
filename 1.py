name=input('Введите имя студента: ')
surname=input('Введите фамилию студента: ')
birthyear=int(input('Введите год рождения студента: '))
print(name,surname,birthyear, sep="_")
birthyear+=60
name,surname=surname,name
print(name,surname,birthyear, sep="_")