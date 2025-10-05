input_line = input("Введите вещественные числа через пробел: ")
numbers = []
for num_str in input_line.split():
    try:
        numbers.append(float(num_str))
    except ValueError:
        print(f"Пропущено неверное значение: {num_str}")
file_name = "numbers.txt"
with open(file_name, 'w') as file:
    for num in numbers:
        file.write(f"{num}\n")

print(f"Числа записаны в файл {file_name}")