#Este es el inicio de un entrenamiento de elite como se debe y lo hacen los grandes
#Asi que esto nos permitirá llegar a dominarlo de manera tal que serás muy deseado en las mejores empresas.
#Con esta skill serás de los pocos que sin mirar podrán de manera automática como caminar o respirar, hacer un proyecto
#en su totalidad.
#from encodings.punycode import generate_generalized_integer

#1.- Escenario: El Inversionista de Wall Street
type_str = "empresa sofia"
type_float = 55.20
type_integer = 115
es_mayor_de_edad = True
tiene_licencia = False

#Imprimo la visualización de los tipos de datos que he creado más arriba
print(type(type_float))
print(type(type_integer))
print(type(type_str))
print(type(es_mayor_de_edad))
print(type(tiene_licencia))

#2.- Escenario: Científico de Datos (Clima)
ciudad = "Santa Cruz"
temperatura = 36.06
humedad_porcentaje = 45, "%"
alerta_lluvia = True

convert_to_integer = int(temperatura)
print(convert_to_integer)
print("En la ciudad de", ciudad,
        "tenemos la temperatura a", temperatura, "grados centígrados",
         "con una humedad que ronda a:",humedad_porcentaje,
          "los servicios meteorológicos de la ciudad pronostican lluvias")

#2.- Escenario: Tu perfil de campeón
#Creacion de Variables
nombre = "Jose Guillermo Carvajal Vaca"
edad = 37
meta_2026 = "Convertirme en master en python para ciencia de datos y obtener un mejor trabajo"
nivel_motivacion = 10
print("Hola mi nombre es", nombre, "y mi edad es", edad, "y mi meta es", meta_2026,
      "y me encuentro con una motivacion de", nivel_motivacion)

#2. Circuito 1: Variables y Tipos (Calentamiento)

#OBJETIVO: Que tus dedos aprendan a crear cajas y saber que hay adentro sin dudar.

#Repeticion Adicional #1
nombre_jugador = "Jose Guillermo Carvajal Vaca"
numero_camiseta = 5
promedio = 0.310
es_activo = False

print(type(nombre_jugador))
print(type(numero_camiseta))
print(type(promedio))
print(type(es_activo))

#Circuito 2: Asignación Aumentada (El Swing)
#Objetivo:Entender como actualizar un valor sobre la marcha, igual que ajustas el bate en medio del swing.

carreras = 0
print("inicio:", carreras)

#Inning 1: Home run (suma 1)
carreras += 1
print("Inning 1:", carreras)

#Inning 3: Grand Slam (suma 4)
carreras += 4
print("Inning 3", carreras)

#Revision de video (Resta 1 carrera anulada)
carreras -= 1
print("Decision arbitral:", carreras)

# Final del partido (Multiplica por 2 por bono de victoria - inventado)
carreras *= 2
print("Puntaje final.", carreras)

#2.2. Repeticiones de una serie de ejercicios en un GYM

repeticiones = 0
print("inicio:", repeticiones)

#Repeticion 1: Empiezo (suma 10)
repeticiones += 10
print("Primer Rep:", repeticiones)

#Repeticion 3: Incrementa la intensidad (suma 12)
carreras += 12
print("Tercer Rep 3", repeticiones)

#Revision de consistencia del ejercicio (Resta 2 carrera anulada)
carreras -= 2
print("Volver a repetir consistentemente el ejercicio:", repeticiones)

# Final del partido (Multiplica por 2 por bono de victoria - inventado)
repeticiones *= 2
print("Puntaje final.", repeticiones)

#Circuito 3: Operadores y Módulo (Lógica de Juego)
#Objetivo: Usar el operador % (Modulo) tan natural como saber si una bola es "strike" o "bola"

#Caso A: Camiseta 24
camiseta = 24
residuo = camiseta % 2
print("Es la camiseta 24 par? (0=Si, 1=No):", residuo)

#Caso B: Camiseta 77
camiseta = 77
residuo = camiseta % 2
print("Es la camiste 77 par? (0=Si, 1=No):", residuo)

#Caso C: Division de Equipos
jugadores = 50
equipos = 3
jugadores_sobrantes = jugadores % equipos
print("Si hago 3 equipos con 50 jugadores, sobran:", jugadores_sobrantes)

#calculo de dias
dias = 100
semana = 7
dias_sobrantes = dias % semana
print("Si divido los dias en semana de 7 dias, cuantos dias sobran:", dias_sobrantes)

#Circuito 4: Comparaciones y Logica Booleana (El Umpire)
#Objetivo: Ser el arbitro. Decidir True o False sin dudar

#Reglas del Gym
peso_actual = 80.5
meta = 75.0
lesionado = False

#Estoy en mi peso ideal?
en_peso = peso_actual == meta
print("Llegue a la meta?", en_peso)

#¿Puedo entrenar? (Debo pesar más de 50 kg Y NO estar lesionado)
puedo_entrenar = (peso_actual > 50) and (not lesionado)
print("Puedo entrenar hoy?", puedo_entrenar)

#¿Debo hacer dieta? (Si peso más que la meta)
hacer_dieta = peso_actual > meta
print("Toca hacer dieta?", hacer_dieta)

#Round 5: El gancho final
peso_producto = 12.5
#¿Está entre 10 y 15? La forma elegante de Python:
pasa_control = 10 < peso_producto < 15
print("El producto pasa el control de calidad?:", pasa_control)

#Serie 1: Manipulación y Conversión de Tipos
#Objetivo: Tienes dos precios que llegaron como pretexto desde una base de datos
#Tienes que sumarlos matemáticamente, no concatenarlos.


precio_a = 150.50
precio_b = 49.99

# TU MISIÓN:
# 1. Convierte ambos a float.
# 2. Súmalos.
# 3. Convierte el resultado a entero (int) para eliminar los centavos.
# 4. Imprime el resultado final.

total_float = float(precio_a) + float(precio_b)
total_entero = int(total_float)
print("Total redondeado hacia abajo:", total_entero)

#Explicación: Si no conviertes primero (float()),
# Python uniría los textos como "150.5049.99". Al final,
# int() corta los decimales sin piedad (no redondea, trunca).

#Serie 2: Aritmética Avanzada (Módulo y División Entera)
#Dominar el tiempo y los residuos. Vital para análisis de series temporales.

#Ejercicio 2: "El Reloj Digital"
#Tienes un total de segundos (ej. 3750) y necesitas mostrarlo como horas, minutos y segundos.

total_segundos = 3750

# TU MISIÓN:
# Usa // para sacar las partes enteras y % para lo que sobra.

# --- SOLUCIÓN --
horas = total_segundos // 3600
segundos_restantes = total_segundos % 3600

minutos = segundos_restantes // 60
segundos_finales = segundos_restantes % 60

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos", segundos_finales)

#Explicación: Es un sistema de cascada.
#Primero sacas los bloques grandes (horas),
#y con el residuo (%) calculas los bloques medianos (minutos).

#Serie 3: Asignación Aumentada (Gestión de Estado)
#Objetivo:Simular un proceso financiero acumulativo

#Ejercicio 3: "La Cuenta Bancaria"
#Empiezas con saldo positivo.
#Simula una serie de transacciones usando SOLO operadores aumentados (+=, -=, *=).

saldo = 1000.0
print("Saldo Inicial:", saldo)

# TU MISIÓN:
# 1. Recibes nómina: Suma 2500.
saldo += 2500

#Pagas alquiler:Restar 800
saldo -= 800

# 3. Inversión rinde frutos: Multiplica tu saldo actual por 1.05 (5% de interés).
saldo *= 1.05

#4. Compras comida: Resta 150.
saldo -= 150

print("Saldo Final:", saldo)

#Explicación: Observa cómo saldo cambia de identidad en cada línea.
#En Data Science, esto se usa para "acumuladores" dentro de bucles de millones de datos.

#Serie 4: Lógica Booleana Compleja
#Objetivo: Crear filtros de seguridad multicriterio.

#Ejercicio4: "El sistema de seguridad"
#Para que una alarma se active, deben cumplirse condiciones específicas.

movimiento_detectado = True
es_de_noche = False
puerta_abierta = True
sistema_armado = True

# TU MISIÓN:
# La alarma suena SI:
# (El sistema está armado) Y ((Hay movimiento Y es de noche) O (La puerta está abierta))

# --- SOLUCIÓN ---
alarma_suena = sistema_armado and ((movimiento_detectado and es_de_noche) or puerta_abierta)

print("Suena la alarma?", alarma_suena)


#Explicación: Los paréntesis son vitales aquí.
#(movimiento y noche) es un bloque.
#puerta_abierta es otro disparador independiente.
#sistema_armado es el interruptor maestro que debe ser True para que cualquier otra cosa importe.

#🔬 Serie 5: Comparaciones Encadenadas y Científicas
#Objetivo:Validar datos dentro de rangos normales

#Ejercicio 5:"Signos Vitales"
#Un paciente está estable si su oxigenación está entre 95 y 100.

oxigeno_paciente = 97
ritmo_cardiaco = 110

# TU MISIÓN:
# 1. Verifica si el oxigeno está en rango normal (usando cadena: 95 <= x <= 100).
# 2. Verifica si el ritmo cardiaco es peligroso (menor a 60 O mayor a 100).

# --- SOLUCIÓN ---
oxigeno_normal = 95 <= oxigeno_paciente <= 100
ritmo_cardiaco = ritmo_cardiaco < 60 or ritmo_cardiaco > 100

print("Oxigeno estable?", oxigeno_normal)
print("Ritmo cardiaco alerta?", ritmo_cardiaco)

#Explicación: Python es de los pocos lenguajes que permite escribir
#95 <= x <= 100 tal cual lo piensas matemáticamente.

#🔄 Serie 6: Intercambio de Variables (El Truco Clásico)
#Objetivo: Mover datos sin perderlos.

#Ejercicio 6: "El Swap"
#Tienes vino en la copa de agua y agua en la copa de vino. Intercámbialos.

copa_vino = "Agua"
copa_agua = "Vino"

# TU MISIÓN:
# Intercambia los valores para que copa_vino tenga "Vino" y copa_agua tenga "Agua".
# Hazlo en UNA SOLA LÍNEA (Python Magic).

# --- SOLUCIÓN ---
copa_vino, copa_agua = copa_agua, copa_vino

print("Copa de vino contiene:", copa_vino)
print("Copa de agua contiene:", copa_agua)

#Explicación: En otros lenguajes necesitas una tercera variable temporal.
#Python permite asignación múltiple simultánea. ¡Es un movimiento ninja! 🥷

#🚀 Serie 7: El Desafío Final (Cálculo de Interés Compuesto)
#Objetivo: Usar potencias y paréntesis correctamente.

#Ejercicio 7: "Tu dinero en 10 años"Fórmula: $Monto = Principal \times (1 + tasa)^{años}$
dinero_inicial = 5000
tasa_interes = 0.07 #7% anual
anios = 10

# TU MISIÓN:
# Traduce la fórmula matemática a Python usando ** para la potencia.

# --- SOLUCIÓN ---
monto_final = dinero_inicial * (1 + tasa_interes) ** anios
print("Dinero final:", monto_final)

#Explicación: El orden de operaciones (PEMDAS) es crítico.
#Primero el paréntesis (1+tasa), luego la potencia **, y al final la multiplicación *.