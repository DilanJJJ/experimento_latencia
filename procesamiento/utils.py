import time
import random

def simular_procesamiento(archivo_path):
    # Simula un procesamiento de datos con un retardo de entre 1 y 2 minutos
    tiempo_procesamiento = random.uniform(60, 120)
    time.sleep(tiempo_procesamiento / 10)  # Reducimos el tiempo para prueba
    return f'Procesamiento simulado completado en {tiempo_procesamiento:.2f} segundos para {archivo_path}'