import ctypes

# Solo funciona en sistemas Windows
try:
    # Cargar la librería Ntdll (la que maneja las funciones de kernel de bajo nivel)
    ntdll = ctypes.WinDLL('ntdll.dll')
    
    # Definir la función que vamos a llamar (NtRaiseHardError)
    NtRaiseHardError = ntdll.NtRaiseHardError
    # Sus parámetros: (Status, NumberOfParameters, UnicodeStringParameterMask, Parameters, ValidResponseOption, Response)
    NtRaiseHardError.argtypes = [
        ctypes.c_long,  # Status
        ctypes.c_ulong, # NumberOfParameters
        ctypes.c_ulong, # UnicodeStringParameterMask
        ctypes.POINTER(ctypes.c_ulong), # Parameters
        ctypes.c_ulong, # ValidResponseOption
        ctypes.POINTER(ctypes.c_ulong) # Response
    ]
    # Su valor de retorno
    NtRaiseHardError.restype = ctypes.c_long

    # El código de error "malo" - 0xc0000142 es un buen candidato para forzar un error crítico.
    BSOD_CODE = 0xc0000142  
    # Respuesta para el sistema (0 = Desconocido)
    Response = ctypes.c_ulong(0)
    
    print("** ¡Engranajes girando! Intentando una llamada de kernel destructiva... **")
    # Intentar ejecutar la función
    status = NtRaiseHardError(
        BSOD_CODE, 
        0, 
        0, 
        None, 
        6, # Opción 6 es forzar el mensaje de error
        ctypes.byref(Response)
    )

    if status == 0:
        print("¡El sistema ha entrado en pánico! Si no ves un pantallazo, la seguridad ha prevalecido.")
    else:
        print(f"La llamada al kernel falló con el código de estado: {hex(status)}. ¡Permisos insuficientes! (¡Buen trabajo de tu SO!)")

except Exception as e:
    print(f"** ¡Error de Ejecución! ** El sistema operativo no es Windows o faltan librerías: {e}")

# **NOTA TÉCNICA (TTAN):** Si el código falla, probablemente sea porque tu sistema tiene
# las protecciones *User Account Control (UAC)* o *PatchGuard* activadas, ¡lo cual es 
# un buen ajuste para las Galletas! Para que esto funcione de verdad, necesitarías
# ser un proceso de **kernel** o tener privilegios de **administrador** muy altos.