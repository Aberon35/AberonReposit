def find_low_scores(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            try:
                name, grade = line.rsplit(maxsplit=1)
                if int(grade) < 3:
                    print(name)
            except ValueError:
                continue


file_path = input("Введите путь к файлу с данными: ")
# C:\\Users\\Strug\\Desktop\\AberonReposit\\Lesson 9\\task_5\\text.txt
find_low_scores(file_path)