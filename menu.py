import view
import data_base as db
import phone_book as pb

def main_menu(choice: int):
    match choice:
        case 1:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
        case 2:
            db.load_data_base()
            view.load_success()
        case 3:
            db.save_data_base()
            view.save_success()
        case 4:
            contact = view.input_new_contact()
            pb.new_contact(contact)
        case 5:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book) # вывели справочник на экран
            id = view.input_change_contact()
            view.print_change_contact(phone_book[id - 1]) # вывели контакт, который хотим изменить
            num = view.what_change() # выбрали, что именно хотим изменить: имя, телефон или комментарий
            if num == 1:
                new_name = view.change_name()
                pb.change_name(id, new_name) # меняем имя
                view.change_name_success()
            if num == 2:
                new_phone = view.change_phone()
                pb.change_phone(id, new_phone) # меняем телефон
                view.change_phone_success()
            if num == 3:
                new_comment = view.change_comment()
                pb.change_comment(id, new_comment) # меняем комментарий
                view.change_comment_success()
        case 6:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_remove_contact()
            if pb.remove_contact(id):
                view.remove_success()
        case 7:
            find = view.find_contact()
            new_phone_book = pb.find_contact(find)
            for contact in new_phone_book:
                if contact in new_phone_book == 0:
                    view.print_zero_contact()
                elif contact in new_phone_book == 1:
                    view.print_new_book_by_find(*new_phone_book)
                else:
                    view.print_new_book_by_find(new_phone_book)
        case 0:
            return True

def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.lof_off()
            break
