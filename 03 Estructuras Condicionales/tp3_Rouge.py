

# Ejercicio 1
Edad = int(input("¿Cuántos años tienes? "))
if Edad >= 18:
    print("Eres mayor de edad")





# Ejercicio 2
Nota = int(input("¿Cuál es tu nota? "))
if Nota >= 6:
    print("Aprobado")
else:
    print("Reprobado")




# Ejercicio 3
Numero = int(input("Introduce un número: "))
if Numero % 2 == 0:
    print("El número es par")
else:
    print("introduzca un número par")



# Ejercicio 4
Edad1 = int(input("¿Cuántos años tienes? "))
if Edad1 < 12:
    print("Eres un niño")
elif Edad1 >=12 and Edad1 < 18:
    print("Eres un adolescente")
elif Edad1 >= 18 and Edad1 < 30:
    print("Eres un adulto joven")
elif Edad1 >= 30:
    print("Eres un adulto")



# Ejercicio 5
contraseña = input("Introduce la contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Contraseña válida")
else:
    print("introduzca una contraseña de entre 8 y 14 caracteres")





# Ejercicio 6
import statistics
import random

# Generar una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la media, mediana y moda
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)


# Imprimir los resultados
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)


# Determinar el sesgo
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")





# Ejercicio 7

frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
    
print(frase)






# Ejercicio 8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opción (1 = mayúsculas, 2 = minúsculas, 3 = primera letra en mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")





# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")





# Ejercicio 10
hemisferio = input("Ingrese su hemisferio (N para norte, S para sur): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

# Convertimos fecha a un número para comparar fácilmente: ej. 21 de marzo → 321
fecha = mes * 100 + dia

# Definimos las estaciones según hemisferio
if hemisferio == "N":
    if 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Invierno"
elif hemisferio == "S":
    if 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Verano"
else:
    estacion = "Hemisferio no válido"

print("La estación actual es:", estacion)
