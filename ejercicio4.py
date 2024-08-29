"""
En este ejercicio, no se utilizó Programación Orientada a Objetos (POO), 
sino que se optó por el uso de funciones sencillas y estructuras de datos básicas como listas y diccionarios. 
Esta decisión se tomó para mantener el código simple y accesible, ideal para situaciones donde la complejidad del sistema es moderada
 y no requiere una estructura más formal.
"""

# Función para crear un nuevo vehículo
def registrar_vehiculo(tipo, marca, modelo, año, coste):
    vehiculo = {
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "año": año,
        "coste": coste,
        "disponible": True
    }


    return vehiculo

# Función para mostrar los vehículos disponibles
def mostrar_vehiculos_disponibles(vehiculos):


    print("\n--- Vehículos Disponibles ---")



    for i, vehiculo in enumerate(vehiculos):
        if vehiculo["disponible"]:
            print(f"{i + 1}. {vehiculo['tipo']} {vehiculo['marca']} {vehiculo['modelo']} ({vehiculo['año']}) - ${vehiculo['coste']} por día")
    print()





# La función para rentar un vehículo
def rentar_vehiculo(vehiculos, indice_vehiculo, cliente, dias_renta):
    vehiculo = vehiculos[indice_vehiculo]
    if vehiculo["disponible"]:
        vehiculo["disponible"] = False
        renta = {
            "cliente": cliente,
            "vehiculo": vehiculo,
            "dias_renta": dias_renta,
            "total_costo": vehiculo["coste"] * dias_renta
        }



        print(f"\n{cliente['nombre']}, ha rentado el {vehiculo['tipo']} {vehiculo['marca']} {vehiculo['modelo']} ({vehiculo['año']}) por {dias_renta} días.")
        print(f"Total a pagar: ${renta['total_costo']}")
        return renta
    

    else:
        print("El vehículo seleccionado no está disponible.")
        return None
    




# La función para crear un nuevo cliente
def registrar_cliente(nombre, telefono, Dui):
    cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "Dui": Dui
    }
    return cliente

def main():
    vehiculos = []

    # Registro de vehículos en el lote por defecto
    vehiculos.append(registrar_vehiculo("Sedán", "Toyota", "Corolla", 2022, 100.0))
    vehiculos.append(registrar_vehiculo("Deportivo", "Mclaren", "720S", 2021, 300.0))
    vehiculos.append(registrar_vehiculo("Camioneta", "Ford", "F-150", 2023, 350.0))

    print("-------- Bienvenido al sistema de renta de vehículos --------------")


# menu principal para el usuario
    while True:
        print("\n1. Registrar un nuevo vehículo")
        print("2. Ver vehículos disponibles")
        print("3. Rentar un vehículo")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")



        if opcion == '1':
            tipo = input("Ingrese el tipo de vehículo: ")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            año = int(input("Ingrese el año del vehículo: "))
            coste = float(input("Ingrese el coste de renta por día: "))
            vehiculos.append(registrar_vehiculo(tipo, marca, modelo, año, coste))
            print("Vehículo registrado exitosamente.")


        elif opcion == '2':
            mostrar_vehiculos_disponibles(vehiculos)


        elif opcion == '3':


            if any(vehiculo["disponible"] for vehiculo in vehiculos):
                nombre = input("Ingrese su nombre: ")
                telefono = input("Ingrese su teléfono: ")
                Dui = input("Ingrese su Dui: ")
                cliente = registrar_cliente(nombre, telefono, Dui)



                mostrar_vehiculos_disponibles(vehiculos)
                indice_vehiculo = int(input("Seleccione un vehículo para rentar (1 -  dependiendo de la cantidad de vehiculos disponibles): ")) - 1
                dias_renta = int(input("Ingrese la cantidad de días para la renta: "))
                


                rentar_vehiculo(vehiculos, indice_vehiculo, cliente, dias_renta)
            else:

                print("No hay vehículos disponibles para rentar.")


        elif opcion == '4':
            print("Gracias por usar el programa de renta de vehículos JIHJ.")
            break


        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
