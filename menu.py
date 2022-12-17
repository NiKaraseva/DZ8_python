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
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 0:
            return True


def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.lof_off()
            break
