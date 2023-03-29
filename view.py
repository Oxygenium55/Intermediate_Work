import datetime

commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все заметки',
            'Создать заметку',
            'Удалить заметку',
            'Изменить заметку',
            'Найти заметку',
            'Фильтровать по дате',
            'Выход из программы']

def main_menu() -> int:
    print('Главное меню: ')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 10:
                return choice
            else:
                print('Введите значение от 1 до 9')
        except ValueError:
            print('Введите корректное значение: ')

def show_notes(note_list: list):
    if len(note_list) < 1:
        print('Заметки пусты или не открыты')
    else:
        print()
        for i, note in enumerate(note_list, 1):
            print(f'\t{i}. {note[0]:20} {note[1]:35} {note[2]:20}')
        print()

def input_error():
    print('Ошибка ввода. Введите корректный пункт меню')

def empty_request():
    print('Заметка не найдена')

def many_request():
    print('Найдено более одной заметки. Уточните данные.')

def create_new_note():
    title = input('Введите название заметки: ')
    message = input('Введите содержание заметки: ')
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    return title, message, now

def find_note():
    find = input('Введите искомый элемент: ')
    return find

def select_note(message: str):
    note = input(message)
    return note

def change_note():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    print('Введите новые данные. Если изменения не требуются, нажмите Enter')
    title = input('Введите название заметки: ')
    message = input('Введите содержание заметки: ')
    return title, message, now

def delete_confirm(note: str):
    result = input(f'Вы действительно хотите удалить заметку {note}? (y/n)').lower()
    if result == 'y':
        return True
    else:
        return False

def end_program():
    print('Программа завершена. До новых встреч!')

