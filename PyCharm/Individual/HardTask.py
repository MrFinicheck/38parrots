#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    sentence = input("Введите предложение: ")

    # Проверить требуюемую длину.
    if len(sentence) == 0:
        print(
            "Предложение должно состоять хотя бы из одного слова",
            file=sys.stderr
        )
        exit(1)

    # Объявить переменные для подсчёта слов.
    wordStart = 0
    wordEnd = 0

    # Разделить предложение на слова.
    words = sentence.split()

    for i in words:
        if i.startswith("н"):
            # Если слово начинается с н.
            wordStart += 1
        elif i.endswith("р"):
            # Если слово оканчивается на р.
            wordEnd += 1

    # Выводим кол-во слов начинающихся с н, и кол-во слов оканчивающихся на р
    print(f"Количество слов, начинающихся с буквы н: {wordStart}\n"
          f"Количество слов, оканчивающихся буквой р: {wordEnd}")
