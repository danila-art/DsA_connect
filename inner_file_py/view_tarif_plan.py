# Просмотр тарфиного плана
import csv
import time
import admin
import main as main_file
# ключи словаря: name_tarif, description_tarif, ithernet_tarif, minuts_tarif, sms_tarif, price_tarif


def view_tarif_plan_admin():
    with open('./inner_file_py/tariff_plans.csv', 'r', encoding='utf-8') as file:
        readTarif = csv.DictReader(file)
        for element in readTarif:
            print(
                f"-----------------------\nНазвание: {element['name_tarif']}\n-----------------------")
            print(f"Описание: {element['description_tarif']}")
            print(f"Количество Гигабайт: {element['ithernet_tarif']}")
            print(f"Количество Минут: {element['minuts_tarif']}")
            print(f"Количесвто SMS: {element['sms_tarif']}")
            print(f"Цена: {element['price_tarif']} руб.")
            print('----'*25)
    while True:
        main = input("Чтобы вернуться в главное меню введите да: ")
        if (main == 'да' or main == 'Да'):
            admin.system_managment_admin()


def view_tarif_plan_user():
    with open('./inner_file_py/tariff_plans.csv', 'r', encoding='utf-8') as file:
        readTarif = csv.DictReader(file)
        for element in readTarif:
            print(
                f"-----------------------\nНазвание: {element['name_tarif']}\n-----------------------")
            print(f"Описание: {element['description_tarif']}")
            print(f"Количество Гигабайт: {element['ithernet_tarif']}")
            print(f"Количество Минут: {element['minuts_tarif']}")
            print(f"Количесвто SMS: {element['sms_tarif']}")
            print(f"Цена: {element['price_tarif']} руб.")
            print('----'*25)
    while True:
        main = input("Чтобы вернуться в главное меню введите да:")
        if (main == 'да' or main == 'Да'):
            main_file.main_no_cowsay()
