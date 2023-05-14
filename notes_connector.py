from save_read_file import save_file
from user_commands import create_new_note, show_all_notis, search_notis, delete_notis, edit_notis
import json


def start_menu():
    print()
    print(f'{"*" * 10} Заметки {"*" * 10}')
    while True:
        program = input(str(f'{"-" * 30} \n           Меню\n{"*" * 30} \n'
                            f'{"-" * 10}Выберете:{"-" * 10}\n'
                            f'1 - Создать новую заметку\n'
                            f'2 - Показать все заметки\n'
                            f'3 - Найти заметку\n'
                            f'4 - Удалить заметку\n'
                            f'5 - Редактировать заметку\n'
                            f'6 - Выйти\n'
                            f'Введите цифру меню: '))
        
        tag_start = '1'        
        tag_show = '2'
        tag_find = '3'
        tag_delete = '4'
        tag_edit = '5'
        tag_out = '6'
        
        try:
            if program == tag_out:
                exit(0)
            elif program == tag_start:
                start = create_new_note()
                save_file(start)
                print(f'{"-" * 15}\nЗаметка создана!\n{"-" * 15}')
            elif program == tag_show:
                show_all_notis()
            elif program == tag_find:
                choice = input(f'{"-" * 15}Выберите значение для поиска:{"-" * 15}\n'
                               f'1 - Поиск по id\n'
                               f'2 - Поиск по теме\n'
                               f'3 - Поиск по сообщению в заметке\n'
                               f'4 - Поиск по дате и времени\n'
                               f'Введите номер меню: ')

                search_type = {
                    '1': 'id',
                    '2': 'title',
                    '3': 'msg',
                    '4': 'data'
                }
                try:
                    choice = search_type[choice]
                    us_list = json.load(open('notes.json', encoding='utf-8'))
                    if choice == 'id':
                        search = int(input('Введите id для поиска заметки (Например: 1):'))
                        search_notis(us_list, search, 1)
                    elif choice == 'title':
                        search = str(input('Введите "Тему заметки" для поиска (Например: Понедельник):'))
                        search_notis(us_list, search, 2)
                    elif choice == 'msg':
                        search = str(input('Введите "Текст заметки" для поиска (Например: Сегодня солнечно):'))
                        search_notis(us_list, search, 3)
                    elif choice == 'data':
                        search = str(input('Введите "Полную дату" для поиска (Например: 06-02-2023 18:23:59):'))
                        search_notis(us_list, search, 4)
                except FileNotFoundError:
                    print(f'Вы еще не создали ни одной заметки!')
            elif program == tag_delete:
                us_list = json.load(open('notes.json', encoding='utf-8'))
                print('Заметки, которые вы создали:')
                show_all_notis()
                notic_val = int(input(f'\nВведите id заметки, которую хотите удалить: '))
                delete_notis(us_list, 'id', notic_val)
            elif program == tag_edit:
                us_list = json.load(open('notes.json', encoding='utf-8'))
                print('Заметки, которые вы создали:')
                show_all_notis()
                notic_val = int(input(f'\nВведите id заметки, которую хотите изменить: '))
                edit_notis(us_list, 'id', notic_val)
        except KeyError:
            print('Вы ввели неверное значение, возврат в меню!')