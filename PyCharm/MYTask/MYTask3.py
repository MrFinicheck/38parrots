#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    word = input("Введите слово: ")
    k = int(input("Введите значение k: "))

    # Проверить требуемое значение k.
    if k < 1 or k > len(word):
        print(
            "Укажите k большее нуля или k меньшее длины слова",
            file=sys.stderr
        )
        exit(1)

    # Переставить буквы.
    new_word = word[1:k] + word[:1] + word[k:]

    # Вывод модифицированного слова.
    print(f"Исправленое слово: {new_word}")





