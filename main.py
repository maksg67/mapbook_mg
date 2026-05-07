# definicj prostej struktury danych obejmujacej przykladowego uzytkownika
users = [
    {"name": "artur", "location": "lomza",
     "posts": ["sprzedam mercedesa", "kupie skrzynie biegow", "ratunku co robic po wypadku",
               "kto dzisiaj idzie biegac"]},
    {"name": "daniel", "location": "legionowo",
     "posts": ["moj kodnie dziala pomocy"]},
    {"name": "kamil", "location": "ciechanow",
     "posts": ["czy ktos zrobil sprawozdanie z ppyt"]},

]


def read_users(users_data: list) -> None:
    for user in users:
        print(f'twoj znajomy {user["name"]}, z miejscowosci {user["location"]}, opublikowal post {user["posts"][-1]}')


read_users(users)


def adder_user(users_data: list) -> None:
    users_data.append({"name": input("podaj uzytkownika: "), "location": input("podaj loc: "),
                       "posts": ["dolaczono do znajomych"]})


def remove_user(user_data: list) -> None:
    user_to_remove = input("podaj imie znajomego do usuniecia: ")
    for user in user_data:
        if user["name"] == user_to_remove:
            users.remove(user)



def update_user(user_data: list) -> None:
    user_to_update = input("podaj imie znajomego do updatu: ")
    for user in user_data:
        if user["name"] == user_to_update:
            user['name'] = input('podaj nowe imie')
            user['location'] = input('podaj nowe loc')

def user_post(user_data: list) -> None:
    user_to_update = input("podaj imie znajomego do updatu: ")
    for user in user_data:
        if user["name"] == user_to_update:
            user['posts'].append(input('wassup beijing??? '))


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