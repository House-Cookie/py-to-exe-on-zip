import os
# Asegúrate de ejecutar esto en una carpeta vacía o de prueba.
# ¡No quiero que arruines tus archivos importantes!

def crear_archivos_basura():
    """Crea 500 archivos de texto vacíos en la carpeta actual."""
    
    # Número de archivos a crear (¡una cantidad molesta!)
    numero_de_archivos = 500
    
    print(f"Iniciando sobrecarga de archivos... ¡Creando {numero_de_archivos} archivos temporales!")

    for i in range(numero_de_archivos):
        # Nombra el archivo como si fuera un registro de error
        nombre_archivo = f"RegistroTemporal_Error_{i+1:03d}.log"
        
        try:
            # Abre el archivo en modo escritura ('w')
            # y lo cierra inmediatamente, dejándolo vacío.
            with open(nombre_archivo, 'w') as f:
                # Escribe un contenido inútil.
                f.write(f"Hora de creación: {os.times()[4]}\n")
            print(f"Archivo creado: {nombre_archivo}")

        except Exception as e:
            print(f"Error al crear archivo {nombre_archivo}: {e}")

    print("¡Sobrecarga de archivos completada! ¡Disfruta de tu nueva montaña de archivos!")

# ¡Activa el script!
crear_archivos_basura()