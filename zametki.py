# coding:utf-8

"""
    Программа для ведения заметок и записи задач
"""

import datetime
import json
import os
import sys

# пременная названия нашего файла
file_tasks = 'tasks.txt'
# формат даты 
date_format = '%Y.%m.%d'
# перменная,хранящая настяоящее время
now = datetime.datetime.now()

if os.path.exists(file_tasks):
    # если файл существует
    # загружаем список задач из файла
    with open(file_tasks, 'r') as f:
        try:
            # при загрузке могут возникнуть какие то ошибки
            tasks = json.load(f)
            for task in tasks:
                task['start'] = ( 
                    datetime.datetime.strptime(task['start'], date_format))
                task['end'] = (
                    datetime.datetime.strptime(task['end'], date_format))
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
    while True:
        print u''' \nВыберите необходимое действие: \n
                    0.Выход.\n
                    1.Добавить заметку. \n
                    2.Посмотреть список всех задач. \n
                    3.Список выполненных задач. \n
                    4.Список будущих задач. \n
                    5.Удалить заметку. \n
                    6.Изменить задачу.'''
        # просим ввести нужную задачу.
        # перехватываем ошибку,если пользоватеь нажал Ctrl+C
        try:  
            variant = input(u'Выберите значение '.encode('utf-8'))

        except KeyboardInterrupt:
            sys.exit()

        # проверка введенного значения 
        if variant == 1: 
            new_note()
                
        elif variant == 2:
            print_task()
        elif variant == 3:
            print_task(filter_perfom_note)
                #filter=lambda task: True if task['status']=='not done' 
                #else False)

        elif variant == 4:
            print_task(filter_future_note)
                #filter=lambda task: True if task['end']>now else False)

        elif variant == 5:
            del_note()

        elif variant == 6:
            change_note()

        elif variant == 0:
            sys.exit()

        else:
            print u'Введите верное значение'

def new_note():
    """
    функция принимающая новую задачу от пользователя
    """ 
    # вводим нашу задачу
    new_target = raw_input(u'Введите новую задачу: '.encode('utf-8'))
    # цикл проверки на правильность ввода даты 
    while True:
        # получаем у пользователя дату начала и конца задачи ввиде строки
        data_start = raw_input(
            u'Введите дату начала выполнения задачи '
            u'(год.месяц.число):\n'.encode('utf-8'))
        try:
            # с помощью функции datetime преобразуем полученные строки 
            # в необходимый нам формат даты
            # получаем дату начала задачи
            dt_start = datetime.datetime.strptime(data_start, date_format)
        except ValueError:
            # перехватываем ошибку,если не правильный ввод 
            # возвращаемся в начало запроса даты  
            print u'Вы ввели неверный формат даты!Повторите ввод '
        #если дата введена правильно продолжаем дальше    
        else:
            break    

    while True:
        data_end = raw_input(
            u'Введите дату завершения задачи '
            u'(год.месяц.число):\n'.encode('utf-8'))
        try:
            # с помощью функции datetime преобразуем полученные строки 
            # в необходимый нам формат даты
            # получаем дату конца задачи
            dt_end = datetime.datetime.strptime(data_end, date_format) 
        except ValueError:
            # перехватываем ошибку, если не правильный ввод
            # возвращаемся в начало запроса даты    
            print u'Вы ввели неверный формат даты!Повторите ввод '
        # если все норм переходим к другому действию                 
        else:
            break
    # создаем наш словарь с задачей
    new_task = {
        'target': new_target.decode('utf-8'), 
        'start': dt_start,   
        'end': dt_end, 
        'status': 'not done',
        } 
    # добавляем наш словарь в список
    tasks.append(new_task)
    # записываем наш список в файл     
    write_file()

def filter_perfom_note(task):
    """
    функция сортировки выполненых задач
    """
    if task['status'] == 'done':
        return True                 
    else:
        return False

def filter_future_note(task):
    """
    функция сортировки будущих задач
    """    
    if task['end'] > now:
        return True
    else:
        return False    

def print_task(filter=None):
    for (number, task) in enumerate(tasks, start=1):
        target = task['target'] 
        if filter is None:
            print( 
                u'Задача №{0}| {1:10} | {start} | {end} | {status}'
                .format(number, get_short_string(target), **task))
        elif filter(task) is True:
            print( 
                u'Задача №{0}| {1:10} | {start} | {end} | {status}'
                .format(number, get_short_string(target), **task))     

def del_note():
    """

    функция удаления задачи.
    """
    # определяем переменную для записи идентификатора задачи
    del_task = 0
    # вызываем функцию просмотра всех задач. 
    all_note()
    # просим пользователя ввести номер задачи  
    del_target = input(
        u'Введите номер задачи,'
        u'которую хотите удалить:\n'.encode('utf-8'))
    # декременитируем введенное число,  
    # т.к.элементы списка начинают отчет с нуля.  
    del_task = del_target - 1
    
    try:    
        # удаляем элемент списка по его индексу.  
        del tasks[del_task]
        
    # перехватывем ошибку, если пользователь ввел не верное число.   
    except IndexError:
        print u'Вы ввели не верное значение!Повторите ввод.'
    # перезаписывам наш файл после изменения списка задач           
    write_file()          

def change_note(): 
    pass
 
def write_file():
    """ 
    функция записи списка в файл  
    """
    # создаем новый список для записи в файл  
    write_tasks = []
    for task in tasks:
        #создадим копию нашего словаря,
        #чтобы не вносить изменения в основном словаре.  
        copy_task = task.copy()
        # преобразуем формат datetime  в строку для корректной записи в файл.
        copy_task['start'] = task['start'].strftime(date_format)
        copy_task['end'] = task['end'].strftime(date_format)
        write_tasks.append(copy_task)
    # создаем файл с нашими данными    
    with open(file_tasks, 'w') as f:
        # преобразуем наш словарь в строку для записи в файл.  
        data = json.dump(write_tasks, f, sort_keys=True)  

def get_short_string(target, size=10):
    """
    функция принимает строку, и макс размер длины строки
    и если строка длинее этого размера, то обрежет её и добавит 
    в конце три точки
    """
    three_dots = '...'
    if len(target) > size: 
        target = target[:size-len(three_dots) ] + three_dots
    return target

main()
