eventos = {}
def agregar_evento():
    fecha = input("ingrese la fecha del evento (dd/mm/aaaa): ").strip()
    if fecha in eventos:
        print("ya existe un evento en esa fecha.")
        return
    descripcion = input("ingrese la descripcion del evento: ").strip()
    eventos[fecha] = descripcion
    print(f"evento registrado en {fecha}.")
def mostrar_eventos():
    if not eventos:
        print("no hay eventos registrados.")
        return
    print("\n eventos registrados:")
    for fecha, descripcion in sorted(eventos.items()):
        print(f"- {fecha}: {descripcion}")
def menu():
    while True:
        print("\n registro de eventos ")
        print("1. agregar evento")
        print("2. consultar eventos")
        print("3. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            agregar_evento()
        elif opcion == "2":
            mostrar_eventos()
        elif opcion == "3":
            print("saliendo del registro de eventos.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()