def process_input(user_input):
    try:
        # Заменяем запятую на точку для корректного преобразования в float
        user_input = user_input.replace(',', '.')

        number = float(user_input)
        is_zero = number == 0
        is_integer = user_input[0] == '-' and user_input[1:].replace('.', '').isdigit() or user_input.replace('.',
                                                                                                              '').isdigit()
        is_negative = number < 0
        is_float = "." in user_input or "," in user_input

        if is_zero:
            return f'You entered zero.'

        if is_float:
            result_message = f'You entered a {"negative" if is_negative else "positive"} float: {number}'
        else:
            result_message = f'You entered a {"negative" if is_negative else "positive"} integer: {int(number)}'

        return result_message

    except ValueError:
        return f'You entered an incorrect number: {user_input}'


def main():
    while True:
        user_input = input('Enter a number or type "exit" to quit: ').lower()

        if user_input in ['exit', 'quit', 'e', 'q']:
            print('Exiting the program.')
            break
        else:
            result = process_input(user_input)
            print(result)


if __name__ == "__main__":
    main()

