phone_book = []


def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book

def new_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def change_name(id: int, new_name: str): # функция замены имени
    global phone_book
    phone_book[id - 1][0] = new_name
    set_phone_book(phone_book)

def change_phone(id: int, new_phone: str): # функция замены телефона
    global phone_book
    phone_book[id - 1][1] = new_phone
    set_phone_book(phone_book)

def change_comment(id: int, new_comment: str): # функция замены комментария
    global phone_book
    phone_book[id - 1][2] = new_comment
    set_phone_book(phone_book)

def remove_contact(id: int):
    global phone_book
    name = phone_book[id - 1][0]
    confirm = input(f'Вы точно хотите удалить контакт {name}? y/n\n')
    if confirm.lower() == 'y':
        phone_book.pop(id - 1)
        return True
    return False

def find_contact(find: str): # функция поиска контакта
    global phone_book
    new_phone_book = []
    count = 0
    for contact in phone_book:
        for item in contact:
            if find in item:
                new_phone_book.append(contact)
                count += 1
    if count > 0:
        return new_phone_book
    else:
        return False






