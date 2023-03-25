# Добавление тарфиного плана
import csv
import time
import admin


def add_tarif_plan():
    name_tarif = name_tarif_plan()
    description_tarif = description_tarif_plan()
    ithernet_tarif = ithernet_tarif_plan()
    minuts_tarif = minuts_tarif_plan()
    sms_tarif = sms_tarif_plan()
    price_tarif = price_tarif_plan()

    dict_tarif_plan = {
        "name_tarif": name_tarif,
        "description_tarif": description_tarif,
        "ithernet_tarif": ithernet_tarif,
        "minuts_tarif": minuts_tarif,
        "sms_tarif": sms_tarif,
        "price_tarif": price_tarif
    }

    with open('./inner_file_py/tariff_plans.csv', 'a', encoding='utf-8', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=dict_tarif_plan)
        writer.writerow(dict_tarif_plan)
    time.sleep(1)
    print("Вы успешно добавили тарифный план, возвращаюсь в главное меню Администратора...")
    time.sleep(1)
    admin.system_managment_admin()


def name_tarif_plan():
    while True:
        name_tarif = input("Введите название нового тарфинго плана: ")
        if (name_tarif == ''):
            print("Поле не может быть пустым, попробуйте заново...")
        else:
            break
    return name_tarif


def description_tarif_plan():
    while True:
        description_tarif = input("Введите описание нового тарфинго плана: ")
        if (description_tarif == ''):
            print("Поле не может быть пустым, попробуйте заново...")
        else:
            break
    return description_tarif


def ithernet_tarif_plan():
    while True:
        ithernet_tarif = input(
            "Введите количество гигабайтов нового тарфинго плана: ")
        if (ithernet_tarif == ''):
            print("Поле не может быть пустым, попробуйте заново...")
        else:
            break
    return ithernet_tarif


def minuts_tarif_plan():
    while True:
        minuts_tarif = input(
            "Введите количество минут нового тарфинго плана: ")
        if (minuts_tarif == ''):
            print("Поле не может быть пустым, попробуйте заново...")
        else:
            break
    return minuts_tarif


def sms_tarif_plan():
    while True:
        sms_tarif = input("Введите количество sms нового тарфинго плана: ")
        if (sms_tarif == ''):
            print("Поле не может быть пустым, попробуйте заново...")
        else:
            break
    return sms_tarif


def price_tarif_plan():
    while True:
        price_tarif = input("Введите стоимость нового тарфинго плана: ")
        if (price_tarif == ''):
            print("Поле не может быть пустым, попробуйте заново...")
        else:
            break
    return price_tarif
