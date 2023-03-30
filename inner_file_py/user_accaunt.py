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
        print(
            f"Фамилия: {self.user_surname} | Имя: {self.user_name} | Отчество: {self.user_patronymic}")
        print(f"Дата Рожждения: {self.user_birthday}")
        print(f"Серия и номер паспорт: {self.user_passport}")
        if (self.user_number_fhone == ''):
            print(f"Номер телефона: нет")
        else:
            print(f"Номер телефона: {self.user_number_fhone}")
        if (self.user_tariff_plan == ''):
            print(f"Тарифный план: нет")
        else:
            print(f"Тарифный план: {self.user_tariff_plan}")
        print(
            f"-----------------------\nБаланс: {self.user_balance}\n-----------------------")

    def system_managment(self):
        print("| 1 - Привязать номер телефона. |")
        print("| 2 - Подключить тарифный план. |")
        print("| 3 - Пополнить баланс. |")
        print("| 0 - Выйти в главное меню |")

    def add_number_fhone(self):
        print("Выберите номер телефона:")
        new_arr_numbers = []
        with open("./inner_file_py/number_fhone.csv", 'r', encoding='utf-8') as file:
            read_number = csv.reader(file)
            print(read_number)
            print("------------------")
            i = 0
            for el in read_number:
                new_arr_numbers.append(el[0])
                print(f"{i} - >  {el}")
                i += 1
        while True:
            index_select = input("Введите номер элемента который выбрали: ")
            if (index_select.isdigit == False):
                print("Введите число")
            elif (int(index_select) < len(new_arr_numbers) and int(index_select) > len(new_arr_numbers)):
                print("Вы ввели недопустимое значение, попробуйте ещё раз")
            else:
                self.user_number_fhone = new_arr_numbers[int(index_select)]
                print(f"Ваш номер телефона: {self.user_number_fhone}")
                new_arr_numbers.remove(new_arr_numbers[int(index_select)])
                all_dict_user = []
                print(new_arr_numbers)

                with open("./inner_file_py/number_fhone.csv", 'w', encoding='utf-8', newline="") as file:
                    write = csv.writer(file)
                    for number in new_arr_numbers:
                        write.writerow(str(number).split(','))

                with open("./inner_file_py/user.csv", 'r', encoding='utf-8', newline="") as file:
                    dict_reader = csv.DictReader(file)
                    for el in dict_reader:
                        all_dict_user.append(el)
                fieldname = ["login", "password", "number_fhone", "passport_number_and_series",
                             "surname", "name", "patronymic", "birthday", "tariff_plan", "balance", "rang"]
                for element in all_dict_user:
                    if (element['login'] == self.user_login):
                        element.update(
                            {'number_fhone': self.user_number_fhone})
                with open("./inner_file_py/user.csv", 'w', encoding='utf-8', newline="") as file:
                    write = csv.DictWriter(file, fieldnames=fieldname)
                    write.writeheader()
                    for el in all_dict_user:
                        write.writerow(el)
                print("Вы успешно добавили номер...")
                get_user(self.user_login, self.user_password)
                break

    def add_tarif_plan(self):
        arr_name_tarif = []
        all_dict_user = []
        fieldname = ["login", "password", "number_fhone", "passport_number_and_series",
                     "surname", "name", "patronymic", "birthday", "tariff_plan", "balance", "rang"]

        print("Выберите тарифный план")
        with open("./inner_file_py/tariff_plans.csv", 'r', encoding='utf-8') as file:
            file = csv.DictReader(file)
            i = 0
            for element in file:
                print(f"{i} -> {element['name_tarif']}")
                arr_name_tarif.append(element['name_tarif'])
                i += 1
        select_tarif = int(input("Введите номер тарифного плана: "))
        with open("./inner_file_py/user.csv", 'r', encoding='utf-8', newline="") as file:
            dict_reader = csv.DictReader(file)
            for el in dict_reader:
                all_dict_user.append(el)
        for element in all_dict_user:
            if (element['login'] == self.user_login):
                element.update(
                    {'tariff_plan': arr_name_tarif[select_tarif]})
        with open("./inner_file_py/user.csv", 'w', encoding='utf-8', newline="") as file:
            write = csv.DictWriter(file, fieldnames=fieldname)
            write.writeheader()
            for el in all_dict_user:
                write.writerow(el)
        print("Вы успешно добавили Тарифный план...")
        get_user(self.user_login, self.user_password)
        

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
        if (user_select == ""):
            print("Вы не ввели значение...")
        elif (user_select < 0 or user_select > 3):
            print("Вы ввели несуществующее значение...")
        else:
            break
    if (user_select == 1):
        # Запуск метода класса
        print("Запуск привязки номера телефона...")
        user.add_number_fhone()
        pass
    elif (user_select == 2):
        # Запуск метода класса
        print("Запуск подключения тарифного плана")
        user.add_tarif_plan()
        pass
    elif (user_select == 3):
        # Запуск метода класса
        pass
    elif (user_select == 0):
        # Запуск метода класса
        time.sleep(1)
        print("Возвращаюсь в главное меню...")
        time.sleep(1)
        main_file.main_no_cowsay()
