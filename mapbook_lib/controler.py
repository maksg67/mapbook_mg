from mapbook_lib.model import users
def read_users(users_data: list) -> None:
    for user in users:
        print(f'twoj znajomy {user["name"]}, z miejscowosci {user["location"]}, opublikowal post {user["posts"][-1]}')




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
