from math import pi
from numpy import array

class ProyectX():
    def __init__(self):
        self.__FechaInicio = array([22, 21, 20, 21, 21, 21, 22, 23, 24, 23, 23, 23])
        self.__SignosZodiacales = array(["Capricornio","Acuario","Piscis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario"])


    def Square(self, base, height):
        return (base * height)

    def Circle(self, radio):
        return (radio * radio) * pi

    def Triangle(self, base, height):
        return (base * height) / 2

    def Zodiaco(self, day, month):
        temp = month - 1
        if(self.__FechaInicio[month] < day):
            temp = temp + 1
        return "que eres: " + self.__SignosZodiacales[temp]

    def Factorial(self, number):
        i = result = 1
        while(number > i):
            result = result * (i + 1)
            i = i + 1
        return result


    


miClass = ProyectX()


print("Elija una opcion: ")
print("1-Cuadrado")
print("2-Triangulo")
print("3-Circulo")
print("4-Zodiaco")
print("5-Valor de 'e'")

opcion = int(input("Opcion: "))

if(opcion >= 1 and opcion <=2):
    base = int(input("Digame la base: "))
    height = int(input("Digame la altura: "))
elif(opcion == 3):
    radio = int(input("Digame cual es el radio: "))
elif(opcion == 4):
    day = int(input("Digame su dia: "))
    month = int(input("Digame su mes: "))




if(opcion == 1):
    result = miClass.Square(base, height)
elif(opcion == 2):
    result = miClass.Triangle(base, height)
elif(opcion == 3):
    result = miClass.Circle(radio)
elif(opcion == 4):
    result = miClass.Zodiaco(day, month)
elif(opcion == 5):
    limite = 100
    n = 0
    e = 0
    while n < limite:
        e += 1/miClass.Factorial(n)
        n = n + 1
    result = e

print("El resultado es: ", result)