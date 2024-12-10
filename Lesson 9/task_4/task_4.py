import re

def censor_file(file_to_censor, stop_words_file):
    # Загружаем запрещённые слова
    with open(stop_words_file, "r", encoding="utf-8") as sw_file:
        stop_words = sw_file.read().split()
    # Читаем текст из файла для цензуры
    with open(file_to_censor, "r", encoding="utf-8") as file:
        text = file.read()
    # Замена запрещённых слов на звёздочки
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, stop_words)) + r')\b', re.IGNORECASE)
    censored_text = pattern.sub(lambda match: '*' * len(match.group()), text)
    print("Результат цензурирования:")
    print(censored_text)


file_to_cens = input("Введите путь к файлу для цензуры: ")
# C:\\Users\\Strug\\Desktop\\AberonReposit\\Lesson 9\\task_4\\text.txt
stop_words_file = "stop_words.txt"
censor_file(file_to_cens, stop_words_file)