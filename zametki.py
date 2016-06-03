# coding:utf-8

"""
   Программа для ведения заметок и записи задач
"""

import datetime
import json
import sys

# список наших задач
new_tasks = [] 

# функция для выбора необходимой задачи пользователем.
def main(): 

    print (u''' \nВыбирите необходимое действие: \n
				0.Выход.\n
				1.Добавить заметку. \n
				2.Посмотреть список всех задач. \n
				3.Список выполненных задач. \n
				4.Список будущих задач. \n
				5.Удалить заметку''')
	# просим ввести нужную задачу.
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
	
	
    else:
        print (u'Введите верное значение')
		
        main()

# функция принимающая новую задачу от пользователя	
def new_note():

	# вводим нашу задачу
    new_target = raw_input(u'Введите новую задачу: '.encode('utf-8'))
	
	# получаем у пользователя дату начала и конца задачи ввиде строки
    data_start = raw_input (u'''Введите дату начала выполнения задачи (год.месяц.число):\n '''.encode('utf-8'))

    data_end = raw_input (u'''Введите дату завершения задачи(год.месяц.число):\n'''.encode('utf-8'))
	
	# проверка на правильность ввода даты
    try:
	# с помощью функции datetime преобразуем полученные строки в необходимый нам формат даты
		# получаем дату начала задачи
        dt_start = datetime.datetime.strptime(data_start,'%Y.%m.%d') 
		# получаем дату конца задачи
        dt_end = datetime.datetime.strptime(data_end,'%Y.%m.%d')	
	# перехватываем ошибку	
    except ValueError:
        print (u'Вы ввели неверный формат даты!Повторите ввод ')
		# возвращаемся в начало запроса даты	
        new_note() 
	
	# создаем наш словарь с задачей.
    new_task = {'target':new_target,'start':data_start,'end':data_end,'status':'not done'} 
	# добавляем наш словарь в список
    new_tasks.append(new_task) 
	# создаем файл с нашими данными
    f = open('data1.txt','w') 
	# преобразуем наш словарь в строку для записи в файл.
    data = json.dump(new_tasks,f, sort_keys = True) 	
	# закрываем наш файл.
    f.close() 
	# возвращаемся в начало программы
    main()
	
# функция просмотра списка задач
def all_note():

    f = open('data1.txt')
	# преобразуем строку в файле обратно наш список
    data = json.load(f) 
	# смотрим список наших задач.
    print (data) 
	# закрываем наш файл.
    f.close()
	
	# возвращаемся в начало запроса задач.
    main()

# функция просмотра выполненых задач
def perfom_note():

    f = open('data1.txt')
    data = json.load(f)
    for key,val in data.items():
        print (key,val)

	''''try:
		f.values(u'done')
	except ValueError:
		print(u'Нет выпоненных задач')'''

# функция просмотра будущих задач		
def future_note():
	 
    f = open('data1.txt')
    data = json.dump(new_tasks,f)

# функция удаления задачи.
def del_note():
	
	# просим ввести необходимую задачу
    del_target = raw_input(u'Введите задачу,которую хотите удалить:\n'.encode('utf-8'))
	# проверка на правильный ввод задачи и её существовании.
    try:
        del f[del_target]
    except KeyError:
        print (u'Нет такой задачи.Повторите ввод!'.encode('utf-8'))
        del_note()
    main()

# функция выхода из программы
def exit_note():

    sys.exit()

# возвращаемся в начало запроса задач.	
main()
