def cabecera():
    """Muestra la cabecera de la aplicación"""
    titulo = r"""
   ______                              ______                   
  / ____/____ _ ____ ___   ___   _____/_  __/____ _ ____ _ _____
 / / __ / __ `// __ `__ \ / _ \ / ___/ / /  / __ `// __ `// ___/
/ /_/ // /_/ // / / / / //  __// /    / /  / /_/ // /_/ /(__  ) 
\____/ \__,_//_/ /_/ /_/ \___//_/    /_/   \__,_/ \__, //____/  
                                                 /____/          
            🎮 ¡Crea tu identidad gamer! 🎮
"""
    print(titulo)

def crear_tag_basico(nombre):
    """
    Crea un gamertag básico usando las primeras 4 letras.

    Parámetro:
    nombre (str): El nombre del usuario

    Retorna:
    str: Gamertag básico
    """
    tag = nombre[:4]
    return tag

def crear_tag_invertido(nombre):
    """
    Crear un gamertag invirtiendo el nombre completo.

    Parámetro:
    nombre (str): El nombre del usuario

    Retorna:
    str: Nombre invertido
    """
    tag = nombre[::-1]
    return tag

def crear_tag_intercalado(nombre, apellido):
    """
    Crea un gamertag combinando letras del nombre y apellido.
    Ejemplo: nombre="Juan", apellido="Perez" → "JPuanerez"
    
    Parámetros:
    nombre (str): El nombre del usuario
    apellido (str): El apellido del usuario
    
    Retorna:
    None (imprime directamente)
    """
    # Primera letra del nombre
    inicial_nombre = nombre[0]
    # Primera letra del apellido
    inicial_apellido = apellido[0]
    # Resto del nombre
    resto_nombre = nombre[1:]
    # Resto del apellido
    resto_apellido = apellido[1:]
    print("3. TAG INTERCALADO: ", inicial_nombre, inicial_apellido, resto_nombre, resto_apellido, sep="")

def crear_tag_elite(nombre):
    """
    Crea un gamertag "elite" usando inicio y final del nombre.
    Ejemplo: "Santiago" → "Sago"
    
    Parámetro:
    nombre (str): El nombre del usuario
    
    Retorna:
    None (imprime directamente)
    """
    # Primeras 2 letras
    inicio = nombre[:2]
    # Últimas 2 letras
    final = nombre[-2:]
    print("4. TAG ELITE: ", inicio, final, sep="")
    
def crear_tag_con_numero(nombre, numero_favorito):
    """
    Crea un gamertag añadiendo número al final.
    
    Parámetros:
    nombre (str): El nombre del usuario
    numero_favorito (int): Número favorito del usuario
    
    Retorna:
    None (imprime directamente)
    """
    print("5. TAG CON NÚMERO: ", nombre[:5], numero_favorito, sep="")

def mostrar_estadisticas(nombre):
    """
    Muestra estadísticas del nombre proporcionado.
    
    Parámetro:
    nombre (str): El nombre a analizar
    
    Retorna:
    None (imprime directamente)
    """
    longitud_nombre = len(nombre)
    print("\n📊 ESTADÍSTICAS DE TU NOMBRE:")
    print("Nombre completo:", nombre)
    print("Longitud del nombre:", longitud_nombre)
    print("Primera letra:", nombre[0])
    print("Última letra:", nombre[-1])

def generar_todas_opciones(nombre, apellido, numero):
    """
    Genera y muestra todas las opciones de gamertags.
    
    Parámetros:
    nombre (str): Nombre del usuario
    apellido (str): Apellido del usuario
    numero (int): Número favorito
    
    Retorna:
    None (imprime directamente)
    """
    print("\n====================================")
    print("🎯 TUS OPCIONES DE GAMERTAG:")
    print("====================================")

    tag_basico = crear_tag_basico(nombre)
    print("\n1. TAG BÁSICO:", tag_basico)
    print("2. TAG INVERTIDO:", crear_tag_invertido(nombre))
    crear_tag_intercalado(nombre, apellido)
    crear_tag_elite(nombre)
    crear_tag_con_numero(nombre, numero)

    print("\n====================================")

# =====================================
# APLICACION PRINCIPAL
# =====================================

# Mostrar cabecera
cabecera()

# Solicitar datos al usuario
nombre = input("\n👤 Introduce tu nombre: ")
apellido = input("📝 Introduce tu apellido: ")
numero = input("🔢 Introduce tu número favorito: ")

# Mostrar estadísticas del nombre
mostrar_estadisticas(nombre)

# Generar y mostrar todas las opciones de gamertag
generar_todas_opciones(nombre, apellido, numero)

print("\n✨ ¡Elige tu favorito y conquista el mundo gamer! ✨\n")