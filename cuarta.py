from math import pi

class ProyectX():

    def Square(self, base, height):
        return (base * height)

    def Circle(self, radio):
        return (radio * radio) * pi

    def Triangle(self, base, height):
        return (base * height) / 2

    


miClass = ProyectX()


print("Elija una opcion: ")
print("1-Cuadrado")
print("2-Triangulo")
print("3-Circulo")
print("4-Zodiaco")
print("5-Factorial")

opcion = int(input("Opcion: "))

if(opcion >= 1 and opcion <=2):
    base = int(input("Digame la base: "))
    height = int(input("Digame la altura: "))
elif(opcion == 3):
    radio = int(input("Digame cual es el radio: "))



if(opcion == 1):
    result = miClass.Square(base, height)
elif(opcion == 2):
    result = miClass.Triangle(base, height)
elif(opcion == 3):
    result = miClass.Circle(radio)


print("El resultado es: ", result)