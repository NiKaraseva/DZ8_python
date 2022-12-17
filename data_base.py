import phone_book as pb

path = 'phone_book.txt'

def load_data_base():
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book = file.readlines()
        pb.set_phone_book(str_to_list(phone_book))

def str_to_list(ph_book: str):
    new_book = []
    for contact in ph_book:
        new_book.append(contact.strip().split(';'))
    return new_book


