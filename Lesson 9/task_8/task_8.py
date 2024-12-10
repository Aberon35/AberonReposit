import json
import csv

# Чтение данных из JSON
def read_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)

# Преобразование JSON в CSV
def json_to_csv(json_data, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'birthday', 'height', 'weight', 'car', 'languages'])
        writer.writeheader()
        for employee in json_data:
            writer.writerow({
                'name': employee['name'],
                'birthday': employee['birthday'],
                'height': employee['height'],
                'weight': employee['weight'],
                'car': employee['car'],
                'languages': ', '.join(employee['languages'])
            })

# Сохранение в CSV
def save_to_csv(file_name, csv_file):
    json_data = read_json(file_name)
    json_to_csv(json_data, csv_file)

# Добавление сотрудника в JSON
def add_employee_to_json(file_name):
    new_employee = {
        "name": input("Имя: "),
        "birthday": input("Дата рождения: "),
        "height": float(input("Рост: ")),
        "weight": float(input("Вес: ")),
        "car": input("Автомобиль (true/false): ").lower() == 'true',
        "languages": [lang.strip() for lang in input("Языки: ").split(',')]
    }
    with open(file_name, 'r+', encoding='utf-8') as f:
        data = json.load(f)
        data.append(new_employee)
        f.seek(0)
        json.dump(data, f, indent=4)

# Добавление сотрудника в CSV
def add_employee_to_csv(file_name):
    new_employee = {
        'name': input("Имя: "),
        'birthday': input("Дата рождения: "),
        'height': float(input("Рост: ")),
        'weight': float(input("Вес: ")),
        'car': input("Автомобиль (true/false): ").lower() == 'true',
        'languages': ', '.join(input("Языки: ").split(','))
    }
    with open(file_name, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'birthday', 'height', 'weight', 'car', 'languages'])
        writer.writerow(new_employee)

# Поиск сотрудника по имени
def find_employee_by_name(file_name):
    name = input("Имя сотрудника: ").lower()
    with open(file_name, 'r', encoding='utf-8') as f:
        employees = json.load(f)
    for emp in employees:
        if emp['name'].lower() == name:
            print(f"Имя: {emp['name']}\nДата рождения: {emp['birthday']}\nРост: {emp['height']} см\nВес: {emp['weight']} кг\nАвтомобиль: {'Да' if emp['car'] else 'Нет'}\nЯзыки: {', '.join(emp['languages'])}")
            return
    print("Сотрудник не найден.")

# Фильтрация по языку
def filter_by_language(file_name):
    language = input("Язык программирования: ").lower()
    with open(file_name, 'r', encoding='utf-8') as f:
        employees = json.load(f)
    filtered = [emp for emp in employees if language in [lang.lower() for lang in emp['languages']]]
    if filtered:
        for emp in filtered:
            print(f"Имя: {emp['name']}, Языки: {', '.join(emp['languages'])}")
    else:
        print("Нет сотрудников с таким языком.")

# Фильтрация по году рождения и средний рост
def filter_by_birth_year(file_name):
    year = int(input("Год рождения: "))
    with open(file_name, 'r', encoding='utf-8') as f:
        employees = json.load(f)
    filtered = [emp for emp in employees if int(emp['birthday'].split('.')[2]) < year]
    if filtered:
        avg_height = sum(emp['height'] for emp in filtered) / len(filtered)
        print(f"Средний рост: {avg_height:.2f} см")
    else:
        print("Нет сотрудников, родившихся до этого года.")

# Меню
def interactive_menu():
    while True:
        print("\nМеню:\n1. Преобразовать JSON в CSV\n"
              "2. Сохранить в CSV\n"
              "3. Добавить сотрудника в JSON\n"
              "4. Добавить сотрудника в CSV\n"
              "5. Найти сотрудника по имени\n"
              "6. Фильтр по языку\n"
              "7. Фильтр по году рождения и средний рост\n"
              "8. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            json_to_csv(read_json('employees.json'), 'employees.csv')
        elif choice == '2':
            save_to_csv('employees.json', 'employees.csv')
        elif choice == '3':
            add_employee_to_json('employees.json')
        elif choice == '4':
            add_employee_to_csv('employees.csv')
        elif choice == '5':
            find_employee_by_name('employees.json')
        elif choice == '6':
            filter_by_language('employees.json')
        elif choice == '7':
            filter_by_birth_year('employees.json')
        elif choice == '8':
            break
        else:
            print("Неверный выбор.")

# Запуск программы
interactive_menu()