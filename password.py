"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""
import re 

if __name__ == '__main__':
    print(f"The password is {'strong' if re.fullmatch(r'[A-Za-z0-9]{8,}', input('Enter new password: ')) else 'weak'}")
