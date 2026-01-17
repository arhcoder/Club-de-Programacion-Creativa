import csv
import random

# Configuración
NUM_EJEMPLOS = 1000
RUTA_SALIDA = "data/credito.csv"

# Generamos ejemplos sin normalizar
datos = []
for _ in range(NUM_EJEMPLOS):
    edad = random.randint(10, 50)               # años
    ahorro = random.randint(500, 2500)         # saldo en pesos

    # Regla lineal base para etiqueta
    aprobado = 1 if (edad >= 18 and ahorro >= 1000) else 0

    datos.append((edad, ahorro, aprobado))

# Guardamos CSV
with open(RUTA_SALIDA, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["edad", "ahorro", "aprobado"])
    writer.writerows(datos)

print(f"✅ Archivo generado con {NUM_EJEMPLOS} ejemplos en '{RUTA_SALIDA}'")