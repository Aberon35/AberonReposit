import re

with open('some_text.txt', 'r', encoding='utf-8') as file:
    content = file.read()
numbers = re.findall(r'\d+', content)

# Преобразуем строки чисел в целые числа и вычисляем сумму
sum_1 = sum(map(int, numbers))

print(f"Сумма всех чисел в файле: {sum_1}")