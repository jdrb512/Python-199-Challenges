"""
Sistema de Pedidos de Restaurante con Delivery
"""

# ===== BASE DE DATOS DEL RESTAURANTE =====

# Menú del restaurante organizado por categorías
menu = {
    "entradas": {
        "Nachos": {"precio": 8.50, "tiempo": 10, "puntos": 50},
        "Alitas BBQ": {"precio": 12.00, "tiempo": 15, "puntos": 80},
        "Ensalada César": {"precio": 9.00, "tiempo": 8, "puntos": 60},
        "Croquetas": {"precio": 7.50, "tiempo": 12, "puntos": 45}
    },
    "principales": {
        "Pizza Margherita": {"precio": 15.00, "tiempo": 20, "puntos": 100},
        "Pizza Pepperoni": {"precio": 16.50, "tiempo": 20, "puntos": 110},
        "Hamburguesa Clásica": {"precio": 13.50, "tiempo": 18, "puntos": 90},
        "Hamburguesa BBQ": {"precio": 14.50, "tiempo": 18, "puntos": 95},
        "Pasta Carbonara": {"precio": 14.00, "tiempo": 15, "puntos": 95},
        "Pasta Bolognesa": {"precio": 13.00, "tiempo": 15, "puntos": 85}
    },
    "postres": {
        "Helado": {"precio": 5.00, "tiempo": 2, "puntos": 30},
        "Tarta de Queso": {"precio": 6.50, "tiempo": 3, "puntos": 40},
        "Brownie": {"precio": 5.50, "tiempo": 3, "puntos": 35},
        "Flan": {"precio": 4.50, "tiempo": 2, "puntos": 25}
    },
    "bebidas": {
        "Refresco": {"precio": 3.00, "tiempo": 1, "puntos": 15},
        "Agua": {"precio": 2.00, "tiempo": 1, "puntos": 10},
        "Jugo Natural": {"precio": 4.50, "tiempo": 3, "puntos": 25},
        "Café": {"precio": 2.50, "tiempo": 2, "puntos": 15}
    }
}

# Base de datos de clientes VIP con puntos acumulados
clientes_vip = {
    "juan": {"puntos": 500, "pedidos": 12},
    "maria": {"puntos": 1200, "pedidos": 28},
    "pedro": {"puntos": 300, "pedidos": 7},
    "ana": {"puntos": 850, "pedidos": 19},
    "luis": {"puntos": 150, "pedidos": 3}
}

# Combos especiales del día (sets para los items)
combos_del_dia = {
    "Combo Italiano": {
        "items": {"Pizza Margherita", "Refresco"},
        "descuento": 15  # Porcentaje de descuento
    },
    "Combo Burger": {
        "items": {"Hamburguesa Clásica", "Nachos", "Refresco"},
        "descuento": 20
    },
    "Combo Light": {
        "items": {"Ensalada César", "Agua", "Flan"},
        "descuento": 10
    }
}

# ===== FUNCIONES DEL SISTEMA =====

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida del restaurante."""
    print("=" * 60)
    print(" " * 15 + "🍕 ¡Bienvenido a Python Eats! 🍕")
    print("=" * 60)
    print()


def verificar_cliente():
    """
    Verifica si el cliente está registrado y retorna su información.
    
    Returns:
        tuple: (nombre_cliente, puntos_disponibles, es_vip)
    """
    es_cliente = ""
    while es_cliente not in ["s", "n", "si", "no"]:
        es_cliente = input("¿Eres cliente registrado? (s/n): ")
        if es_cliente not in ["s", "n", "si", "no"]:
            print("❌ Por favor, ingresa 's' para sí o 'n' para no.")
    
    if es_cliente in ["s", "si"]:
        nombre = input("Ingresa tu nombre: ")
        
        if nombre in clientes_vip:
            puntos = clientes_vip[nombre]["puntos"]
            print(f"\n✨ ¡Hola {nombre}! Tienes {puntos} puntos acumulados.")
            print(f"📊 Has realizado {clientes_vip[nombre]['pedidos']} pedidos con nosotros.")
            return nombre, puntos, True
        else:
            print(f"\n👋 Hola {nombre}! No estás registrado como cliente VIP.")
            print("   Te registraremos automáticamente después de tu pedido.")
            return nombre, 0, False
    else:
        print("\n👋 ¡Bienvenido nuevo cliente!")
        nombre = input("¿Cómo te llamas? ")
        print(f"   Gracias {nombre}, te registraremos después del pedido.")
        return nombre, 0, False


def mostrar_menu_principal():
    """Muestra el menú principal de opciones."""
    print("\n" + "=" * 40)
    print("        MENÚ PRINCIPAL")
    print("=" * 40)
    print("1. 📖 Ver menú completo")
    print("2. 🛒 Realizar pedido")
    print("3. 🎁 Ver ofertas del día")
    print("4. ⭐ Canjear puntos")
    print("5. 🚪 Salir")
    print("=" * 40)


def mostrar_menu_completo():
    """Muestra todos los productos disponibles organizados por categoría."""
    print("\n" + "=" * 50)
    print("         MENÚ COMPLETO")
    print("=" * 50)
    
    # Iterar por cada categoría del menú
    for categoria in menu:
        print(f"\n🍴 {categoria}")
        print("-" * 30)
        
        contador = 1
        productos = menu[categoria]
        for nombre in productos:
            info = productos[nombre]
            precio = info["precio"]
            tiempo = info["tiempo"]
            puntos = info["puntos"]
            print(f"  {contador}. {nombre}")
            print(f"     💵 ${precio:.2f} | ⏱️ {tiempo} min | ⭐ {puntos} pts")
            contador += 1
    
    print("\n" + "=" * 50)
    input("\nPresiona Enter para continuar...")


def mostrar_ofertas():
    """Muestra los combos especiales del día."""
    print("\n" + "=" * 50)
    print("       🎁 OFERTAS DEL DÍA 🎁")
    print("=" * 50)
    
    contador = 1
    for nombre_combo in combos_del_dia:
        info_combo = combos_del_dia[nombre_combo]
        productos = ""
        for item in info_combo['items']: productos += f'{item}, '
        print(f"\n{contador}. {nombre_combo}")
        print(f"   Incluye: {productos[:-2]}")
        print(f"   💥 {info_combo['descuento']}% de descuento")
        contador += 1
    
    print("\n" + "=" * 50)
    input("\nPresiona Enter para continuar...")


def calcular_precio_con_puntos(total, puntos_disponibles):
    """
    Pregunta si el cliente quiere usar sus puntos y calcula el descuento.
    
    Args:
        total (float): Total del pedido
        puntos_disponibles (int): Puntos disponibles del cliente
    
    Returns:
        tuple: (nuevo_total, puntos_usados)
    """
    if puntos_disponibles == 0:
        return total, 0
    
    # Conversión: 100 puntos = $1
    descuento_maximo = puntos_disponibles / 100
    
    print(f"\n💰 Tienes {puntos_disponibles} puntos disponibles")
    print(f"   Equivalen a un descuento de hasta ${descuento_maximo:.2f}")
    
    usar = ""
    while usar not in ["s", "n", "si", "no"]:
        usar = input("¿Deseas usar tus puntos? (s/n): ")
        if usar not in ["s", "n", "si", "no"]:
            print("❌ Por favor, ingresa 's' o 'n'")
    
    if usar in ["s", "si"]:
        puntos_a_usar = 0
        while True:
            entrada = input(f"¿Cuántos puntos quieres usar? (máx {puntos_disponibles}): ")
            
            # Verificar que sea un número
            es_numero = True
            for char in entrada:
                if char not in "0123456789":
                    es_numero = False
                    break
            
            if es_numero and entrada != "":
                puntos_a_usar = int(entrada)
                if 0 <= puntos_a_usar <= puntos_disponibles:
                    descuento = puntos_a_usar / 100
                    if descuento <= total:
                        return total - descuento, puntos_a_usar
                    else:
                        print(f"❌ El descuento (${descuento:.2f}) es mayor que el total")
                else:
                    print(f"❌ Debes ingresar un número entre 0 y {puntos_disponibles}")
            else:
                print("❌ Por favor, ingresa un número válido")
    
    return total, 0


def verificar_combo(items_pedido):
    """
    Verifica si los items del pedido forman algún combo.
    
    Args:
        items_pedido (list): Lista de nombres de productos en el pedido
    
    Returns:
        tuple: (nombre_combo, descuento) o (None, 0) si no hay combo
    """
    for nombre_combo in combos_del_dia:
        info_combo = combos_del_dia[nombre_combo]
        # Verificar si todos los items del combo están en el pedido
        if all(item in items_pedido for item in info_combo["items"]):
            return nombre_combo, info_combo["descuento"]

    return None, 0


def realizar_pedido(nombre_cliente, puntos_disponibles):
    """
    Proceso principal para realizar un pedido.
    
    Args:
        nombre_cliente (str): Nombre del cliente
        puntos_disponibles (int): Puntos disponibles del cliente
    
    Returns:
        tuple: (total_final, puntos_ganados, puntos_usados)
    """
    carrito = []  # Lista de tuplas (producto, cantidad, precio_unitario, tiempo)
    continuar = True
    
    while continuar:
        print("\n" + "=" * 40)
        print("       REALIZAR PEDIDO")
        print("=" * 40)
        print("1. Entradas")
        print("2. Platos Principales")
        print("3. Postres")
        print("4. Bebidas")
        print("5. Ver carrito")
        print("6. Finalizar pedido")
        print("=" * 40)
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            agregar_producto(carrito, "entradas")
        elif opcion == "2":
            agregar_producto(carrito, "principales")
        elif opcion == "3":
            agregar_producto(carrito, "postres")
        elif opcion == "4":
            agregar_producto(carrito, "bebidas")
        elif opcion == "5":
            mostrar_carrito(carrito)
        elif opcion == "6":
            if len(carrito) > 0:
                continuar = False
            else:
                print("\n❌ El carrito está vacío. Agrega productos antes de finalizar.")
        else:
            print("\n❌ Opción inválida. Intenta de nuevo.")
    
    # Calcular totales y aplicar descuentos
    return procesar_pedido(carrito, nombre_cliente, puntos_disponibles)


def agregar_producto(carrito, categoria):
    """
    Agrega un producto al carrito desde una categoría específica.
    
    Args:
        carrito (list): Lista del carrito de compras
        categoria (str): Categoría del menú
    """
    print(f"\n--- {categoria} ---")
    productos = menu[categoria]
    
    # Mostrar productos de la categoría
    lista_productos = []
    contador = 1
    for nombre in productos:
        info = productos[nombre]
        print(f"{contador}. {nombre} - ${info['precio']:.2f}")
        lista_productos += [(nombre, info)]
        contador += 1
    print("0. Volver")
    
    # Seleccionar producto
    seleccion = input("\n¿Qué deseas agregar? (0 para volver): ")
    
    # Validar entrada
    es_numero = True
    for char in seleccion:
        if char not in "0123456789":
            es_numero = False
            break
    
    if not es_numero or seleccion == "":
        print("❌ Por favor, ingresa un número válido.")
        return
    
    seleccion = int(seleccion)
    
    if seleccion == 0:
        return
    elif 1 <= seleccion <= len(lista_productos):
        nombre_producto, info_producto = lista_productos[seleccion - 1]
        
        # Solicitar cantidad
        cantidad_str = input("¿Cuántas unidades? ")
        
        # Validar cantidad
        es_numero = True
        for char in cantidad_str:
            if char not in "0123456789":
                es_numero = False
                break
        
        if es_numero and cantidad_str != "" and int(cantidad_str) > 0:
            cantidad = int(cantidad_str)
            # Agregar al carrito (nombre, cantidad, precio_unitario, tiempo, puntos)
            carrito += [(
                nombre_producto,
                cantidad,
                info_producto["precio"],
                info_producto["tiempo"],
                info_producto["puntos"]
            )]
            print(f"\n✅ {cantidad}x {nombre_producto} agregado al carrito")
        else:
            print("❌ Cantidad inválida.")
    else:
        print("❌ Selección inválida.")


def mostrar_carrito(carrito):
    """
    Muestra el contenido actual del carrito.
    
    Args:
        carrito (list): Lista del carrito de compras
    """
    if len(carrito) == 0:
        print("\n🛒 El carrito está vacío.")
        input("\nPresiona Enter para continuar...")
        return
    
    print("\n" + "=" * 50)
    print("         🛒 TU CARRITO")
    print("=" * 50)
    
    total = 0
    tiempo_total = 0
    
    for item in carrito:
        nombre, cantidad, precio, tiempo, puntos = item
        subtotal = cantidad * precio
        total += subtotal
        tiempo_total = max(tiempo_total, tiempo)  # El tiempo es el del plato más lento
        
        print(f"{cantidad}x {nombre}")
        print(f"   ${precio:.2f} c/u = ${subtotal:.2f}")
    
    print("-" * 50)
    print(f"TOTAL: ${total:.2f}")
    print(f"Tiempo estimado: {tiempo_total} minutos")
    print("=" * 50)
    
    input("\nPresiona Enter para continuar...")


def procesar_pedido(carrito, nombre_cliente, puntos_disponibles):
    """
    Procesa el pedido final aplicando descuentos y calculando puntos.
    
    Args:
        carrito (list): Lista del carrito de compras
        nombre_cliente (str): Nombre del cliente
        puntos_disponibles (int): Puntos disponibles del cliente
    
    Returns:
        tuple: (total_final, puntos_ganados, puntos_usados)
    """
    # Calcular totales iniciales
    subtotal = 0
    tiempo_max = 0
    puntos_ganados = 0
    items_pedido = []
    
    print("\n" + "=" * 60)
    print("         📋 RESUMEN DEL PEDIDO")
    print("=" * 60)
    
    for item in carrito:
        nombre, cantidad, precio, tiempo, puntos = item
        subtotal_item = cantidad * precio
        subtotal += subtotal_item
        puntos_ganados += puntos * cantidad
        tiempo_max = max(tiempo_max, tiempo)
        
        # Agregar items al listado para verificar combos
        for _ in range(cantidad):
            items_pedido += [nombre]
        
        print(f"{cantidad}x {nombre}: ${subtotal_item:.2f}")
    
    print("-" * 60)
    print(f"Subtotal: ${subtotal:.2f}")
    
    # Verificar si hay combo
    combo_aplicado, descuento_combo = verificar_combo(items_pedido)
    descuento_monto = 0
    
    if combo_aplicado:
        descuento_monto = subtotal * (descuento_combo / 100)
        print(f"\n🎉 ¡Combo {combo_aplicado} aplicado!")
        print(f"   Descuento del {descuento_combo}%: -${descuento_monto:.2f}")
    
    total = subtotal - descuento_monto
    
    # Aplicar descuento por puntos si el cliente quiere
    puntos_usados = 0
    if puntos_disponibles > 0:
        total, puntos_usados = calcular_precio_con_puntos(total, puntos_disponibles)
        if puntos_usados > 0:
            print(f"⭐ Puntos usados: {puntos_usados} (-${puntos_usados/100:.2f})")
    
    # Happy Hour: 10% descuento adicional (simulado con número de pedidos)
    pedidos_del_dia = 47  # Número fijo para simular pedidos del día
    if pedidos_del_dia % 10 == 7:  # Cada 10 pedidos, el séptimo tiene happy hour
        descuento_happy = total * 0.10
        print(f"\n🍻 ¡HAPPY HOUR! 10% descuento adicional: -${descuento_happy:.2f}")
        total -= descuento_happy
    
    # Cliente sorpresa (cada pedido 50)
    if pedidos_del_dia == 50:
        print("\n🎊 ¡FELICIDADES! ¡Eres nuestro cliente #50 del día!")
        print("   ¡Tu pedido es GRATIS! 🎁")
        total = 0
    
    print("\n" + "=" * 60)
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print(f"Tiempo de entrega: {tiempo_max} minutos")
    print(f"Puntos ganados: {puntos_ganados}")
    print("=" * 60)
    
    # Confirmar pedido
    confirmar = ""
    while confirmar not in ["s", "n", "si", "no"]:
        confirmar = input("\n¿Confirmar pedido? (s/n): ")
        if confirmar not in ["s", "n", "si", "no"]:
            print("❌ Por favor, ingresa 's' o 'n'")
    
    if confirmar in ["s", "si"]:
        print("\n✅ ¡Pedido confirmado!")
        print(f"📍 Tu pedido llegará en {tiempo_max} minutos.")
        
        # Solicitar reseña
        print("\n⭐ ¿Cómo calificarías tu experiencia? (1-5 estrellas)")
        calificacion = input("Calificación: ")
        
        # Validar calificación
        if calificacion in ["1", "2", "3", "4", "5"]:
            estrellas = "⭐" * int(calificacion)
            print(f"\n¡Gracias por tu calificación de {estrellas}!")

        # Registrar cliente
        if nombre_cliente not in clientes_vip:
            clientes_vip[nombre_cliente] = {"puntos": puntos_ganados, "pedidos": 1}
            print(f"\n¡Has sido registrado como cliente VIP, accede con tu nombre!")
        
        return total, puntos_ganados, puntos_usados
    else:
        print("\n❌ Pedido cancelado.")
        return 0, 0, 0


def menu_canjear_puntos(puntos_disponibles):
    """
    Menú para canjear puntos por productos gratis.
    
    Args:
        puntos_disponibles (int): Puntos disponibles del cliente
    
    Returns:
        int: Puntos utilizados
    """
    if puntos_disponibles < 100:
        print("\n❌ Necesitas al menos 100 puntos para canjear.")
        print(f"   Actualmente tienes: {puntos_disponibles} puntos")
        input("\nPresiona Enter para continuar...")
        return 0
    
    print("\n" + "=" * 50)
    print("       ⭐ CANJEAR PUNTOS ⭐")
    print("=" * 50)
    print(f"Puntos disponibles: {puntos_disponibles}")
    print("\nProductos disponibles para canje:")
    print("-" * 50)
    
    # Crear lista de productos canjeables
    productos_canjeables = []
    
    for categoria in menu:
        productos = menu[categoria]
        for nombre in productos:
            info = productos[nombre]
            puntos_necesarios = info["puntos"] * 3  # Canje cuesta 3x los puntos que da
            if puntos_necesarios <= puntos_disponibles:
                productos_canjeables += [(nombre, puntos_necesarios, categoria)]
    
    if len(productos_canjeables) == 0:
        print("No hay productos disponibles con tus puntos actuales.")
        input("\nPresiona Enter para continuar...")
        return 0
    
    # Mostrar productos canjeables
    for i, (nombre, puntos, categoria) in enumerate(productos_canjeables, 1):
        print(f"{i}. {nombre} ({categoria}) - {puntos} puntos")
    print("0. Volver")
    
    # Seleccionar producto
    seleccion = input("\n¿Qué deseas canjear? ")
    
    # Validar entrada
    es_numero = True
    for char in seleccion:
        if char not in "0123456789":
            es_numero = False
            break
    
    if not es_numero or seleccion == "":
        print("❌ Selección inválida.")
        return 0
    
    seleccion = int(seleccion)
    
    if seleccion == 0:
        return 0
    elif 1 <= seleccion <= len(productos_canjeables):
        nombre, puntos_canje, categoria = productos_canjeables[seleccion - 1]
        print(f"\n✅ Has canjeado: {nombre}")
        print(f"   Puntos utilizados: {puntos_canje}")
        print(f"   ¡Tu pedido llegará en {menu[categoria][nombre]['tiempo']} minutos!")
        input("\nPresiona Enter para continuar...")
        return puntos_canje
    else:
        print("❌ Selección inválida.")
        return 0


def main():
    """Función principal del programa."""
    # Mostrar bienvenida
    mostrar_bienvenida()
    
    # Verificar cliente
    nombre_cliente, puntos_disponibles, es_vip = verificar_cliente()
    
    # Variables para el control del programa
    ejecutando = True
    puntos_totales_ganados = 0
    puntos_totales_usados = 0
    
    # Bucle principal del programa
    while ejecutando:
        mostrar_menu_principal()
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            # Ver menú completo
            mostrar_menu_completo()
            
        elif opcion == "2":
            # Realizar pedido
            total, puntos_ganados, puntos_usados = realizar_pedido(
                nombre_cliente, 
                puntos_disponibles - puntos_totales_usados + puntos_totales_ganados
            )
            puntos_totales_ganados += puntos_ganados
            puntos_totales_usados += puntos_usados
            es_vip = True
            
        elif opcion == "3":
            # Ver ofertas
            mostrar_ofertas()
            
        elif opcion == "4":
            # Canjear puntos
            if es_vip:
                puntos_actual = puntos_disponibles - puntos_totales_usados + puntos_totales_ganados
                puntos_canjeados = menu_canjear_puntos(puntos_actual)
                puntos_totales_usados += puntos_canjeados
            else:
                print("\n❌ Necesitas ser cliente VIP para canjear puntos.")
                print("   Realiza tu primer pedido para registrarte.")
                input("\nPresiona Enter para continuar...")
            
        elif opcion == "5":
            # Salir
            print("\n" + "=" * 50)
            print("¡Gracias por visitarnos! 👋")
            print(f"Hasta pronto, {nombre_cliente}!")
            
            # Mostrar resumen si hubo actividad
            if puntos_totales_ganados > 0 or puntos_totales_usados > 0:
                print("\nResumen de tu sesión:")
                print(f"  Puntos ganados: {puntos_totales_ganados}")
                print(f"  Puntos usados: {puntos_totales_usados}")
                saldo_final = puntos_disponibles - puntos_totales_usados + puntos_totales_ganados
                print(f"  Saldo de puntos: {saldo_final}")
            
            print("=" * 50)
            ejecutando = False
            
        else:
            print("\n❌ Opción inválida. Por favor, elige entre 1 y 5.")
    
    print("\n¡Programa finalizado!")


# ===== EJECUTAR EL PROGRAMA =====
# Llamar a la función principal
main()