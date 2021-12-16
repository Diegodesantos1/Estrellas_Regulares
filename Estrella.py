import turtle
import math
print("¿Cuántas puntas tiene tu estrella?")
puntas=int(input())
angulo= (puntas - 2) * 180 / puntas #Fórmula del ángulo interno de un polígono
angulo_positivo = (1 - 4/puntas) * 180 #Fórmula del ángulo interno positivo de un polígono
estrella=turtle.Turtle()
pantalla=turtle.Screen()
turtle.pensize(3) # Pongo el tamaño un poco más grueso
pantalla.bgcolor("White")
estrella.speed(1) #Tiempo que tarda en dibujar en escala de 1: muy lento, 10 muy rápido

turtle.done()