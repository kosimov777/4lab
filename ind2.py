# Дано предложение. Определить количество букв н, предшествующих первой запятой предложения.
# Рассмотреть два случая: известно, что запятые в предложении есть; запятых в предложении может не быть.

# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentense = input("Введите предложение: ")
    comma = int(input("Есть ли в предложении запятые? Ввделите 1 или 0: "))

    cout = sentense.find(",")
    if comma == 0:
        print("0")
    elif comma == 1:
        print(sentense.count("н", 0, cout))
