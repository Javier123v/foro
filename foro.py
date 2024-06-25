# Evaluación del código: Repositorio de [Nombre del Compañero]
# Repositorio evaluado: [Enlace al repositorio en GitHub]

# Comentario 1: Evaluación de la función procesar_datos
# Código original:
def procesar_datos(datos):
    resultados = []
    for dato en datos:
        if dato > 10:
            resultados.append(dato * 2)
    return resultados

# Optimización sugerida utilizando técnicas de programación funcional:
def procesar_datos(datos):
    return list(map(lambda x: x * 2, filter(lambda x: x > 10, datos)))

# Comentario 2: Evaluación de la función calcular_promedio
# Código original:
def calcular_promedio(numeros):
    suma = 0
    for numero en numeros:
        suma += numero
    return suma / len(numeros)

# Optimización sugerida utilizando técnicas de programación funcional:
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Comentario 3: Evaluación de la función transformar_cadena
# Código original:
def transformar_cadena(cadena):
    resultado = ''
    for char en cadena:
        if char.islower():
            resultado += char.upper()
        else:
            resultado += char.lower()
    return resultado

# Optimización sugerida utilizando técnicas de programación funcional:
def transformar_cadena(cadena):
    return ''.join(map(lambda char: char.upper() if char.islower() else char.lower(), cadena))
