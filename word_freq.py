"""
Программа считает Топ-100 слов для переданного ей текстого файла.
Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk
Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""
import collections
import os
import sys
from gensim.parsing.preprocessing import remove_stopwords

LIMIT = 100

def count_top_eng(file_name, limit):
    with open(file_name, "r", encoding="UTF-8") as file:
        words = []
        for line in file:
            line = remove_stopwords(line.strip().lower())
            words += line.split()

    top_list = collections.Counter(words).most_common(limit)
    print(top_list)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isfile(file_path := sys.argv[1]):
            count_top_eng(file_path, LIMIT)
        else:
            print("The file is missing")
    else:
        print("Full path to the file is missing")
