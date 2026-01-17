# PERCEPTRÓN SIMPLE: Clasificador de Mayores de Edad

import random

# ========== DATOS DE ENTRENAMIENTO ==========
# Lista de edades (entrada)
edades = [15, 16, 17, 17, 18, 19, 20, 21, 22, 25, 30, 14, 13, 18, 19, 20, 17, 16, 23, 24]

# Lista de clases (salida esperada): 0 = menor, 1 = mayor de edad
clases = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1]

# ========== NORMALIZACIÓN ==========
# Dividir edades entre 40 para tener valores entre 0 y 1
edades_normalizadas = [edad / 40.0 for edad in edades]

# ========== FUNCIÓN DE ACTIVACIÓN ==========
def activacion(peso, edad, bias):
    """
    Función que decide si activar o no el perceptrón
    z = peso * edad + bias
    Si z > 0 -> retorna 1 (mayor de edad)
    Si z <= 0 -> retorna 0 (menor de edad)
    """
    z = peso * edad + bias
    if z > 0:
        return 1
    else:
        return 0

# ========== INICIALIZACIÓN ==========
# Peso aleatorio entre -1 y 1
peso = random.uniform(-1, 1)
# Bias (sesgo) aleatorio entre -1 y 1
bias = random.uniform(-1, 1)

print(f"Peso inicial: {peso:.3f}")
print(f"Bias inicial: {bias:.3f}\n")

# ========== PARÁMETROS DE ENTRENAMIENTO ==========
tasa_de_aprendizaje = 0.1  # Qué tan rápido aprende
epocas = 100               # Cuántas veces repasará todos los datos

# ========== ENTRENAMIENTO ==========
print("=== INICIANDO ENTRENAMIENTO ===\n")

for epoca in range(epocas):
    errores = 0  # Contador de errores en esta época
    
    # Recorrer cada ejemplo de entrenamiento
    for i in range(len(edades_normalizadas)):
        edad = edades_normalizadas[i]
        clase_real = clases[i]
        
        # Hacer predicción
        prediccion = activacion(peso, edad, bias)
        
        # Calcular error
        error = clase_real - prediccion
        
        # Si hay error, ajustar pesos
        if error != 0:
            peso = peso + tasa_de_aprendizaje * edad * error
            bias = bias + tasa_de_aprendizaje * error
            errores += 1
    
    # Mostrar progreso cada 10 épocas
    if epoca % 10 == 0:
        precision = 100 * (1 - errores / len(edades))
        print(f"Época {epoca}: Precisión = {precision:.1f}% (Errores: {errores})")

print(f"\n=== ENTRENAMIENTO COMPLETADO ===")
print(f"Peso final: {peso:.3f}")
print(f"Bias final: {bias:.3f}\n")

# ========== FUNCIÓN DE PREDICCIÓN ==========
def predecir_mayor_de_edad(edad):
    """
    Predice si una persona es mayor de edad
    """
    edad_normalizada = edad / 40.0
    resultado = activacion(peso, edad_normalizada, bias)
    
    if resultado == 1:
        print(f"Edad {edad}: MAYOR DE EDAD ✓")
    else:
        print(f"Edad {edad}: MENOR DE EDAD ✗")
    
    return resultado

# ========== PRUEBAS ==========
print("=== PROBANDO EL PERCEPTRÓN ===\n")

# Casos de prueba
pruebas = [15, 17, 18, 19, 25, 30, 12, 21]

for edad_prueba in pruebas:
    predecir_mayor_de_edad(edad_prueba)

print("\n=== FIN ===")