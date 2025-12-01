# ¡Importo la herramienta del sistema!
import time 

# Lista que crecerá para consumir memoria RAM (¡es un agujero negro de memoria!)
lista_gigante = []

# La función que hace la sobrecarga
def ataque_de_sobrecarga():
    """Ejecuta un bucle infinito que consume RAM y CPU."""
    
    print("🚀 Iniciando la sobrecarga... ¡Prepárate para la lentitud!")
    
    # El "while True" asegura que la función nunca se detenga.
    while True:
        
        # 1. Consumo de RAM: Agrego cadenas de texto grandes 
        # a la lista en cada iteración. ¡La lista se hace GIGANTE!
        # Cada cadena tiene 1 millón de caracteres 'X'
        try:
            cadena_pesada = "X" * 1_000_000
            lista_gigante.append(cadena_pesada)
            
            # 2. Consumo de CPU: Hago un cálculo inútil y repetitivo
            # sin pausas para mantener el procesador trabajando al máximo.
            for i in range(1000):
                _ = 12345 * 98765 / (i + 1)
            
            # ¡Digo cuánta memoria se está consumiendo!
            if len(lista_gigante) % 50 == 0:
                 print(f"¡Memoria utilizada por la lista: {len(lista_gigante)} MB (aproximadamente)! ¡Casi se congela!")

            # Un micro-descanso para no bloquear *inmediatamente*
            time.sleep(0.001)

        except KeyboardInterrupt:
            # Puedes presionar Ctrl+C en la terminal para detenerlo
            print("\n¡Desconexión de emergencia! ¡Sobrecarga abortada!")
            break
        except Exception as e:
             print(f"Error inesperado: {e}")
             break

# ¡Hora de encender la máquina!
ataque_de_sobrecarga()