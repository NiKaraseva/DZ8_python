

def main_menu():
    print('\n1. Показать телефонную книгу')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('\n0. Выход')
    return choice_main_menu()


def choice_main_menu():
    while True:
        try:
            choice = int(input('Выберите команду из меню: '))
            if choice in range(0, 8):
                return choice
            else:
                print('Такого пункта нет, повторите попытку!')
        except:
            print('Ошибка ввода, некорректные данные!')

def lof_off():
    print('Спасибо и всего хорошЕГО!')

def load_success():
    print('Телефонная книга загружена!')

def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('Телефонная книга пуста или не загружена')

def save_success():
    print('Телефонная книга сохранена!')

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите номер контакта: ')
    comment = input('Введите комментарий: ')
    return [name, phone, comment]

def input_change_contact(): # вводим id контакта, который хотим удалить
    id = int(input('\nВведите ID контакта, который желаете изменить: '))
    return id

def print_change_contact(contact: list):
    print(f'Вы хотите изменить контакт: ', end='')
    print(*contact)


def what_change(): # проверка на дурака: чтобы точно ввели 1, 2 или 3
    while True:
        try:
            num = int(input('Выберите, что хотите изменить: \n1. Имя\n2. Номер телефона\n3. Комментарий\n'))
            if num in range(1, 4):
                return num
            else:
                print('Такого пункта нет, повторите попытку!')
        except:
            print('Ошибка ввода, некорректные данные!')

def change_name(): # вводим новой имя
    new_name = input('Введите новое имя: ')
    return new_name

def change_name_success(): # сохранили новое имя
    print('Имя успешно изменено!')

def change_phone(): # вводим новый телефон
    new_phone = input('Введите новый телефон: ')
    return new_phone

def change_phone_success(): # сохранили новый телефон
    print('Телефон успешно изменён!')

def change_comment(): # вводим новый комментарий
    new_comment = input('Введите новый комментарий: ')
    return new_comment

def change_comment_success(): # сохранили новый комментарий
    print('Комментарий успешно изменён!')

def input_remove_contact():
    id = int(input('\nВведите ID контакта, который желаете удалить: '))
    return id

def remove_success():
    print('Контакт успешно удалён!')

def find_contact(): # спрашиваем, кого хотим найти
    find = input('Кого хотим найти?: ')
    return find

def print_new_book_by_find(new_phone_book: list): # печатаем, кого нашли
    print(f'Вы искали:')
    print(*new_phone_book)

def print_zero_contact(): # выводим сообщение, если по поиску ничего найти не удалось
    print('Такого контакта в справочнике нет')