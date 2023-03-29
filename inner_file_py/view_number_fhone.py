import csv
import main


def view_number():
    with open("./inner_file_py/number_fhone.csv", 'r', encoding='utf-8') as file:
        read_number = csv.reader(file)
        for el in read_number:
            print(f"{el} - ", end="\t")
    while True:
        out = int(input("\nВведите 0 если желаете выйти в главное меню: "))
        if (out == 0):
            main.main_no_cowsay()
