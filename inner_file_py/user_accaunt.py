import csv


class user():
    user_login = None
    user_password = None
    user_number_fhone = None
    user_passport = None
    user_surname = None
    user_name = None
    user_patronymic = None
    user_birthday = None
    user_tariff_plan = None
    user_balance = None
    user_rang = None

    def __init__(self, login, password, number_fhone, passport_number_and_series, surname, name, patronymic, birthday, tariff_plan, balance, rang):
        self.user_login = login
        self.user_password = password
        self.user_number_fhone = number_fhone
        self.user_passport = passport_number_and_series
        self.user_surname = surname
        self.user_name = name
        self.user_patronymic = patronymic
        self.user_birthday = birthday
        self.user_tariff_plan = tariff_plan
        self.user_balance = balance
        self.user_rang = rang

    def set_data(self):
        print(f"Фамилия: {user.user_surname}")


def get_user(login, password):
    with open("./inner_file_py/user.csv", 'r', encoding="utf-8") as file:
        users = csv.DictReader(file)
        for user_element in users:
            if (user_element['login'] == login and user_element['password'] == password):
                user_auth = user(user_element['login'], user_element['password'], user_element['number_fhone'], user_element['passport_number_and_series'],  user_element['surname'],
                                         user_element['name'], user_element['patronymic'], user_element['birthday'], user_element['tariff_plan'], user_element['balance'], user_element['rang'])

    user_auth.set_data()
