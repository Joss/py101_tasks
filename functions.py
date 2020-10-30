"""Задания по ветвлениям, итерациям и вводу данных."""
import keyword

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
# x = list(map(int, input("Enter comma separated values: ").split()))
def check_even():
    if (list(filter(lambda number: int(number) % 2 == 0, input("Enter comma separated values: ").split(",")))):
        print("There is an even number")

      
# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
age = 17
print("Мы не продаём алкоголь несовершеннолетним") if age < 21 else sell_alcohol()


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
def is_keyword(str):
    return keyword.iskeyword(str)


# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь list tuple set dict 
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
def get_type(obj):
    type_translations = {"int": "число", "float": "число", "str": "строка", "bool": "булевый", "NoneType": "None",
                         "list": "список", "tuple": "кортеж", "set": "множество", "dict" : "словарь"}
    return "Это " + type_translations[type(obj).__name__]
  
