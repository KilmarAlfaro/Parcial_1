
"""
En el ejercicio proporcionado, se utilizó la Programación Orientada a Objetos (POO) 
junto con otras funcionalidades básicas de Python, como estructuras de control y listas.
Se muestra un menu donde el usuario va decidiendo que opcion le parece la adecuada y dependiendo sus opciones
se ira rellenando su respectiva factura con el monto total a pagar y sus datos ingresados

"""


# se crea la clase habitacion donde ira el tipo de habitacion y su respectivo precio
class Habitacion:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio
# se ingresaran los datos del cliente
class Cliente:
    def __init__(self, nombre, telefono, noches):
        self.nombre = nombre
        self.telefono = telefono
        self.noches = noches
        self.habitacion = None
        self.servicios_extra = []



    def agregar_habitacion(self, habitacion):
        self.habitacion = habitacion




    def agregar_servicio_extra(self, servicio):
        self.servicios_extra.append(servicio)


# se calculara el monto total dependiendo de la habitacion, numero de noches y si adquirio servicios extras
    def calcular_total(self):
        total = self.habitacion.precio * self.noches
        for servicio in self.servicios_extra:
            total += servicio["precio"]
        return total


# los datos que se mostrara en la factura
    def mostrar_factura(self):
        print("\n----- Factura -----")
        print(f"Cliente: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Habitación: {self.habitacion.tipo}")
        print(f"Noches: {self.noches}")
        print(f"Precio por noche: ${self.habitacion.precio}")

        if self.servicios_extra:
            print("\nServicios Extra:")
            for servicio in self.servicios_extra:
                print(f"- {servicio['nombre']}: ${servicio['precio']}")
        print(f"\nTotal a pagar: ${self.calcular_total()}")



# mostrara las listas de habitaciones a eligir
def mostrar_opciones_habitaciones(habitaciones):
    print("\n----- Opciones de Habitaciones -----")
    for i, habitacion in enumerate(habitaciones):
        print(f"{i + 1}. {habitacion.tipo} - ${habitacion.precio} por noche")


# mostrara las listas de servicios extras a eligir
def mostrar_opciones_servicios(servicios):
    print("\n----- Servicios Extra -----")
    for i, servicio in enumerate(servicios):
        print(f"{i + 1}. {servicio['nombre']} - ${servicio['precio']}")

# mostrara los tipos de habitaciones y su precio
def main():
    habitaciones = [
        Habitacion("Estándar", 100),
        Habitacion("Vista al Mar", 150),
        Habitacion("Suite", 250)
    ]



    servicios_extra = [
        {"nombre": "Piscina", "precio": 25},
        {"nombre": "Cancha de Golf", "precio": 50},
    ]




    print("---------- Bienvenido al Hotel de Playa -------------")

    # Mostrara las opciones de las habitaciones
    mostrar_opciones_habitaciones(habitaciones)

    # se llevara a cabo la elección de la habitación
    opcion_habitacion = int(input("Seleccione una habitación (1-3): ")) - 1
    habitacion_elegida = habitaciones[opcion_habitacion]

    # se ingresan los datos del cliente
    nombre = input("Ingrese su nombre: ")
    telefono = input("Ingrese su número de teléfono: ")
    noches = int(input("Número de noches que desea quedarse: "))

    cliente = Cliente(nombre, telefono, noches)
    cliente.agregar_habitacion(habitacion_elegida)

    # Los servicios extra si desea agregarlos o no
    while True:
        mostrar_opciones_servicios(servicios_extra)
        opcion_servicio = input("¿Desea agregar un servicio extra? (s/n): ").lower()
        if opcion_servicio == 's':
            opcion_servicio = int(input("Seleccione un servicio extra (1-2): ")) - 1
            cliente.agregar_servicio_extra(servicios_extra[opcion_servicio])
        else:
            break

    # se mostrara la factura al usuario
    cliente.mostrar_factura()

if __name__ == "__main__":
    main()
