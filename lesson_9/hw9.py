def process_number_input(user_input):
    cleaned_input = user_input.replace(',', '.')

    if cleaned_input.replace('.', '', 1).replace('-', '', 1).isdigit():
        number = float(cleaned_input)
        if number > 0:
            return f"Вы ввели {'положительное'} {'целое' if number.is_integer() else 'дробное'} число: {number}"
        elif number < 0:
            return f"Вы ввели {'отрицательное'} {'целое' if number.is_integer() else 'дробное'} число: {number}"
        else:
            return "Вы ввели ноль"
    else:
        return f"Вы ввели не корректное число: {user_input}"


def main():
    exit_commands = ["выход", "exit", "quit", "e", "q"]

    while True:
        user_input = input(
            "Введите число или одно из значений (выход/exit/quit/e/q): ").lower()

        if user_input in exit_commands:
            print("Выход из программы.")
            break
        else:
            result = process_number_input(user_input)
            print(result)


if __name__ == "__main__":
    main()
