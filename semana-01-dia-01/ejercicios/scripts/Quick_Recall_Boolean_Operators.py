##Quick Recall & Active Retrieval Session
##Boolean Operators & Conditional Statements - Core Foundations
import condition
import pandas as pd

##1️⃣ BOOLEAN OPERATORS - The Three Pillars and operator:

#Both conditions MUST be True "and operator"
name = "John"
age = 20

print(name == "John" and age >= 18) #For this code line to shows up the print I did two variables at first

# Use "or" operator. At least ONE condition must be True

name = "John"
name_1 = "Jane"

print(name == "John" or name_1 == "Jane") #True if EITHER is True

#Using "not" operator: Inverts the boolean value
is_locked = False

resultado = not is_locked

print(f"Esta bloqueado (is_locked)?: {is_locked}")
print(f"Resultado de not is_locked?: {resultado}")

#How Python evaluates this:
name = "John"
age = 20
has_permission = True

print(name == "John" and age >= 18 and has_permission)
print((name == "John") or (age >= 18) and has_permission)
print(name == "John") or ((age >= 18) and has_permission)
print(name == "John" or age >= 18) and has_permission

#3️⃣ IF STATEMENTS - Decision Making: Basic structure
# Definimos la variable correctamente
decision = True

# La condición debe evaluar la variable existente
if decision:
    # Indentación de 4 espacios (estándar PEP 8)
    print("Condition met")

#💻 Ejemplo Mínimo Viable: Buscando Nulos
#Imagina que recibes un dataset de ventas con 4 registros.




data = {
    'ID_Clientes': [101, 102, 103, 104],
    'Ventas': [250.5, None, 400.2, 150.0]
}
df = pd.DataFrame(data)

hay_nulos = df.isnull().values.any()

if hay_nulos:
    print('Alerta: se detectaron valores nulos')
    print('Acción: Iniciando proceso de limpieza (Imputacion)...')
else:
    print('Datos Limpios: El dataset esta listo para el analisis')

#ELSE and ELIF- Multiple Paths
#If-else(two paths)
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")

#If-elif-else
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(grade)


#Critical concept: Python checks conditions top-to-bottom stops at first true
score = 75

if score >= 70:
    grade = "C"
elif score >= 90:
    grade = "A"

print(grade)

resultado = "Verdadero" if condition else "Falso"
print(resultado)

compras = 1500

# Lógica ternaria: Si compras > 1000 es VIP, si no, es Normal.
categoria = "VIP" if compras > 1000 else "Normal"

print(f"El cliente es: {categoria}")