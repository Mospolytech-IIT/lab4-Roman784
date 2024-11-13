'''Точка входа'''

from functions import (
    divide, root, calculate, load_file,
    is_palindrome, factorial, check_age,
    validate_levels, validate_email,
    validate_phone_number, insert,
    add_unique, convert_to_int, can_convert_to_int)


def run():
    '''Запуск вссех функций'''
    try:
        print("Шаг 1.1:")
        print(divide(10, 2))
        print(divide(10, 0))
    except ValueError as e:
        print(f"Необработанная ошибка: {e}")

    try:
        print("\nШаг 1.2")
        print(root(16))
        print(root(-4))
    except ValueError as e:
        print(f"Необработанная ошибка: {e}")

    try:
        print("\nШаг 2")
        print(calculate(10, 2))
        print(calculate(10, 0))
        print(calculate(-10, 2))

        print("\nШаг 3")
        load_file("file1.txt", lambda res: print(f"Результат загрузки: {res}"))
        load_file("file2", lambda res: print(f"Результат загрузки: {res}"))

        print("\nШаг 4.1")
        print(is_palindrome("Aboba"))
        print(is_palindrome(""))
        print(is_palindrome(123))

        print("\nШаг 4.2")
        print(factorial(5))
        print(factorial(-1))
        print(factorial(5.5))
        print(factorial(21))

        print("\nШаг 4.3")
        check_age(30)
        check_age(-5)
        check_age(200)

        print("\nШаг 5")
        validate_levels([1, 2, 3])
        validate_levels([])
        validate_levels([1, -2, 3])

        print("\nШаг 6.1 (7)")
        validate_email("rmiro@gmail.com")
        validate_email("rmiro.com")

        print("\nШаг 6.2 (7)")
        validate_phone_number("1234567890")
        validate_phone_number("12345")

        print("\nШаг 6.3 (7)")
        my_list = [1, 2, 3]
        insert(my_list, 4, 1)
        print(my_list)
        insert(my_list, 5, 5)

        print("\nШаг 8.1")
        my_list = [1, 2, 3]
        add_unique(my_list, 4)
        print(my_list)
        add_unique(my_list, 4)

        print("\nШаг 8.2")
        print(convert_to_int("1"))
        print(convert_to_int("a"))

        print("\nШаг 8.3")
        print(can_convert_to_int("1"))
        print(can_convert_to_int("a"))

    except Exception as e:
        print(f"Необработанная ошибка: {e}")


if __name__ == "__main__":
    run()
