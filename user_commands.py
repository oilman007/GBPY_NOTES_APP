from user_interface import Notes
from datetime import datetime
from save_read_file import read_file, rewrite_file, get_cur_id


def create_new_note():
    
    header = create_header()
    msg = create_msg()
    id = get_cur_id()
    change_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    #new_notes = Notes(id, header, msg)
    result_note = save_note_to_data(id, header, msg, change_date)
    return result_note


def create_header():
    header = input('Введите заголовок Заметки: ')
    return header


def create_msg():
    msg = input('Введите заметку: ')
    return msg


def save_note_to_data(id, header, msg, date):
    
    date_list = {
        'id': id,
        'header': header,
        'msg': msg,
        'date': date
    }
    return date_list


def show_all_notis():
    try:
        data = read_file()
        for val in data:
            print(val)
    except FileNotFoundError:
        print(f'{"-" * 15}\nЗаметок еще нет\n{"-" * 15}')


def search_notis(data_list, search_data, choice):
    
    if choice == 1:
        data = list(filter(lambda x: x['id'] == search_data, data_list))
        if not data:
            print(f'\n\nДанных с таким id нет.\n\n')
        else:
            print(f'\n\nПо вашему запросу найдены следующие заметки: \n\n{data}\n')
    elif choice == 2:
        data = list(filter(lambda x: x['header'] == search_data, data_list))
        if not data:
            print(f'\n\nДанных с таким id нет.\n\n')
        else:
            print(f'\n\nПо вашему запросу найдены следующие заметки: \n\n{data}\n')
    elif choice == 3:
        data = list(filter(lambda x: x['msg'] == search_data, data_list))
        if not data:
            print(f'\n\nДанных с таким id нет.\n\n')
        else:
            print(f'\n\nПо вашему запросу найдены следующие заметки: \n\n{data}\n')
    elif choice == 4:
        data = list(filter(lambda x: x['date'] == search_data, data_list))
        if not data:
            print(f'\n\nДанных с таким id нет.\n\n')
        else:
            print(f'\n\nПо вашему запросу найдены следующие заметки: \n\n{data}\n')


def delete_notis(data_list: list, key, value):
    """
    Удаляет заметку по id
    
    """
    for index, dict_ in enumerate(data_list):
        if key in dict_ and dict_[key] == value:
            data_list.remove(dict_)
            print(f'Запись удалена: {dict_}')
        rewrite_file(data_list)


def edit_notis(data_list: list, key, value):
    """
    Изменяет заметку по номеру id
   
    """
    for i, dict_ in enumerate(data_list):
        if key in dict_ and dict_[key] == value:
            new_header = ''
            new_msg = ''
            change_header = input(f'Хотите оставить заголовок заметки: "{dict_.get("header")}" или поменять?\n'
                                 f'1 - Поменять\n'
                                 f'2 - Оставить\n')
            if change_header == '1':
                new_header = input(f'Введите новый заголовок заметки: ')
            elif change_header == '2':
                new_header = dict_.get('header')
            else:
                print('\nВведено неверное значение!\n')
            change_msg = input(f'Хотите оставить текст заметки: "{dict_.get("msg")}" или поменять?\n'
                               f'1 - Поменять\n'
                               f'2 - Оставить\n')
            if change_msg == '1':
                new_msg = input(f'Введите новый заголовок заметки: ')
            elif change_msg == '2':
                new_msg = dict_.get('msg')
            else:
                print('\nВведено неверное значение!\n')
            data_list[i] = {
                'id': value,
                'header': new_header,
                'msg': new_msg,
                'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
            print(f'Произведено изменение заметки с {dict_} на {data_list[i]}')
    rewrite_file(data_list)