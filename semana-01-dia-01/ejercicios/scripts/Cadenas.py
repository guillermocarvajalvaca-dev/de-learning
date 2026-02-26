#Sesión de Entrenamiento: Dominio de Cadenas (Repetición 1)

#Enfoque: Control del Espacio y la Multiplicación.
#El error común a eliminar: Olvidar que Python no agrega espacios automáticamente
#y que multiplicar cadenas es literal (sin separadores).

#Suma (+): Pega dos cosas exactamente como están. Si no hay espacio en la variable, no habrá espacio en el resultado.
#Multiplicación (*): Repite la cadena exactamente como es. "Gol" * 3 es "GolGolGol". Si quieres "Gol Gol Gol",
#debes multiplicar "Gol".

#Ejercicio 1: El Cantico de la Hinchada

#Tiene dos variables base. Tu misión es construir una frase exacta usando
#repetir y concatenación para unir.

prefix = "Hip "
suffix = "Hurra"

chant = prefix * 3 + suffix
print(chant)

#Repetición 2 (Precisión Quirúrgica)

#Enfoque: Slicing (Rebanado de Datos). El músculo a entrenar:
# La capacidad de extraer un dato específico "enterrado" dentro de una cadena más larga.
# Esto es el "pan de cada día" en Data Science (limpiar columnas sucias).

#🧠 La Lógica (Tu técnica de bisturí)
#El slicing usa la sintaxis [inicio: fin].
#Inicio (Inclusive): El índice donde empiezas a cortar. (Recuerda: Python cuenta desde 0).
#Fin (Exclusive): El índice donde te detienes. Ojo aquí: Python se detiene antes de tocar este índice.
#Si quieres la letra en la posición 5, tu fin debe ser 6.


#🏋️ Ejercicio 2: Extracción de ID
#Imagina que recibes un lote de códigos de productos sucios.
# Todos siguen el formato CATEGORIA_ID_VERSION. Tu jefe solo quiere el número del medio.

sku = "ITEM_5678_V20"
product_id = sku [5:9]
print(product_id)


#🔥 Sesión de Entrenamiento: Repetición 3 (Agilidad Dinámica)

#Enfoque: F-Strings con Transformación "In-Place" (En el sitio).
#El músculo a entrenar:No solo inyectar datos, sino procesarlos justo antes de mostrarlos.
#En Data Science, los datos crudos suelen venir "sucios"
#(todo minúsculas, espacios extra). Tienes que limpiarlos al vuelo para el reporte.

#Ya sabes que f"Hola {nombre}" inyecta el nombre.
# Pero las llaves {} son pequeños entornos de ejecución. Puedes ejecutar código de Python ahí dentro.
#En lugar de crear una variable nueva para convertir a mayúsculas y luego imprimirla...
#Haces la transformación dentro de la f-string: f"Hola {nombre.upper()}".
#Ahorras memoria y líneas de código. Eficiencia pura.

#🏋️ Ejercicio 3: El Log del Sistema
#Estás construyendo un sistema de logs que registra qué archivos se están procesando.
#El nombre del archivo viene en minúsculas, pero el estándar del log exige que se vea en MAYÚSCULAS para resaltar.

file_name = "data_analysis_2025.csv"
print(f"STATUS: Processing {file_name.upper()}...")


#🔥 Sesión de Entrenamiento: Repetición 4 (El Combo Final)
#Enfoque: Integración Total (Slicing + Métodos + F-Strings). Nivel: Élite.
#Escenario: Tienes un código de empleado sucio que mezcla letras y números.
#Necesitas extraer el nombre, corregir su formato (Capitalizar: primera mayúscula, resto minúscula) y presentarlo en una credencial.

raw_data = "EMP_guillermo_007"
slice_guillermo = raw_data[4:13]
print(f"Credential generated for: {slice_guillermo.capitalize()}")
