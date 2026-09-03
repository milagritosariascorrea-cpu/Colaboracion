def sugerir(palabra, opciones):
    """Devuelve las opciones que empiezan con la palabra"""
    palabra = palabra.lower()
    sugerencias = [op for op in opciones if op.lower().startswith(palabra)]
    return sugerencias[:5]  # máximo 5 sugerencias

# Ejemplo de uso
comandos = ["abrir", "cerrar", "guardar", "guardar como", "imprimir", "imprimir todo"]
entrada = input("Escribe un comando: ")

resultados = sugerir(entrada, comandos)
if resultados:
    print("¿Quisiste decir:", ", ".join(resultados))
else:
    print("No hay sugerencias")