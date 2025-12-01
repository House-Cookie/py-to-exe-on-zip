import os
import time

# Nombre del archivo de registro a "atacar"
nombre_archivo = "registro_galletas.log"
# El "arma": una línea que no sirve para nada, como exceso de mantequilla.
linea_basura = "ADVERTENCIA: ¡Exceso de Mantequilla detectado! Corrompiendo datos... ERROR\n"
# El "contador de ataque": cuántas líneas inútiles agregaremos.
cantidad_ataque = 1000000 

print(f"** ¡Iniciando el hack de saturación en {nombre_archivo}! **")
print("Preparando la inyección de líneas inútiles...")

# Abrir el archivo en modo de adición ('a')
try:
    with open(nombre_archivo, 'a') as archivo:
        tiempo_inicio = time.time()
        
        # Bucle principal del ataque
        for i in range(cantidad_ataque):
            archivo.write(linea_basura)
        
        tiempo_fin = time.time()

    print("--- Proceso Completo ---")
    print(f"Se inyectaron {cantidad_ataque} líneas de 'mantequilla' en {nombre_archivo}.")
    print(f"El tiempo de ejecución fue de {tiempo_fin - tiempo_inicio:.2f} segundos.")
    print("El archivo ahora es terriblemente grande y lento. ¡Objetivo logrado!")

except Exception as e:
    print(f"¡Falla en el ataque! Ocurrió un error: {e}")

# Opcional: mostrar el tamaño del archivo después del "daño"
if os.path.exists(nombre_archivo):
    tamano_mb = os.path.getsize(nombre_archivo) / (1024 * 1024)
    print(f"** Tamaño del archivo post-ataque: {tamano_mb:.2f} MB **")
    # Este archivo se vuelve muy grande. ¡Es un buen ejemplo de saturación!