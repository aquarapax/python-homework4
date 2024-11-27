import math

class ComplexNumber:
    # Конструктор класса принимает действительную и мнимую часть 
    # или радиус и угол в полярной форме
    def __init__(self, real=0.0, imaginary=0.0, polar=False):
        if polar:  # Проверяем, если передана полярная форма
            self.r = real  # Устанавливаем радиус
            self.theta = imaginary  # Устанавливаем угол
            # Вычисляем действительную и мнимую части из полярной формы
            self.real = self.r * math.cos(self.theta) 
            self.imaginary = self.r * math.sin(self.theta)
        else:  # Если передана алгебраическая форма
            self.real = real  # Устанавливаем действительную часть
            self.imaginary = imaginary  # Устанавливаем мнимую часть
            # Вычисляем радиус и угол из алгебраической формы
            self.r = math.sqrt(real**2 + imaginary**2)  # Радиус
            self.theta = math.atan2(imaginary, real)  # Угол
   
    # Метод сложения
    def __add__(self, other):
        # Возвращаем новое комплексное число, сложив действительные и мнимые части
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    # Метод вычитания
    def __sub__(self, other):
        # Возвращаем новое комплексное число, вычитая действительные и мнимые части
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    # Метод умножения
    def __mul__(self, other):
        # Формула для умножения комплексных чисел
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,  # Действительная часть
            self.real * other.imaginary + self.imaginary * other.real  # Мнимая часть
        )

    # Метод деления
    def __truediv__(self, other):
        # Вычисляем знаменатель
        denom = other.real**2 + other.imaginary**2
        # Формула для деления комплексных чисел
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denom
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denom
        # Возвращаем новое комплексное число
        return ComplexNumber(real_part, imaginary_part)

    # Метод для получения алгебраической формы числа
    def algebraic(self):
        # Форматируем строку для алгебраической формы
        return f"{self.real} + {self.imaginary}j"

    # Метод для получения полярной формы числа
    def polar(self):
        # Форматируем строку для полярной формы
        return f"r = {self.r}, angle = {self.theta} (radians)"

    # Метод для строкового представления объекта
    def __str__(self):
        # При выводе объекта будет показана алгебраическая форма
        return self.algebraic()

# Пример использования класса
if __name__ == "__main__":
    # Создаем комплексное число в алгебраической форме
    c1 = ComplexNumber(3, 4)  
    print("Алгебраическая форма записи:", c1.algebraic())  # Выводим алгебраическую форму
    print("Полярная форма записи:", c1.polar())  # Выводим полярную форму

    # Создаем комплексное число в полярной форме
    c2 = ComplexNumber(5, math.pi / 3, polar=True)  
    print("Алгебраическая форма записи:", c2.algebraic())  # Выводим алгебраическую форму
    print("Полярная форма записи:", c2.polar())  # Выводим полярную форму

    # Выполняем операции с комплексными числами
    c3 = c1 + c2  # Сложение
    print("с1 + с2 = ", c3)

    c4 = c1 - c2  # Вычитание
    print("c1 - c2 = ", c4)

    c5 = c1 * c2  # Умножение
    print("c1 * c2 = ", c5)

    c6 = c1 / c2  # Деление
    print("c1 / c2 = ", c6)