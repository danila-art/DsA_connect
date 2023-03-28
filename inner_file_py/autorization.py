# Система авторизации (В одном файле cvs - ранг (клиент, модератор, админ <- админа нет в cvs файле, зайти под него можно только напрямую))
import admin
import csv
import user_accaunt
# -------------------------------------------------------------------------------------------------------------------------------------------------


def autorizationUser():  # Главная функция
    login = getLogin()
    password = getPassword()
    search = None
    with open("./inner_file_py/user.csv", 'r', encoding='utf-8') as file:
        users = csv.DictReader(file)
        for user in users:
            # print(user)
            # print(login)
            # print(password)
            if (login == user['login'] and password == user['password']):
                print("Пользователь найден")
                if (user['rang'] == 'admin'):  # Если ранг админ переходим к файлу admin.py
                    admin.system_managment_admin()
                    search = True
                    break
                # Если обычный пользователь то переходим к странице пользователя
                elif (user['rang'] == 'user'):
                    user_accaunt.get_user(login, password)
                    search = True
                    break
            else:
                search = False
    if (search == False):
        print("Пользователь не найден, попробуйте ещё раз...")
        autorizationUser()


# -------------------------------------------------------------------------------------------------------------------------------------------------


def getLogin():
    while True:
        login = input("Введите логин: ")
        if (login == ""):
            print("Вы оставили пустое поле")
        else:
            return login
            break


def getPassword():
    while True:
        password = input("Введите пароль: ")
        if (password == ""):
            print("Вы оставили пустое поле")
        else:
            return password
            break
