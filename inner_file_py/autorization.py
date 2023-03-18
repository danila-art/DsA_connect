# Система авторизации (В одном файле cvs - ранг (клиент, модератор, админ <- админа нет в cvs файле, зайти под него можно только напрямую))
import admin


# -------------------------------------------------------------------------------------------------------------------------------------------------
def autorizationUser(): #Главная функция
    login = getLogin()
    password = getPassword()
    print(login, password)
    if (login == "admin" and password == "admin"):
        # Инструкции системы админа
        admin.system_managment_admin()
# -------------------------------------------------------------------------------------------------------------------------------------------------

def getLogin():
    while True:
        login = input("Введите логин: ")
        if (login == ""):
            print("Errorlogin")
        else:
            return login
            break


def getPassword():
    while True:
        password = input("Введите пароль: ")
        if (password == ""):
            print("Errorpassword")
        else:
            return password
            break
