# Файл добавления номеров телефона
import csv
import admin

def add_number_fhone():
    print("Добро пожаловать в сценарий добавления номеров телефона\n Через секунду запустится цикл добавления номеров. \n Пример записи номеров (89375069109)\n Чтобы выйти из цикла и вернуться в главное меню введите один 0")
    while True:
        number_fhone = input("Введите номер телефона: ")
        if(number_fhone == ""):
            print("Вы ничего не ввели, попробуйте ещё раз.")
        elif(number_fhone == '0'):
            admin.system_managment_admin()
            break
        elif(number_fhone.isnumeric() == False):
            print("Вы ввели не число")
        elif(len(number_fhone) < 11):
            print("В вашем введенном номере меньше 11 символов, номер недействиителен. Попробуйте еще раз")
        else:
            with open("./inner_file_py/number_fhone.csv", 'a', encoding='utf-8') as file:
                write = csv.writer(file)
                write.writerow(number_fhone)

add_number_fhone()