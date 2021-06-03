# 3. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
# Решение покрыть тестами.

def re_numbers():
    numbers = {"One": "Один",
               "Two": "Два",
               "Three": "Три",
               "Four": "Четыре"}

    file1 = open("file_eng_numbers.txt", "r")
    file_out = open("file_ru_numbers.txt", "w")

    read = 1
    while read:
        line = file1.readline().replace("\n", "")
        if len(line) > 0:
            # print(numbers[line.split(" ")[0]])
            file_out.writelines(numbers[line.split(" ")[0]])
            file_out.writelines("\n")

        if not line:
            break
    file_out.close()


re_numbers()
