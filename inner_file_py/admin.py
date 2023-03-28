# Файл системы администратора
import time
import registration_admin
import add_tarif_plan
import view_tarif_plan
import add_number_fhone

def system_managment_admin():
    adminGetValue = system_hello_admin()
    if (adminGetValue == 1):
        print("Вы выбрали: зарегистрировать нового администратора.\nЗапуск программы")
        time.sleep(1)
        registration_admin.create_moderator()
        # Инструкция при выбранном значении
    elif (adminGetValue == 2):
        print("Вы выбрали: Смотреть полный список Тарифных планов.")
        time.sleep(1)
        view_tarif_plan.view_tarif_plan_admin()
        # Инструкция при выбранном значении
    elif (adminGetValue == 3):
        print("Вы выбрали: Добавить новый тарифный план.")
        time.sleep(1)
        add_tarif_plan.add_tarif_plan()
        # Инструкция при выбранном значении
    elif (adminGetValue == 4):
        print("Вы выбрали: Смотреть полную информацию о клиенте по номеру телефона.")
        time.sleep(1)

        # Инструкция при выбранном значении
    elif (adminGetValue == 5):
        print("Вы выбрали: Добавить новые номера телефонов.")
        time.sleep(1)
        add_number_fhone.add_number_fhone()
        # Инструкция при выбранном значении


def system_hello_admin():
    print("Добро пожаловать, Администратор, в систему управления проектом DsA connect:")
    time.sleep(4)
    print("Выберите функцию управления:")
    time.sleep(2)
    print("|(1) < - Зарегистрировать нового Администратора. | \n|(2) < - Смотреть полный список Тарифных планов. | \n|(3) < - Добавить новый тарифный план. | \n|(4) < - Смотреть полную информацию о клиенте по номеру телефона. | \n|(5) < - Добавить новые номера телефонов. |")
    time.sleep(1)
    adminGetValue = int(
        input("Введите значение действия которое хотите выполнить: - > "))
    return adminGetValue
