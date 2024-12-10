import re


#Поиск слов и их количества
def get_most_count(a):
    #Ищем слова и помещаем их в список
    words = re.findall(r'\b\w+\b', a[0])
    #Словарь где key= слово value= количество
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1  #
        most_word = max(word_counts, key=word_counts.get)
        count = word_counts[most_word]
    return most_word, count


#Открываем файл
def create_list(a):
    with open(f"{a}", "r", encoding="utf-8") as file:
        #Добавляем строки в список
        list_of_str = file.readlines()
    print(list_of_str)
    result = []
    #Каждая строка в виде списка
    for str_file in list_of_str:
        most_word, count = get_most_count([str_file])
        result.append((most_word, count))
    return result


def create_new(file_path):
    result = create_list(file_path)
    with open("New_file.txt", "w", encoding="utf-8") as new_file:
        for word, count in result:
            new_file.write(f"Слово '{word}' встречается {count} раз(а)\n")


a = input("Введите абсолютный путь до вашего файла: ")
    #C:\\Users\\Strug\\Desktop\\AberonReposit\\Lesson 9\\task_3\\Some_text.txt
create_new(a)
