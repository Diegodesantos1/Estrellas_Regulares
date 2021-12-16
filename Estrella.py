import turtle
print("¿Cuántas puntas tiene tu estrella?")
puntas=int(input())

angulo= 360//puntas
print(angulo)
estrella=turtle.Turtle()
pantalla=turtle.Screen()
pantalla.bgcolor("White")
estrella.speed(1) #Tiempo que tarda en dibujar en escala de 1: muy lento, 10 muy rápido
for i in range(puntas): #Solo funciona para la estrella de 5 puntas
    estrella.left(144)
    estrella.forward(100)
turtle.done()