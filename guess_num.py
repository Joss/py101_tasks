"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

import random

def task_3():
    UPPER_LIMIT = 1000000

    random_value = random.randint(0, UPPER_LIMIT)
    input_value = input(f"Enter your guess in 0-{UPPER_LIMIT}: ")
    while input_value not in ("", "exit"):
        if not input_value.isdigit() or (integer_value := int(input_value)) > UPPER_LIMIT:
            print("Wrong enter")
        else:
            if (integer_value == random_value):
                print(f"Your are right!")
                break

            hint = "greater" if integer_value > random_value else "less"
            print(f"Your guess is {hint} then the value")

        input_value = input(f"Enter your guess in 0-{UPPER_LIMIT}: ")

if __name__ == '__main__':
    task_3()
