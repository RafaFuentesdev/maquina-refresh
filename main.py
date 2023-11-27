import json

# Variables globales
inventario = {}
dinero = 0


def cargar_inventario(archivo):
    global inventario, dinero
    try:
        with open(archivo, "r") as file:
            datos = json.load(file)
            inventario = datos["items"]
            dinero = datos["dinero"]
    except Exception as e:
        print(f"Error al cargar el inventario: {e}")


def guardar_inventario(archivo):
    try:
        datos = {"items": inventario, "dinero": dinero}
        with open(archivo, "w") as file:
            json.dump(datos, file, indent=4)
        print("Inventario guardado exitosamente.")
    except Exception as e:
        print(f"Error al guardar el inventario: {e}")


def mostrar_menu():
    print("\nBebidas Disponibles:")
    print("-" * 50)
    for nombre, datos in inventario.items():
        print(f"{nombre}: Precio: {datos['precio']}€ - Cantidad: {datos['cantidad']}")
    print("-" * 50)


def seleccionar_bebida():
    bebida = input("Seleccione una bebida: ")
    if bebida in inventario and inventario[bebida]["cantidad"] > 0:
        return bebida
    else:
        print("Bebida no disponible.")
        return None


def procesar_pago(precio):
    global dinero
    print(f"El precio es: {precio:.2f}€")
    dinero_ingresado = float(input("Ingrese el dinero: "))
    if dinero_ingresado >= precio:
        cambio = round(dinero_ingresado - precio, 2)
        print(f"Cambio: {cambio:.2f}€")
        dinero += precio
        return True
    else:
        print("Dinero insuficiente.")
        return False


def main():
    archivo_inventario = "inventario.json"
    cargar_inventario(archivo_inventario)
    print(inventario)

    print("Bienvenido a la Máquina de Refrescos")
    print("Seleccione una opción para comenzar.\n")

    while True:
        mostrar_menu()
        opcion = input("Opciones:\n 1: Comprar\n 2: Salir\nSeleccione una opción: ")

        if opcion == "1":
            bebida_seleccionada = seleccionar_bebida()
            if bebida_seleccionada:
                if procesar_pago(inventario[bebida_seleccionada]["precio"]):
                    inventario[bebida_seleccionada]["cantidad"] -= 1
                    print("Compra exitosa.")
                else:
                    print("Compra fallida.")
            guardar_inventario(archivo_inventario)
        elif opcion == "q":
            guardar_inventario(archivo_inventario)
            print("Gracias por usar la máquina de refrescos.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
