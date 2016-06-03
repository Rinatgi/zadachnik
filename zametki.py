# coding:utf-8

"""
    Программа для ведения заметок и записи задач
"""

import datetime
import json
import sys

# список наших задач
new_tasks = [] 


def main(): 
    """ 
    функция для выбора необходимой задачи пользователем.
    """
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

	
def new_note():
    """
    функция принимающая новую задачу от пользователя
    """    
    # вводим нашу задачу
    new_target = raw_input(u'Введите новую задачу: '.encode('utf-8'))
	
    # получаем у пользователя дату начала и конца задачи ввиде строки
    data_start = raw_input (u'''Введите дату начала выполнения задачи (год.месяц.число):\n '''.encode('utf-8'))

    data_end = raw_input (u'''Введите дату завершения задачи(год.месяц.число):\n'''.encode('utf-8'))
	
    # проверка на правильность ввода даты
    try:
    # с помощью функции datetime преобразуем полученные строки в необходимый нам формат даты
        # получаем дату начала задачи
        dt_start = datetime.datetime.strptime(data_start, '%Y.%m.%d') 
        # получаем дату конца задачи
        dt_end = datetime.datetime.strptime(data_end, '%Y.%m.%d')	
    # перехватываем ошибку	
    except ValueError:
        print (u'Вы ввели неверный формат даты!Повторите ввод ')
        # возвращаемся в начало запроса даты	
        new_note() 
	
    # создаем наш словарь с задачей.
    new_task = {'target': new_target, 'start': data_start, 'end': data_end, 'status': 'not done'} 
    # добавляем наш словарь в список
    new_tasks.append(new_task) 
    # создаем файл с нашими данными
    f = open('data1.txt', 'w') 
    # преобразуем наш словарь в строку для записи в файл.
    data = json.dump(new_tasks, f, sort_keys = True) 	
    # закрываем наш файл.
    f.close() 
    # возвращаемся в начало программы
    main()
	

def all_note():
    """
    функция просмотра списка задач
    """
    f = open('data1.txt')
    # преобразуем строку в файле обратно наш список
    data = json.load(f)
    # выведем наши задачи по одному элементу в строке
    for i in range(len(data)): 
    # смотрим список наших задач.
    	print (data[i]) 
    # закрываем наш файл.
    f.close()
	
    # возвращаемся в начало запроса задач.
    main()


def perfom_note():
    """	
    функция для просмотра выполненых задач
    """
    f = open('data1.txt')
    data = json.load(f)
    # создаем переменную для будущих задач
    future_tasks = []
    # организуем цикл проверки каждого элемента списка
    for i in data:
        if i['status'] == 'not done':
            future_tasks.append(i)
            print (future_tasks)
        else:
            print('Нет будущих задач.')            
    f.close()

    main()
def future_note():
    """
    функция просмотра для будущих задач		 
    """
    f = open('data1.txt')
    data = json.dump(new_tasks, f)


def del_note():
    """
    функция удаления задачи.
    """
    # просим ввести необходимую задачу
    del_target = raw_input(u'Введите задачу,которую хотите удалить:\n'.encode('utf-8'))
    # проверка на правильный ввод задачи и её существовании.
    try:
        del f[del_target]
    except KeyError:
        print (u'Нет такой задачи.Повторите ввод!'.encode('utf-8'))
        del_note()
    main()


def exit_note():
    """
    функция выхода из программы
    """
    sys.exit()

# возвращаемся в начало запроса задач.	
main()
