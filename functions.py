''' Функции '''

from exceptions import InvalidEmailError, InvalidPhoneNumberError, OutOfRangeError


# Шаг 1.1
def divide(a, b):
    '''Деление двух чисел'''
    if b == 0:
        raise ValueError("Ошибка деления на 0")
    return a / b


# Шаг 1.2
def root(x):
    '''Извлечение корня'''
    if x < 0:
        raise ValueError("Невозможно извлечь корень из отрицательного числа")
    return x ** 0.5


# Шаг 2
def calculate(a, b):
    '''Возвращает корень деления a на b'''
    try:
        result_divide = divide(a, b)
        result_sqrt = root(result_divide)
        return result_sqrt

    except Exception as e: # Жалуется линтер тк слишком обобщённое исключение
        return f"Ошибка: {e}"


# Шаг 3
def load_file(name, callback):
    '''
    Загружает файл
    Выбрасывает исключения при ошибке загрузки
    '''

    print(f"Файл {name} открыт")

    try:
        if len(name) <= 3 or "." not in name:
            raise UnicodeError("Ошибка загрузки")
        print(f"Файл {name} загружен")
        callback(True)

    except Exception as e:
        print(f"Ошибка: {e}")
        callback(False)
    finally:
        print(f"Файл {name} закрыт")


# Шаг 4.1
def is_palindrome(s):
    '''
    Проверка, является ли строка палиндромом
    Выбрасывает исключения при неверных входных параметрах
    '''
    try:
        if not isinstance(s, str):
            raise TypeError("Входное значение должно быть строкой")
        if len(s) == 0:
            raise ValueError("Строка не должна быть пустой")

        cleaned = ''.join(s.split()).lower()
        return cleaned == cleaned[::-1]

    except TypeError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")
    return False


# Шаг 4.2
def factorial(n):
    '''
    Факториала числа
    Выбрасывает исключения при отрицательных значениях или если входной параметр не целое число
    '''
    try:
        if not isinstance(n, int):
            raise TypeError("Входное значение должно быть целым числом")
        if n < 0:
            raise ValueError("Входное значение должно быть положительным")
        if n > 20:
            raise OverflowError("Слишком большое число")

        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    except ValueError as e:
        print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка: {e}")
    except OverflowError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")
    return 0


# Шаг 4.3
def check_age(age):
    '''
    Функция для проверки возраста
    Выбрасывает исключения при отрицательном или слишком большом возрасте
    '''
    try:
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if age > 150:
            raise ValueError("Возраст не может превышать 150 лет")

        print(f"Возраст {age} допустим")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")


# Шаг 5
def validate_levels(levels):
    '''
    Валидирует уровни
    Выбрасывает исключения при отсутствии уровней или отрицательном номере
    '''
    try:
        if len(levels) == 0:
            raise ValueError("Список уровней пуст")
        for number in levels:
            if number <= 0:
                raise ValueError("Уровень с отрицательным номером не допустим")

    except ValueError as e:
        print(f"Ошибка: {e}")


# Шаг 6.1 (7)
def validate_email(email):
    '''
    Валидирует почту
    Выбрасывает исключение при отсутствии необходимых символов в почте
    '''
    try:
        if "@" not in email or "." not in email.split("@")[-1]:
            raise InvalidEmailError("Неверный формат электронной почты")
        print("Электронная почта валидна")

    except InvalidEmailError as e:
        print(f"Ошибка: {e}")


# Шаг 6.2 (7)
def validate_phone_number(phone_number):
    '''
    Валидирует номер телефона
    Выбрасывает исключение при неправильной длине номера
    '''
    try:
        if len(phone_number) != 10:
            raise InvalidPhoneNumberError("Неверный формат номера телефона")
        print("Номер телефона валиден")

    except InvalidPhoneNumberError as e:
        print(f"Ошибка: {e}")


# Шаг 6.3 (7)
def insert(ls, value, index):
    '''
    Вставляет элемент в список
    Выбрасывает исключение при выходе за пределы списка
    '''
    try:
        if index < 0 or index > len(ls) - 1:
            raise OutOfRangeError("Выход за пределы списка")
        ls.insert(index, value)

    except OutOfRangeError as e:
        print(f"Ошибка: {e}")


# Шаг 8.1
def add_unique(ls, value):
    '''
    Добавляет уникальный элемент в список
    Выбрасывает исключение, если в списке уже существует такой элемент
    '''
    try:
        if value in ls:
            raise ValueError("Элемент уже существует")
        ls.append(value)

    except ValueError as e:
        print(f"Ошибка: {e}")


# Шаг 8.2
def convert_to_int(value):
    '''
    Конвертирует значение в число
    Выбрасывает ошибку при невозможности конвертации
    '''
    try:
        if not can_convert_to_int(value):
            raise ValueError("Конвертация невозможна")
        return int(value)

    except ValueError as e:
        print(f"Ошибка конвертации: {e}")


# Шаг 8.3
def can_convert_to_int(value):
    '''Проверка на возможность конвертировать в int'''
    try:
        int(value)
        return True
    except ValueError:
        return False
