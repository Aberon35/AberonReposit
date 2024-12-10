def caesar_cipher(text, shift):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(
        (lower[(lower.index(c) + shift) % 26] if c.islower() else
         upper[(upper.index(c) + shift) % 26] if c.isupper() else c)
        for c in text
    )

# Чтение строк из файла
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Шифрование и запись результатов в файл
encrypted_lines = [
    caesar_cipher(line.strip(), i + 1) + '\n' for i, line in enumerate(lines)
]

with open('output.txt', 'w', encoding='utf-8') as file:
    file.writelines(encrypted_lines)