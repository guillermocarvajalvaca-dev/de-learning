

#Operador Modulo (%)
# ¿Qué hace? → Devuelve el RESTO de una división

camiseta = 24 #Asigna el valor 24 a la variable camiseta
residuo = camiseta % 2  #Divide 24 entre 2, guarda el RESTO (0 porque 24÷2=12 exacto)
print(f"Es la camiseta {camiseta} par? (0=Si 1=NO):", residuo) #Muestra el resultado usando f-string

#Regla: Si numero % 2 == 0 → es PAR, si es 1 → es IMPAR

# División de jugadores en equipos

jugadores = 50 #Total de jugadores
equipos = 3 #Cantidad de equipos
jugadores_sobrantes = jugadores % equipos #50÷3=16 equipos completos, SOBRAN 2 jugadores
print("Si hago 3 equipos con 50 jugadores, sobran:", jugadores_sobrantes) #Muestra cuántos jugadores no entraron en equipos completos

# Output: Si hago 3 equipos con 50 jugadores, sobran: 2


# Convertir días totales en semanas completas + días sobrantes

dias = 100 #Total de días
semana = 7 #Días por semana
dias_sobrantes = dias % semana #100÷7=14 semanas, RESTO=2 días
print("Si divido 100 dias en semanas de 7 dias, cuantos dias sobran:", dias_sobrantes)
#El % te da los días que NO completan una semana más
# Output: Si divido 100 días en semanas de 7 días, cuantos dias sobran: 2

# 100 ÷ 7 = 14 semanas completas, SOBRAN 2 días

# Verifica si los siguientes números son pares o impares
numeral = 156
residuo = numeral % 2
print(f"El numeral {numeral} es par? (0=Si 1=NO):", residuo)
# TODO: Calcula el residuo y muestra si es par (0) o impar (1)

numeral_2 = 89
residuo_2 = numeral_2 % 2
print(f"El numeral 2 es impar? (0=Si 1=NO):)", residuo_2)
# TODO: Calcula el residuo y muestra si es par (0) o impar (1)

numeral_3 = 1024
residuo_3 = numeral_3 % 2
print(f"El numeral 3 {numeral_3} es par? (0=Si 1=NO):", residuo_3)
# TODO: Calcula el residuo y muestra si es par (0) o impar (1)

###DIVISIVIBILAD POR 3

#Verifica si estos numeros son divisilbles por 3

numero1 = 45
divisible_1 = numero1 % 3
print(f"El numero1 {numero1} es divisible? (0=Si otro numero=NO):", divisible_1)
#Todo:usa % 3 y muestra si es divisible (0) o no (otro numero)

numero2 = 50
divisible_2 = numero2 % 3
print(f"El numero2 {numero2} es divisible? (0=Si Otro numero=No):", divisible_2)
#Todo:usa % 3 y muestra si es divisible (0) o no (otro numero)

numero3 = 99
divisible_3 = numero3 % 3
print(f"El numero3 {numero3} es divisible? (0=Si Otro numero=No):", divisible_3)
#Todo:usa % 3 y muestra si es divisible (0) o no (otro numero)

##Ejercicio:Repartir Caramelos

# Tienes 47 caramelos y 5 niños
# ¿Cuántos caramelos sobran si repartes equitativamente?

caramelos = 47
ninos = 5
caramelos_sobrantes = caramelos % ninos
print(f"Cuantos caramelos sobran si reparto en cantidades iguales los caramelos a los ninos = {caramelos_sobrantes} caramelos")

# TODO: Calcula cuántos caramelos SOBRAN usando %
# TODO: Muestra el resultado con un mensaje claro

# Tienes un proyecto de 365 días
# ¿En cuántas semanas completas se divide y cuántos días sobran?

dias_proyectos = 365
dias_semanas = 7
semanas_completas = dias_proyectos // dias_semanas
dias_sobrantes = dias_proyectos % dias_semanas
print("Cuantos dias sobran en el proyecto si cuento las semanas completas:", dias_sobrantes)
# TODO: Calcula las semanas COMPLETAS (usa //)
# TODO: Calcula los días SOBRANTES (usa %)
# TODO: Muestra ambos resultados con f-strings


# Crea un verificador que muestre:
# - Si el número es par o impar
# - Si es divisible por 5
# - Si es divisible por 10

numero = 100
residuo_par = numero % 2
residuo_5 = numero % 5
residuo_10 = numero % 10
print(f"El numero {numero} es par? (0=Si 1=NO):", residuo_par)
print(f"El numero {numero} es par? (0=Si 1=NO):", residuo_5)
print(f"El numer {numero} es par? (0=Si 1=NO):", residuo_10)
# TODO: Calcula residuo_par (% 2)
# TODO: Calcula residuo_cinco (% 5)
# TODO: Calcula residuo_diez (% 10)
# TODO: Muestra los 3 resultados