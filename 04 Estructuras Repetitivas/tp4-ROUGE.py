# Ejercicio 1

# Imprime los números del 0 al 100, uno por línea
for i in range(101):
    print(i)



# Ejercicio 2

# Solicita un número entero al usuario
numero = int(input("Ingresá un número entero: "))

# Convierte el número a positivo por si es negativo
numero = abs(numero)

# Convierte el número a cadena y cuenta los dígitos
cantidad_digitos = len(str(numero))


print("El número tiene", cantidad_digitos, "dígitos.")





# Ejercicio 3

# Pide dos números al usuario
inicio = int(input("Ingresá el primer número: "))
fin = int(input("Ingresá el segundo número: "))

# Asegura que el inicio sea menor que el fin
if inicio > fin:
    inicio, fin = fin, inicio

# Suma los números entre los dos valores, excluyéndolos
suma = 0
for i in range(inicio + 1, fin):
    suma += i


print("La suma de los números entre", inicio, "y", fin, "es:", suma)




# Ejercicio 4

# Inicializa la suma acumulada
suma = 0

# Bucle para pedir números hasta que se ingrese un 0
while True:
    numero = int(input("Ingresá un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero


print("La suma total es:", suma)




# Ejercicio 5

import random

# Genera un número aleatorio entre 0 y 9
secreto = random.randint(0, 9)
intentos = 0
adivino = False

print("Adiviná el número del 0 al 9!")

# Bucle hasta que el usuario adivine
while not adivino:
    intento = int(input("Ingresá tu intento: "))
    intentos += 1

    if intento == secreto:
        adivino = True
    else:
        print("¡Incorrecto! Probá de nuevo.")


print("¡Bien ahí! Adivinaste el número en", intentos, "intento(s).")




# Ejercicio 6

# Imprime los números pares del 100 al 0 en orden decreciente
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)






# Ejercicio 7

# Pide al usuario un número entero positivo
limite = int(input("Ingresá un número entero positivo: "))

# Verifica que sea positivo
if limite < 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(1, limite):
        suma += i
    print("La suma de los números entre 0 y", limite, "es:", suma)






# Ejercicio 8

# Cantidad de números a ingresar
cantidad_numeros = 100

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Bucle para ingresar los números
for i in range(cantidad_numeros):
    num = int(input(f"Ingresá el número {i+1}: "))

    # Par o impar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Positivo o negativo
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1


print("\nResultados:")
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)







# Ejercicio 9


# Cantidad de números a ingresar 
cantidad_numeros = 100

# Acumulador de la suma
suma = 0

# Bucle para ingresar los números
for i in range(cantidad_numeros):
    num = int(input(f"Ingresá el número {i+1}: "))
    suma += num

# Cálculo de la media
media = suma / cantidad_numeros


print("\nLa media de los", cantidad_numeros, "números es:", media)





# Ejercicio 10

# Pide un número al usuario
numero = input("Ingresá un número: ")

# Invierte los dígitos
numero_invertido = numero[::-1]


print("Número invertido:", numero_invertido)
