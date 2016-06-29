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

if os.path.exists(file_tasks):
    # если файл существует
    # загружаем список задач из файла
    with open(file_tasks, 'r') as f:
        try:
            # при загрузке могут возникнуть какие то ошибки
            tasks = json.load(f)
            for task in tasks:
                task['start'] = (datetime.datetime.strptime(task['start'], 
                                date_format))
                task['end'] = (datetime.datetime.strptime(task['end'], 
                              date_format))
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
            sys.exit()

        else:
            print u'Введите верное значение'

def new_note():
    """
    функция принимающая новую задачу от пользователя
    """ 
    # вводим нашу задачу
    new_target = raw_input(u'Введите новую задачу: '.encode('utf-8'))
    get_fp(new_target)
    # Цикл проверки на правильность ввода даты 
    while True:
        # получаем у пользователя дату начала и конца задачи ввиде строки
        data_start = raw_input(
            u'Введите дату начала выполнения задачи '
            u'(год.месяц.число):\n '.encode('utf-8'))
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
        u'Введите дату завершения задачи(год.месяц.число):\n'
        .encode('utf-8'))
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
        'target': new_target, 
        'start': dt_start,   
        'end': dt_end, 
        'status': 'not done',
        } 
        # добавляем наш словарь в список
    tasks.append(new_task)
        # записываем наш список в файл     
    write_file()    
        # возвращаемся в начало программы        

def all_note():
    """
    функция просмотра списка задаx

    """  
    
    for (number, task) in enumerate(tasks, start=1):
        # переменная будет хранить название задачи
        a = task['target']
        # если у название задачи больше 10 символов  мы его обрезаем
        if len(a) > 10:
            task['target'] = a[:10-3] + '...'     
        string = u'Задача №{0:2}: {target:10}; {start}; {end}; {status}.'\
        .format(number, **task)
        print  string      
    # возвращаемся в начало запроса задач.    

def perfom_note():
    """    
    функция для просмотра выполненых задач
    """
    print u'Список выполненых задач \n',"="* 50
    # организуем цикл проверки каждого элемента списка
    for task in tasks:
        # если есть похожее значение в ключе мы его принтуем
        if task['status'] == 'done':
            string = u'Задача: {target:<10}; {start}; {end}; {status}.'\
            .format(**task)
            print string                

def future_note():
    """
    функция просмотра для будущих задач         
    """
    now = datetime.datetime.now()
    # организуем цикл проверки каждого элемента списка
    for task in tasks:
        # получаем значение конца даты задачи
        # сравниваем дату конца задачи с сегодняшним числом
        if task['end'] > now:
            string = u'Задача: {target};{start};{end};{status}'.format(**task)
            print string 

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
        # преобразуем формат datetime  в строку для корректной записи в файл.
        task['start'] = task['start'].strftime(date_format)
        task['end'] = task['end'].strftime(date_format)
        write_tasks.append(task)
    # создаем файл с нашими данными
    with open(file_tasks, 'w') as f:
        # преобразуем наш словарь в строку для записи в файл.
        data = json.dump(write_tasks, f, sort_keys=True)  
# возвращаемся в начало запроса задач.              
def get_fp(size=10):
    """
    приджнимает строку, и макс размер длины строки
    и если строка длинее этого размера, то обрежет её и добавит 
    в конце три точки
    """
    for task in tasks:
        a = task['target']
        if len(a) > size: 
           return a[:size-3] + '...'
        return a
main()


