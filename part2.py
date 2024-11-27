import math

class Vector:
    def __init__(self, coordinates):
        # Инициализация вектора с заданными координатами.
        if not isinstance(coordinates, list): # Проверяем что коодинаты переданы в виде списка
            raise ValueError("Координаты вектора должны быть переданы в виде списка.")
        if len(coordinates) == 0: # Проверяем наличии координат в списке
            raise ValueError("Координаты вектора не могут быть пустыми.")
        self.coordinates = coordinates
    
    # Метод сложения
    def __add__(self, other):
        if len(self.coordinates) != len(other.coordinates): # Проверяем размерность векторов
            raise ValueError("Сложение невозможно: векторы разной размерности.")
        return Vector([self.coordinates[i] + other.coordinates[i] for i in range(len(self.coordinates))])
    
    # Метод вычитания
    def __sub__(self, other):
        if len(self.coordinates) != len(other.coordinates): # Проверяем размерность векторов
            raise ValueError("Вычитание невозможно: векторы разной размерности.")
        return Vector([self.coordinates[i] - other.coordinates[i] for i in range(len(self.coordinates))])

    # Метод скалярного произведения
    def dot(self, other):
        if len(self.coordinates) != len(other.coordinates): # Проверяем размерность векторов
            raise ValueError("Скалярное произведение невозможно: векторы разной размерности.")
        return sum(self.coordinates[i] * other.coordinates[i] for i in range(len(self.coordinates)))

    # Метод вычисление косинуса между двумя векторами
    def cosine(self, other):
        
        dot_result = self.dot(other) # Вычисляем скалярное произведение векторов
        # Вычисляем длинны векторов
        self_len = self.norm() 
        other_len = other.norm()
        
        if self_len == 0 or other_len == 0: # Проверка на нулевую длинну
            raise ValueError("Косинус угла невозможно вычислить: один из векторов имеет нулевую длину.")
        
        return dot_result / (self_len * other_len)

    # Метод вычисление евклидовой нормы
    def norm(self):
       
        return math.sqrt(sum(x**2 for x in self.coordinates))
    # Метод строкового представления вектора
    def __str__(self):
        
        return f"Vector({self.coordinates})"

# Пример использования класса Vector
if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
         
    v3 = v1 + v2  # Сложение
    print("Сложение v1 и v2:", v3)
    
    v4 = v1 - v2  # Вычитание
    print("Вычитание v1 и v2:", v4)
    
    dot_product = v1.dot(v2)  # Скалярное произведение
    print("Скалярное произведение v1 и v2:", dot_product)
    
    cosine_value = v1.cosine(v2)  # Косинус угла
    print("Косинус угла между v1 и v2:", cosine_value)
    
    norm_v1 = v1.norm()  # Евклидова норма
    print("Длина вектора v1:", norm_v1)