import csv
import time
import main as main_file



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
        print(f"Фамилия: {self.user_surname} | Имя: {self.user_name} | Отчество: {self.user_patronymic}")
        print(f"Дата Рожждения: {self.user_birthday}")
        print(f"Серия и номер паспорт: {self.user_passport}")
        if(self.user_number_fhone == ''):
            print(f"Номер телефона: нет")
        else:
            print(f"Номер телефона: {self.user_tariff_plan}")
        if(self.user_tariff_plan == ''):
            print(f"Тарифный план: нет")
        else:
            print(f"Тарифный план: {self.user_tariff_plan}")
        print(f"-----------------------\nБаланс: {self.user_balance}\n-----------------------")

    def system_managment(self):
        if(self.user_number_fhone == ""):
            print("| 1 - Привязать номер телефона. |")
        if(self.user_tariff_plan == ""):
            print("| 2 - Подключить тарифный план. |")
        print("| 3 - Пополнить баланс. |")
        print("| 0 - Выйти в главное меню |")


def get_user(login, password):
    with open("./inner_file_py/user.csv", 'r', encoding="utf-8") as file:
        users = csv.DictReader(file)
        for user_element in users:
            if (user_element['login'] == login and user_element['password'] == password):
                user_auth = user(user_element['login'], user_element['password'], user_element['number_fhone'], user_element['passport_number_and_series'],  user_element['surname'],
                                         user_element['name'], user_element['patronymic'], user_element['birthday'], user_element['tariff_plan'], user_element['balance'], user_element['rang'])
    main_work_class(user_auth)
    

def main_work_class(user):
    print("Выгружаются ваши данные...\n----------------------------------------")
    time.sleep(1)
    user.set_data()
    print("Система управления личным кабинетом:")
    user.system_managment()
    while True:
        user_select = int(input("Введите значение процедуры: "))
        if(user_select == ""):
            print("Вы не ввели значение...")
        elif(user_select < 0 or user_select > 3):
            print("Вы ввели несуществующее значение...")
        else:
            break
    if(user_select == 1):
        # Запуск метода класса
        pass
    elif(user_select == 2):
        # Запуск метода класса
        pass
    elif(user_select == 3):
        # Запуск метода класса
        pass
    elif(user_select == 0):
        # Запуск метода класса
        time.sleep(1)
        print("Возвращаюсь в главное меню...")
        time.sleep(1)
        main_file.main_no_cowsay()


