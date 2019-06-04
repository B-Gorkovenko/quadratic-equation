import math
a = int(input("Введите значение a = "))
b = int(input("Введите значение b = "))
c = int(input("Введите значение c = "))
class Equation:
    def __init__(self,a,b,c):
        d = b**2-4*a*c #вычисление дискриминанта
        if d < 0: #проверка дискриминанта
            print("Нет корней")
        else:
            x1 = (-b + math.sqrt(d))/(2*a) #первый корень
            print("Первый корень равен: " + str(x1))
            x2 = (-b - math.sqrt(d))/(2*a) #второй корень
            print("Второй корень равен: " + str(x2))
s = Equation(a,b,c)#создание объекта, его инициализация

