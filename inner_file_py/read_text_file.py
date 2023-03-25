import main as main_file


def read_guide():
    with open("./inner_file_py/guide_user.txt", 'r', encoding='utf-8') as file:
        guide = file.read()
        print("----------"*20)
        print(guide)
    while True:
        main = input("Чтобы вернуться в главное меню введите да:")
        if (main == 'да' or main == 'Да'):
            main_file.main_no_cowsay()
