# ¡ADVERTENCIA DE CÓDIGO EXTREMO!
# Esto es solo un esquema lógico para demostrar la posibilidad.

import os
import glob

def eliminar_registros_extremos():
    # Rutas típicas de logs en sistemas basados en Unix
    rutas_criticas = [
        '/var/log/',
        '~/.bash_history',  # Historial de comandos del usuario
        # Más rutas específicas podrían añadirse aquí
    ]
    
    contador = 0
    print("Iniciando la secuencia de eliminación crítica...")
    
    for ruta_base in rutas_criticas:
        try:
            # Si es un directorio, busca todos los archivos dentro
            if os.path.isdir(ruta_base):
                # Usamos glob para encontrar todos los archivos de log
                archivos_a_eliminar = glob.glob(os.path.join(ruta_base, '*'))
                
                for archivo in archivos_a_eliminar:
                    if os.path.isfile(archivo):
                        os.remove(archivo)
                        print(f"[{contador}] Eliminado: {archivo}")
                        contador += 1
            # Si es un archivo (como .bash_history), lo elimina directamente
            elif os.path.isfile(ruta_base):
                os.remove(ruta_base)
                print(f"[{contador}] Eliminado: {ruta_base}")
                contador += 1
                
        except PermissionError:
            print(f"--- Falla de Permiso: Necesitas ser root/sudo para {ruta_base}")
        except FileNotFoundError:
            print(f"--- Advertencia: Ruta no encontrada: {ruta_base}")
        except Exception as e:
            print(f"--- Error inesperado al procesar {ruta_base}: {e}")

    print(f"\n¡**Operación de Limpieza Finalizada**! Total de archivos eliminados: {contador}")

# Si ejecutas esta función, ¡prepara el backup!
# eliminar_registros_extremos()
