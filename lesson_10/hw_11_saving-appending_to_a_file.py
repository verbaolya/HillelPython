# Ввод четырех строк с клавиатуры
line1 = input("Введите первую строку: ")
line2 = input("Введите вторую строку: ")
line3 = input("Введите третью строку: ")
line4 = input("Введите четвертую строку: ")

# Создание и запись первых двух строк в файл
with open("output.txt", "w") as file:
    file.write(line1 + '\n')
    file.write(line2 + '\n')

# Открытие файла на редактирование и дозапись оставшихся двух строк
with open("output.txt", "a") as file:
    file.write(line3 + '\n')
    file.write(line4 + '\n')

print("Запись завершена.")
