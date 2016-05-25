#coding:utf-8
#Задание
#программа для ведения заметок.
#1.добавить заметку,удалить, посмотреть список всех задач, список выполненных,список будущих задач.
import shelve,sys
from datetime import datetime, date
new_tasks = {}
def main(): 
	print (u''' \nВыбирите необходимое действие: \n
				0.Выход.\n
				1.Добавить заметку. \n
				2.Посмотреть список всех задач. \n
				3.Список выполненных задач. \n
				4.Список будущих задач. \n
				5.Удалить заметку''')
	variant = raw_input(u'Выбирите значение '.encode('utf-8'))
	if variant == '1':
		new_note()
	elif variant == '2':
		all_note()
	elif variant == '3':
		perfom_note()		
	elif variant == '4':
		future_note()
	elif variant == '5':
		del_note()
	elif variant == '0':
		exit_note()	
		exit	
	else:
		print (u'Введите верное значение')
		main()
def new_note():
	new_target = raw_input(u'Введите новую задачу: '.encode('utf-8'))#вводим нашу задачу
	# получаем у пользователя дату начала и конца задачи ввиде строки
	data_start = raw_input (u'''Введите дату начала 
						выполнения задачи (год,месяц число):\n '''.encode('utf-8'))

	data_end = raw_input (u'''Введите дату завершения задачи
						(год,месяц,число):\n'''.encode('utf-8'))
	#проверка на правильность ввода даты
	try:
	#с помощью функции datetime преобразуем полученные строки в необходимый нам формат даты
		dt_start = datetime.strptime(data_start,'%Y.%m.%d')# получаем дату начала задачи
		dt_end = datetime.strptime(data_end,'%Y.%m.%d')	# получаем дату конца задачи
	#перехватываем ошибку	
	except ValueError:
		print (u'Вы ввели неверный формат даты!Повторите ввод ')
		new_note()# возвращаемся в начало запроса

	#new_task = {'target':new_target ,'start':dt_start, 'end':dt_end,'status': u'Не выполнено'}#создаем словарь с нашими данными 
	#print (new_task)
	status = 'not done'
	# создаем файл с нашими данными для задачи
	f = shelve.open('out.txt')# для этого используем модуль shelve
	f[new_target] = [dt_start,dt_end,status]# создаем кортеж  со словарем
	print (f.items)
	f.close

	main()# Возващаемся в начало программы
def all_note():
	f = shelve.open('out.txt')
	print (f.keys)
	f.close
	#print(u'Посмотреть список всех задач')
def perfom_note():
	f = shelve.open('out.txt')
	try:
		f.values(u'done')
	except ValueError:
		print(u'НЕт')
			
	#print(u'Выполненные задачи')	
def future_note():
	print(u'Будущие задачи')		
def del_note():
	del_target = raw_input(u'Введите задачу,которую хотите удалить:\n'.encode('utf-8'))
	f = shelve.open('out.txt')
	#проверка на правильный ввод задачи и её существовании.
	try:
		del f[del_target]
	except KeyError:
		print (u'Нет такой задачи.Повторите ввод!'.encode('utf-8'))
		del_note()
	f.close
	main()
	#print(u'Удалить задачу')
def exit_note():
	sys.exit()


main()# вызываем функцию для выбора	