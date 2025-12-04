import os
import time
import random
import ctypes

# =================================================================
# 1. Simulación de Mensajes Críticos Aleatorios
# =================================================================

def mostrar_error_critico_simulado():
    """Simula una ventana de error crítica."""
    titulos = ["Error de Sistema 404", "Advertencia Temporal", "Sobrecarga de Datos de Tiempo", "¡Señales de Fugas de Crema!"]
    mensajes = [
        "ERROR: Se detectó una alteración en la línea de tiempo. Deshacer (S/N)?",
        "El componente principal del Sistema se ha deteriorado. ¡Inmediata Reparación Requerida!",
        "ATENCIÓN: Se ha perdido la conexión al Reloj Maestro. El tiempo se detiene en 3... 2...",
        "¡Archivos de Configuracion Culinaria Corruptos! ¡Su galleta favorita ha sido reemplazada!"
    ]
    
    # Esto solo funciona en Windows para mostrar una ventana real de mensaje
    if os.name == 'nt':
        try:
            ctypes.windll.user32.MessageBoxW(0, random.choice(mensajes), random.choice(titulos), 0x10) # 0x10 es el icono de error crítico
        except:
            print(f"[{random.choice(titulos)}]: {random.choice(mensajes)}")
    else:
        print(f"\n--- [MENSAJE CRÍTICO SIMULADO] ---\n{random.choice(titulos)}:\n{random.choice(mensajes)}\n---------------------------------\n")

# =================================================================
# 2. Simulación de Cambio de Registro de Sistema (Registro Mágico)
# =================================================================

REGISTRO_MAGICO_SIMULADO = {
    "Configuracion_Tiempo": "2025-12-04_13:00:00",
    "Clave_Auto_Ejecucion": "False",
    "Frecuencia_Parpadeo": "100ms"
}

def alterar_registro_simulado():
    """Simula la alteración de claves del registro."""
    
    global REGISTRO_MAGICO_SIMULADO
    
    print("\n[INICIANDO] Simulación de Alteración de Claves Críticas de Registro...")
    time.sleep(1)
    
    # Inversión de valores
    REGISTRO_MAGICO_SIMULADO["Frecuencia_Parpadeo"] = "5000ms (¡Súper Lento!)"
    REGISTRO_MAGICO_SIMULADO["Clave_Auto_Ejecucion"] = "True (¡Ahora te veré siempre!)"
    
    # Clave nueva, ¡la sorpresa!
    REGISTRO_MAGICO_SIMULADO["Mensaje_Secreto_Croissant"] = "¡El tiempo es solo una ilusión, y el MBR no está tan seguro!"
    
    print("\n[TERMINADO] Claves alteradas. Nuevos valores:")
    for key, value in REGISTRO_MAGICO_SIMULADO.items():
        print(f"   -> {key}: {value}")

# =================================================================
# 3. Simulación de Manipulación MBR (Master Boot Record)
# =================================================================

def simular_manipulacion_mbr():
    """Teoriza la manipulación del MBR, aunque no es funcional en Python puro."""
    
    print("\n[ACCEDIENDO] Al sector 0 del disco: Master Boot Record (MBR)...")
    time.sleep(2)
    
    # En un código real a bajo nivel, aquí se escribirían bytes directamente.
    # Por ejemplo, un *assembly* que sustituya la rutina de arranque por un mensaje.
    
    mensaje_mbr = "El MBR ha sido reemplazado por una deliciosa Receta de Croissant. ¡Arranca el Horno!"
    print(f"\n[ESCRITO] Nuevo MBR cargado con el Payload: '{mensaje_mbr}'")
    print("El sistema requerirá una 'reparación de arranque' al reiniciar. ¡Sorpresa!")

# =================================================================
# 4. El Payload Mágico (Función Principal)
# =================================================================

def payload_magico_simulado():
    """El virus 'mágico' con múltiples sorpresas."""
    
    print("--- ¡Activando el Payload Mágico de Croissant Cookie! ---")
    
    # Sorpresa 1 y 2: Ventanas y Registro
    mostrar_error_critico_simulado()
    alterar_registro_simulado()
    
    # Sorpresa 3: La gran alteración del MBR
    simular_manipulacion_mbr()
    
    # Sorpresa final: Un mensaje de despedida en modo tiempo detenido
    print("\n--- [TERMINADO] El tiempo se reanuda. ¡Vuelve a tu época! ---")

# --- Ejecutar la simulación ---
# payload_magico_simulado() 
# Comentado para evitar ejecución accidental, pero la estructura está ahí.
