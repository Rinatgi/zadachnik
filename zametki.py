# coding:utf-8

"""
    Программа для ведения заметок и записи задач
"""

import datetime
import json
import os
import sys
# список наших задач
new_tasks = []
# пременная названия нашего файла
file_tasks = 'data1.txt'

if os.path.exists(file_tasks):
    # если файл существует
    # загружаем список задач из файла
    with open(file_tasks, 'r') as f:
        try:
            # при загрузке могут возникнуть какие то ошибки
            new_tasks = eval(f.read())
        except Exception:
            # при возникновении любой ошибки, будем считать файл не корректным
            new_tasks = []
        # а если ошибок нет, значит наш список успешно загрузился
else:
    # файла нет, значит и задач ещё нет
    new_tasks = [] 

def main(): 
    """ 
    функция для выбора необходимой задачи пользователем.
    """
    print u''' \nВыбирите необходимое действие: \n
                0.Выход.\n
                1.Добавить заметку. \n
                2.Посмотреть список всех задач. \n
                3.Список выполненных задач. \n
                4.Список будущих задач. \n
                5.Удалить заметку'''
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
        print u'Введите верное значение'
        
        main()

def new_note():
    """
    функция принимающая новую задачу от пользователя
    """    
    # вводим нашу задачу
    new_target = raw_input(u'Введите новую задачу: '.encode('utf-8'))
        
    # получаем у пользователя дату начала и конца задачи ввиде строки
    data_start = raw_input(
        u'Введите дату начала выполнения задачи '
        u'(год.месяц.число):\n '.encode('utf-8'))
    
    data_end = raw_input(
        u'Введите дату завершения задачи(год.месяц.число):\n'.encode('utf-8'))
    
    # проверка на правильность ввода даты
    try:
        # с помощью функции datetime преобразуем полученные строки 
        # в необходимый нам формат даты
        # получаем дату начала задачи
        dt_start = datetime.datetime.strptime(data_start, '%Y.%m.%d') 
        # получаем дату конца задачи
        dt_end = datetime.datetime.strptime(data_end, '%Y.%m.%d')    
    
    except ValueError:
        # перехватываем ошибку    
        print u'Вы ввели неверный формат даты!Повторите ввод '
        # возвращаемся в начало запроса даты    
        new_note() 
    
    # создаем наш словарь с задачей.
    new_task = {
        'target': new_target, 
        'start': data_start, 
        'end': data_end, 
        'status': 'not done',
    } 
    # добавляем наш словарь в список
    new_tasks.append(new_task) 
    # создаем файл с нашими данными
    with open(file_tasks, 'w') as f:
    # преобразуем наш словарь в строку для записи в файл.
        data = json.dump(new_tasks, f, sort_keys=True)     
    # закрываем наш файл.
    # возвращаемся в начало программы
    main()
    
def all_note():
    """
    функция просмотра списка задач
    """
    # выведем наши задачи по одному элементу в строке
    for i in range(len(new_tasks)): 
        # смотрим список наших задач.
        print new_tasks[i]
    
    # возвращаемся в начало запроса задач.
    main()

def perfom_note():
    """    
    функция для просмотра выполненых задач
    """
    # создаем переменную для будущих задач
    perfom_tasks = []
    # организуем цикл проверки каждого элемента списка
    for i in new_tasks:
        if i['status'] == 'done':
            perfom_tasks.append(i)
            print perfom_tasks
        else:
            print u'Нет выполненных задач'         

    main()

def future_note():
    """
    функция просмотра для будущих задач         
    """
    # создаем переменную для будущих задач
    future_tasks = []
    # организуем цикл проверки каждого элемента списка
    for i in new_tasks:
    # проверяем условия 
        if i['status'] == 'not done':
            # то добавляем в наш список
            future_tasks.append(i)
            print future_tasks
        # или выводим сообщение об этом    
        else:
            print u'Нет задач на будущее.'        

    main()    

def del_note():
    """
    функция удаления задачи.
    """
    del_target = raw_input(u'Введите задачу,которую хотите удалить:\n'
    .encode('utf-8'))
    # организуем цикл проверки каждого элемента списка
    for elem in new_tasks:
        if del_target in elem.values():
            new_tasks.remove(elem)
            
    main()

def exit_note():
    """
    функция выхода из программы
    """
    sys.exit()

# возвращаемся в начало запроса задач.    
main()
