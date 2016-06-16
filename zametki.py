# coding:utf-8

"""
    Программа для ведения заметок и записи задач
"""

import datetime
import json
import os
import sys

# список наших задач
tasks = []
# пременная названия нашего файла
file_tasks = 'tasks.txt'

if os.path.exists(file_tasks):
    # если файл существует
    # загружаем список задач из файла
    with open(file_tasks, 'r') as f:
        try:
            # при загрузке могут возникнуть какие то ошибки
            tasks = json.load(f)
        except Exception:
            # при возникновении любой ошибки, будем считать файл не корректным
            tasks = []
        # а если ошибок нет, значит наш список успешно загрузился
else:
    # файла нет, значит и задач ещё нет
    tasks = [] 

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
                5.Удалить заметку. \n
                6.Изменить задачу.'''
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
    
    elif variant == '6':
        change_note()

    elif variant == '0':
        exit_note()

    else:
        print u'Введите верное значение'
        
        return main()

def new_note():
    """
    функция принимающая новую задачу от пользователя
    """ 
    message = 1
    while message == 1:
        # вводим нашу задачу
        new_target = raw_input(u'Введите новую задачу: '.encode('utf-8'))
        
        # получаем у пользователя дату начала и конца задачи ввиде строки
        data_start = raw_input(
            u'Введите дату начала выполнения задачи '
            u'(год.месяц.число):\n '.encode('utf-8'))
    
        # проверка на правильность ввода даты
        try:
            # с помощью функции datetime преобразуем полученные строки 
            # в необходимый нам формат даты
            # получаем дату начала задачи
            dt_start = datetime.datetime.strptime(data_start, '%Y.%m.%d')

        except ValueError:
            # перехватываем ошибку    
            print u'Вы ввели неверный формат даты!Повторите ввод '
            # возвращаемся в начало запроса даты    
            return

        data_end = raw_input(
            u'Введите дату завершения задачи(год.месяц.число):\n'
            .encode('utf-8'))
    
        try:
            # с помощью функции datetime преобразуем полученные строки 
            # в необходимый нам формат даты
            # получаем дату конца задачи
            dt_end = datetime.datetime.strptime(data_end, '%Y.%m.%d')    
        
        except ValueError:
            # перехватываем ошибку    
            print u'Вы ввели неверный формат даты!Повторите ввод '
            # возвращаемся в начало запроса даты    
            return
        # создаем наш словарь с задачей.
        new_task = {
            'target': new_target, 
            'start': data_start,   
            'end': data_end, 
            'status': 'not done',
        } 
        # добавляем наш словарь в список
        tasks.append(new_task)
        # записываем наш список в файл 
        write_file()    
        # возвращаемся в начало программы
        message = input(u'Задача добавлена. Продолжить? 1-Да,0-Нет\n'
        .encode('utf-8'))
     
    else:


        main()    
        


def all_note():
    """
    функция просмотра списка задач
    """
    for (number,task)in enumerate(tasks):
        number += 1
        string = u'Задача №{0}: {target}; {start}; {end}; {status}.'\
        .format(number,**task)
        print string    
    # возвращаемся в начало запроса задач.   
    
def perfom_note():
    """    
    функция для просмотра выполненых задач
    """
    # организуем цикл проверки каждого элемента списка
    for task in tasks:
        if task['status'] == 'done':
            string = u'Задача: {target}; {start}; {end}; {status}.'\
            .format(**task)
            print string
                

    return main()

def future_note():
    """
    функция просмотра для будущих задач         
    """
    # переменная с текущей датой
    now_date = datetime.datetime.now()
    # организуем цикл проверки каждого элемента списка
    for task in tasks:
        # получаем значение конца даты задачи
        data = task['end']
        # преобразуем в формат datetime 
        data_end = datetime.datetime.strptime(data,'%Y.%m.%d')
        # сравниваем дату конца задачи с сегодняшним числом
        if data_end < now_date:
            string = u'Задача: {target};{start};{end};{status}'.format(**task)
            print string 
    

    return main()

def del_note():
    """
    функция удаления задачи.
    """
    # определяем переменную для записи идентификатора задачи
    del_task = 0
    # вызываем функцию просмотра всех задач.
    all_note()
    # просим пользователя ввести номер задачи
    del_target = input(u'Введите номер задачи,которую хотите удалить:\n'
    .encode('utf-8'))
    # декременитируем введенное число,
    # т.к.элементы списка начинают отчет с нуля.
    del_task = del_target - 1
    
    try:    
        # удаляем элемент списка по его индексу.
        del tasks[del_task]
        # перезаписывам наш файл после изменения списка задач
        write_file()
    # перехватывем ошибку, если пользователь ввел не верное число. 
    except IndexError:
        print u'Вы ввели не верное значение!Повторите ввод.'
        
        del_note()  
    
    return main()       

def change_note(): 
    pass

def exit_note():
    """
    функция выхода из программы
    """
    sys.exit()
 
def write_file():
    """ 
    функция записи списка в файл
    """
    # создаем файл с нашими данными
    with open(file_tasks, 'w') as f:
        # преобразуем наш словарь в строку для записи в файл.
        data = json.dump(tasks, f, sort_keys=True)  
# возвращаемся в начало запроса задач.    
main()
