import turtle
import math
print("¿Cuántas puntas tiene tu estrella?")
puntas=int(input())
estrella=turtle.Turtle()
pantalla=turtle.Screen()
pantalla.bgcolor("White")
estrella.speed(1) #Tiempo que tarda en dibujar en escala de 1: muy lento, 10 muy rápido
for i in range(puntas):
turtle.done()