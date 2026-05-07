from mapbook_lib.model import users
from mapbook_lib.controler import read_users, adder_user, remove_user, update_user, user_post

def main():
    while True:
        print('=======MENU======')
        print('0 - zakoncz program')
        print('1 - wyswitl znajomych')
        print('2 - dodaj znajmych')
        print('3 - usun znajomych')
        print('4 - aktualizauj znajomych')
        print('5 - update posta')
        choice = input('wybierz opcje menu: ')
        print(f'wybrano opcje {choice}')
        if choice == '0':
            break
        if choice == '1': read_users(users)
        if choice == '2': adder_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': update_user(users)
        if choice == '5': user_post(users)

if __name__ == '__main__':
    main()