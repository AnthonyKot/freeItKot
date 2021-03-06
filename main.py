# импортируем из модуля дата_и_время объект, который умеет работать с текущей датой и временем
from datetime import datetime


# 5 строчек нашего кода, который проверяет текущую минуту на нечетность (odd)
def check_minute():
    # лист всех нечетные числа от 1 до 60 - https://catonmat.net/tools/generate-odd-numbers
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
            21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
            41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

    # переменная для сохранения текущей минуты
    right_this_minute = datetime.today().minute

    # самая популярная конструкция - оператор ветвления (обратите внимание на двоеточие и отступы)
    if right_this_minute in odds:
        # если данная минута содержится в листе нечетных чисел, значит мы печатаем это ("Эта минута немного странная")
        print("This minute seems a little odd.")
    else:
        # иначе четная
        print("Not an odd minute.")


# питонячий аналог main из других языков, что бы можно было нашу единственную функцию дергать из консоли
# python main.py
if __name__ == '__main__':
    check_minute()
