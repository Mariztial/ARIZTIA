# -*- coding: utf-8 -*-
"""Tarea 02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i1OvHa0PLx0YbQpbxzO5P3pGfbSoU7oO

Ejercicio 1
"""

for x in range(100):
  print(x+1)

"""Ejercicio 2"""

for x in range(100):

  if(x+1) % 3 == 0:
    print(x+1)

"""Ejercicio 3"""

numero_1 = int(input("Ingresa un número"))
numero_2 = 5
suma = numero_1 + numero_2
resultado = ""

if(suma<100):
  resultado = "menor a 100"
elif(suma>=100 and suma<150):
  resultado = "mayor a 100"
elif(suma>=150):
  resultado = "mayor a 150"

print(resultado)

"""Ejercicio 4"""

edad = int(input())
if edad >= 18:
  print("bienvenido, eres mayor de edad")
  print("¿Te gusta programar?")
  a = input()
  if a == "si":
    print("Bien!, unete al grupo")
  if a != "si":
    print("buuu aburrido!")
else:
  print("no cumples con la edad necesaria")