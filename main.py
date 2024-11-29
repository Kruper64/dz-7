numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('before', numbers)

def set_up_pow(value: int, result=0, operation="**"):
    result = 0
    delim = 2
    def up_pow(n):
        if n % delim != result:
            return n**value
        return n
    def multiplication(n):
        if n % delim != result:
            return n*value
        return n
    def division(n):
        try:
            if n % delim != result:
                rez_operation = n/value
                return rez_operation
            return n
        except ZeroDivisionError as error:
            print(f'error info: {error} {n}')
            rez_operation = 0
            return rez_operation

    def subtraction(n):
        if n % delim != result:
            return n-value
        return n

    if operation == "**":
        return up_pow
    elif operation == "*":
        return multiplication
    elif operation == "/":
        return division
    elif operation == "-":
        return subtraction
def check_n(n):
    return n >= 5

def StrToFloatOrInt(number_str: str, operation: str = "float"):
    try:
        print(f'--->>> конвертація типу данних str в float, значення {number_str}')
        try:
            if operation == "float":
                return float(number_str)
            else:
                return int(number_str)
        except:
            raise TypeError(f'помилка конвертації')

    except TypeError as error:
        print(f'{error}')
        return 0
    except:
        print(">>>>>error")
        return 0
    finally:
        print(">>>>>конвертація завершено!")

b = input("введіть значення зміної b = ")
#b = StrToFloatOrInt(b,"int")
b = StrToFloatOrInt(b,"float")

#up_square = set_up_pow(2,0,"**")
up_cube = set_up_pow(b, 1,"**")
multiplication = set_up_pow(b, 0,"*")
division = set_up_pow(b, 0,"/")
subtraction = set_up_pow(b, 0,"-")

print(f'-->>> Зведення у ступінь {b}: ')
numbers_square = [up_cube(n) for n in numbers if check_n(n)]
print('after', numbers_square)
print(f'-->>> Множення на {b}: ')
numbers_square = [multiplication(n) for n in numbers if check_n(n)]
print('after', numbers_square)
print(f'-->>> Ділення на {b}: ')
numbers_square = [division(n) for n in numbers if check_n(n)]
print('after', numbers_square)
print(f'-->>> Віднімання {b} з числа: ')
numbers_square = [subtraction(n) for n in numbers if check_n(n)]
print('after', numbers_square)