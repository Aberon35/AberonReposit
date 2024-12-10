import os

#Использовать ОДИН раз, лучше сделать копию

""" Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются
все файлы с расширением .txt, то же самое для остальных
расширений """

def sort_files(a): #Указать директорию
    os.chdir(a)
    folder_name = ""
    list_files = os.listdir()
    for file in list_files:
        # Присваиевам название нашего расширения
        file_ext = file[file.rfind(".")+1:]
        #Создаем папку
        if not folder_name == f"{file_ext}_folder":
            folder_name = f"{file_ext}_folder"
            os.mkdir(f"{a}\\{folder_name}")
        # #Перемещаем файл в папку
        os.replace(f"{file}", f"{folder_name}/{file}")

""" После рассортировки выводится сообщение типа «в папке
с текстовыми файлами перемещено 5 файлов, их
суммарный размер - 50 гигабайт """

"""Как минимум один файл в любой из получившихся
поддиректорий переименовать. Сделать вывод
сообщения типа «Файл data.txt был переименован в
some_data.txt"""

def count_and_size(a):
    os.chdir(a)
    folders = os.listdir()
    for folder in folders:
        count = 0
        size_all = 0
        os.chdir(f"{folder}")
        files = os.listdir()
        for file in files:
            count += 1
            size = os.stat(file).st_size
            size_all += size
        print(f"В папку {folder} перемещено {count} файлов, их суммарный размер - {size_all} байт» ")
        os.chdir("..")
    new_name = f"another_file.{file[file.rfind(".") + 1:]}"
    os.rename(f"{folder}\\{file}", f"{folder}\\{new_name}")
    print(f"Файл {file} был переименован в {new_name}")

# """Вывести имя вашей ОС"""
print(f"Имя вашей Операционной Системы: {os.name}")
a = input("Введите путь до папки, в которой вы находитесь: ") # C:\\Users\\Strug\\Desktop\\AberonReposit\\Lesson 9\\task_1\\Work
sort_files(a)
count_and_size(a)






