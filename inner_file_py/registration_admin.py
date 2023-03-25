# Файл регистрации модератора взят на основе модуля registration_user
import csv
from registration_user import get_login, get_password, get_passport_number_and_series, get_surname, get_name, get_patronymic, get_birthday
import time
import admin

# get_login < - Создание логина
# get_password < - Создание пароля
number_fhone = None
# get_passport_number_and_series < - Ввод паспортных данных
# get_surname < - Ввод фамилии
# get_name < - Ввод имени
# get_patronymic < - Ввод отчества
# get_birthday < - Ввод даты дня рождения
tariff_plan = None
balance = 0
rang = "admin"


def create_moderator():
    login = get_login()
    password = get_password()
    pasport = get_passport_number_and_series()
    surname = get_surname()
    name = get_name()
    patronymic = get_patronymic()
    birthday = get_birthday()
    # Все данные получены
    dict_moderator = {
        "login": login,
        "password": password,
        "number_fhone":  number_fhone,
        "passport_number_and_series": pasport,
        "surname": surname,
        "name": name,
        "patronymic": patronymic,
        "birthday": birthday,
        "tariff_plan": tariff_plan,
        "balance": balance,
        "rang": rang
    }
    with open("./inner_file_py/user.csv", "a", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=dict_moderator)
        writer.writerow(dict_moderator)
    time.sleep(1)
    print("Вы успешно добавили модератора, возвращаюсь в главное меню Администратора...")
    time.sleep(1)
    admin.system_managment_admin()
