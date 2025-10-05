class Roman:
    # соответствие римских и арабских чисел
    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    int_to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(self, value):
        # можно передавать как int, так и строку
        if isinstance(value, int):
            self.value = value
        elif isinstance(value, str):
            if value.upper() == 'N':   # поддержка "нуля"
                self.value = 0
            else:
                self.value = self.roman_to_int(value)
        else:
            raise TypeError("Аргумент должен быть int или str")

    # Статические методы для преобразования
    @staticmethod
    def roman_to_int(roman: str) -> int:
        result = 0
        prev_value = 0
        for char in reversed(roman.upper()):
            value = Roman.roman_to_int_map[char]
            if value < prev_value:
                result -= value
            else:
                result += value
                prev_value = value
        return result

    @staticmethod
    def int_to_roman(number: int) -> str:
        if number <= 0:
            raise ValueError("Римские числа должны быть положительными")
        result = ""
        for val, sym in Roman.int_to_roman_map:
            while number >= val:
                result += sym
                number -= val
        return result

    # Операции
    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value + other.value)
        return Roman(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value - other.value)
        return Roman(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value * other.value)
        return Roman(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value // other.value)
        return Roman(self.value // other)

    def __str__(self):
        return self.int_to_roman(self.value)

    def __repr__(self):
        return f"Roman('{self.int_to_roman(self.value)}')"

a = Roman("M")
b = Roman("V")

print(a + b)
print(a - b)
print(a * b)
print(a / b)