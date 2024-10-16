# сложные типы данных

# list - список, массив, может хранить любой тип данных
# fruits = ['apple', 'banana', 'kiwi', 'orange']

# tuple - кортеж, тоже хранить любой тип данных, но никакие методы его не изменят
# password = ('qwerty123', '1234', '341')

# set - множество, хранит в себе только уникальные значения
# emails = {'ada@gmail.com','qwerty@gmail.ru', True, 1,2,3,3,2}

# dict - словарь, хранит в себе данные в виде ключа и значения  
#               key     :   value
# username = {'nickname':'pro100_vanya', 'age': 21, 12:33}


# students = ['malysh','vasya','gregory','timoty', '2oy']
# time = ('neverwasted','timewasted','lost_time')
# numbers = {1,2,3,3,3,3,3,3,44,12,32,'creeper','maloy'}
# vest = {'mine':'yours', 'ours':'theirs'}

# #            0         1       2        3
# fruits = ['apple', 'banana', 'kiwi', 'orange']

# fruits = [1,1,1,1,22,2,2,3,3,33,4,4,5,5,66,6,6,6,'apple','apple']

# fruits.append('lemon') # добавляет элемент в конец списка
# fruits.insert(2,'lemon') # добавляет элемент по индексу
# fruits.remove('kiwi') # удаляет элемент 
# fruits.pop(3) # удаляет элемент по индексу
# fruits.reverse() # разворачивает список
# fruits.clear() # очищает список 
# fruits.count('apple') # считает кол-во элементов в списке
# fruits.index('kiwi') # показывает индекс элемента в списоке (лучше юзать с print) 
# fruits.sort() # сортирует список, по алфавиту, регистре, но номеру
# print(len(fruits)) # считает кол-во элементов в списке
# print(sum(fruits)) # считает сумму элементов в списке если это числа
# print(max(fruits)) # макс знч если это число
# print(min(fruits)) # мин знч если это число
# fruits.extend([5,6,7]) # добавляет элемент в конец списка

# print(fruits.index('kiwi'))  
# print(fruits) 


#################################################################

#                0     1   2      3      4      5
# coordinates = (10, 20, 'xdv', '213', 'xdv', [12, 3]) # tuple
# print(coordinates.index(10)) # если в строке 2 похожих элемента то индекс выводит первую
# # print(coordinates.count('xdv')) # а каунт считает все похожие
# print(coordinates[4]) 



#################################################################

# set - множество м его методы
# num = {'hello', 'we', 'werr', 'we', 1, 2, 2}
# num.clear() # очистка множества
# num.add('xdv') # добавляет элемент 
# num.remove('we') # удаляет элемент, только один
# num.discard('we') # удаляет элемент и не ругается, если сделать ошибку в коде он не выводит
# num.update(['xdv', 'werr']) # обновляет множество, можно добавлять много элементов
# num.pop() # удаляет случайный элемент
# num.difference_update(['hello', 'we']) # удаляет все что написано в этом методе

# print(num) 


##################################################################



# Неизменяемые типы данных
# str
# int
# float
# bool
# tuple
# frozenset


# Изменяемые типы данных
# list
# set
# dict










