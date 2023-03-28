# Главный фал регистрации нового абонента
import time
import csv
import main as main_file


def main_get_data():
    login = get_login()
    password = get_password()
    number_fhone = None
    passport_number_and_series = get_passport_number_and_series()
    surname = get_surname()
    name = get_name()
    patronymic = get_patronymic()
    birthday = get_birthday()
    tariff_plan = None
    balance = 0
    rang = "user"
    data_user = {
        "login": login,
        "password": password,
        "number_fhone":  number_fhone,
        "passport_number_and_series": passport_number_and_series,
        "surname": surname,
        "name": name,
        "patronymic": patronymic,
        "birthday": birthday,
        "tariff_plan": tariff_plan,
        "balance": balance,
        "rang": rang
    }
    with open("./inner_file_py/user.csv", "a", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data_user)
        writer.writerow(data_user)
    time.sleep(1)
    print("Вы успешно зарегистрировались, возвращаюсь в главное меню...")
    time.sleep(1)
    main_file.main_no_cowsay()
# Получение логина


def get_login():
    while True:
        login = input("Введите login: ")
        if (login == ''):
            print("Поле не может быть пустым, введите login: ")
        else:
            with open("./inner_file_py/user.csv", "r", encoding="utf-8") as file:
                read = csv.DictReader(file)
                for element in read:
                    if (element['login'] == login):
                        print(
                            "Приносим извинения, но такой логин уже существует, попробуйте ещё раз")
                    else:
                        return login
                        break


# Получения пароля
def get_password():
    while True:
        password = input("Введите password: ")
        if (password == ''):
            print("Поле не может быть пустым, введите password: ")
        else:
            return password
            break


# Получение паспортных данных
def get_passport_number_and_series():
    while True:
        passport_number_and_series = input(
            "Введите passport_number_and_series: ")
        if (passport_number_and_series == ''):
            print(
                "Поле не может быть пустым, введите passport_number_and_series: ")
        else:
            return passport_number_and_series
            break


# Получение Фамилии
def get_surname():
    while True:
        surname = input("Введите surname: ")
        if (surname == ''):
            print("Поле не может быть пустым, введите surname: ")
        else:
            return surname
            break


# Получение Имя
def get_name():
    while True:
        name = input("Введите name: ")
        if (name == ''):
            print("Поле не может быть пустым, введите name: ")
        else:
            return name
            break


# Поулчение Отчества
def get_patronymic():
    while True:
        patronymic = input("Введите patronymic: ")
        if (patronymic == ''):
            print(
                "Поле не может быть пустым, введите patronymic: ")
        else:
            return patronymic
            break


# Получение даты дня рождения
def get_birthday():
    while True:
        birthday = input("Введите birthday: ")
        if (birthday == ''):
            print("Поле не может быть пустым, введите birthday: ")
        else:
            return birthday
            break
