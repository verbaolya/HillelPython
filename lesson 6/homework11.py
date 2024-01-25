import random

def generate_secret_number():
    """Генерує випадкове число від 1 до 100."""
    return random.randint(1, 100)

def take_user_guess():
    """Запитує користувача ввести варіант числа."""
    while True:
        try:
            guess = int(input("Введіть свій варіант числа (від 1 до 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Будь ласка, введіть число від 1 до 100.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

def check_guess(secret_number, user_guess):
    """Перевіряє, чи вірно вгадано число."""
    if user_guess < secret_number:
        return "Загадане число більше."
    elif user_guess > secret_number:
        return "Загадане число менше."
    else:
        return "Вітаємо! Ви вгадали число."

def play_game():
    """Головна функція для гри."""
    while True:
        print("Вгадайте число від 1 до 100.")

        secret_number = generate_secret_number()
        attempts = 0

        while True:
            user_guess = take_user_guess()
            attempts += 1

            result = check_guess(secret_number, user_guess)
            print(result)

            if result == "Вітаємо! Ви вгадали число.":
                print(f"Кількість спроб: {attempts}")
                break

        play_again = input("Бажаєте спробувати ще раз? (Так/Ні): ")
        if play_again.lower() != 'так':
            break

if __name__ == "__main__":
    play_game()