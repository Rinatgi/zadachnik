# coding:utf-8
"""
   Программа для ведения заметок и записи задач
"""

import datetime
import json
import sys

new_tasks = [] # список наших задач

def main(): 
# функция для выбора необходимой задачи пользователем.
	print (u''' \nВыбирите необходимое действие: \n
				0.Выход.\n
				1.Добавить заметку. \n
				2.Посмотреть список всех задач. \n
				3.Список выполненных задач. \n
				4.Список будущих задач. \n
				5.Удалить заметку''')
	
	variant = raw_input(u'Выбирите значение '.encode('utf-8'))
	# проверка введенного значения.
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
	# функция принимающая новую задачу от пользователя	
	new_target = raw_input(u'Введите новую задачу: '.encode('utf-8'))# вводим нашу задачу
	# получаем у пользователя дату начала и конца задачи ввиде строки
	data_start = raw_input (u'''Введите дату начала выполнения задачи (год.месяц.число):\n '''.encode('utf-8'))

	data_end = raw_input (u'''Введите дату завершения задачи(год.месяц.число):\n'''.encode('utf-8'))
	# проверка на правильность ввода даты
	try:
	# с помощью функции datetime преобразуем полученные строки в необходимый нам формат даты
		dt_start = datetime.datetime.strptime(data_start,'%Y.%m.%d')# получаем дату начала задачи
		dt_end = datetime.datetime.strptime(data_end,'%Y.%m.%d')	# получаем дату конца задачи
	# перехватываем ошибку	
	except ValueError:
		print (u'Вы ввели неверный формат даты!Повторите ввод ')
		
		new_note() # возвращаемся в начало запроса даты	
	# создаем файл с нашими данными для задачи
	new_task = {'target':new_target,'start':data_start,'end':data_end,'status':'not done'} # создаем наш словарь с задачей.
	new_tasks.append(new_task) #добавляем наш словарь в список
	f = open('data1.txt','w')#создаем файл с нашими данными
	data = json.dump(new_tasks,f, sort_keys = True)# преобразуем наш словарь в строку для записи в файл.
	f.close() # закрываем наш файл.
	
	main()# Возващаемся в начало программы

def all_note():
	# функция просмотра списка задач
	f = open('data1.txt')
	data = json.load(f)# преобразуем строку в файле обратно наш список
	print (data)# смотрим список наших задач.
	f.close()
	
	main()

def perfom_note():

	try:
		f.values(u'done')
	except ValueError:
		print(u'Нет')
		
def future_note():
	print(u'Будущие задачи')

def del_note():
	# функция удаления задачи.
	del_target = raw_input(u'Введите задачу,которую хотите удалить:\n'.encode('utf-8'))
	# проверка на правильный ввод задачи и её существовании.
	try:
		del f[del_target]
	except KeyError:
		print (u'Нет такой задачи.Повторите ввод!'.encode('utf-8'))
		del_note()
	main()

def exit_note():
# функция выхода из программы

	sys.exit()


main()
# вызываем функцию для выбора	