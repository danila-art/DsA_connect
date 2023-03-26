# Главный файл системы DsA_connect
import cowsay
import sys
import time
sys.path.insert(0, "inner_file_py")  # Инициализация папки inner_file_py
import read_text_file
import registration_user
import view_tarif_plan
import autorization
# ----------------------------------------------------------------------------------------------------------------------------------------------


def main():  # Главная функция управления
    cowsay.cow("Добро пожаловать в команию DsA connect!\nЕсли вы еще не подключились к нам, регистрируйся, приходи в офис и подключайся)")
    time.sleep(1)
    main_system_viev()
    print("Совет: Сначала прочти руководство пользователя, если ещё не читал, а то запутаешься:)\n------С лучшими пожеланиями: Администратор")
    main_value = check_main_value()
    main_select_value(main_value)

# ----------------------------------------------------------------------------------------------------------------------------------------------


# Главная функция перенаправления в зависимости от выбора пользователя
def main_select_value(user_value):
    arrValue = arr_select()
    if (user_value == 1):
        print(f"Вы выбрали: ({arrValue[0]})")
        # Запуск модуля
        print("Запуск просмотра Тарифных планов...")
        time.sleep(1)
        view_tarif_plan.view_tarif_plan_user()

    elif (user_value == 2):
        print(f"Вы выбрали: ({arrValue[1]})")
        # Запуск модуля

    elif (user_value == 3):
        print(f"Вы выбрали: ({arrValue[2]})")
        # Запуск модуля
        print("Запуск файла Регистрации...")
        time.sleep(1)
        registration_user.main_get_data()

    elif (user_value == 4):
        print(f"Вы выбрали: ({arrValue[3]})")
        # Запуск модуля
        print("Запуск авторизации...")
        time.sleep(1)
        autorization.autorizationUser()
    elif (user_value == 5):
        print(f"Вы выбрали: ({arrValue[4]})")
        # Запуск модуля
        print("Запуск руководства...")
        time.sleep(1)
        read_text_file.read_guide()
    elif (user_value == 6):
        print(f"Вы выбрали: ({arrValue[5]})")
        # Запуск модуля


def main_system_viev():  # Функция представления выбора действий
    arrValue = arr_select()
    # Придумать красивый вывод функций управвления в итоге сократится и кол-во строк
    for el in arrValue:
        print("-"*int(len(el)))
        print(el)
        print("-"*int(len(el)))
        time.sleep(1)


def arr_select():
    # Для сокрашения объявления переменных использовать список
    arrValue = [
        "| (1) < - Просмотр тарифных планов. |",
        "| (2) < - Посмотреть номера телефонов |",
        "| (3) < - Зарегестрироваться |",
        "| (4) < - Авторизироваться |",
        "| (5) < - Руководство пользователя |",
        "| (6) < - О компании |"
    ]
    return arrValue


def check_main_value():
    while True:
        main_value = input("Выберете дальнейшее действие: ")
        if (main_value == ""):
            print("Вы ничего не указали, повторите попытку...")
            time.sleep(1)
        elif (main_value.isdigit() == False):
            print("Попробуйте еще раз и введите только одно число...")
        elif (int(main_value) < 1 or int(main_value) > 7):
            print("Вы ввели несуществующее значение, попробуйте ещё раз...")
            main_value = False
        elif (main_value.isdigit() == True):
            return int(main_value)
            break
# Меню без коровы если пользователь возращается с другой страниы


def main_no_cowsay():
    time.sleep(1)
    main_system_viev()
    print("Совет: Сначала прочти руководство пользователя, если ещё не читал, а то запутаешься:)\n------С лучшими пожеланиями: Администратор")
    main_value = check_main_value()
    main_select_value(main_value)


if __name__ == "__main__":
    main()
