"""Una biblioteca ofrece préstamos de libros a través de una tarjeta
impresa que contiene los datos de la persona que realiza el préstamo. El
sistema de préstamos registra la fecha en que se retira el libro y la fecha
límite para su devolución. Realiza un programa que solvente esto de
una manera más eficaz.
 Implementar la sección de devolución la cual si la fecha excede la
que devolución se dará una sanción."""


#Para empezar una función para registrar a las clientes que seria un diccionario representado por una tarjeta para este caso.
#En esta tarjeta se registraran el nombre, email, telefono y una lista en la cuál registraremos todos
#los prestamos cargados en la tarjeta.


def crear_tarjeta(nombre, email, telefono):

    #Aquí se crea el diccionario que funcionara como nuestra tarjeta

    tarjeta = {
        "nombre": nombre,
        "email": email,
        "telefono": telefono,

        #Una lista para registrar los préstamos

        "prestamos": []
    }

    #Devolvemos/regresamos nuestro diccionario para su posterior uso

    return tarjeta


#ahora una función para registrar los préstamos, se registraran el título, la fecha de prestamo y cuando debe ser devuelto


def registrar_prestamo(tarjeta, titulo_libro, fecha_prestamo, fecha_devolucion):

    #Tomamos la lista creada anteriormente en el dicionario tarjeta llamada prestamos

    prestamo = {
        "titulo_libro": titulo_libro,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion
    }

    #Y devolvemos la lista prestamos

    tarjeta["prestamos"].append(prestamo)
    return prestamo


#Una función para mostrar los prestamos hechos


def mostrar_prestamos(tarjeta):
    print("\n--- Préstamos Actuales ---")
    if tarjeta["prestamos"]:
        for prestamo in tarjeta["prestamos"]:
            print(f"Título: {prestamo['titulo_libro']}")
            print(f"Fecha de préstamo: {prestamo['fecha_prestamo']}")
            print(f"Fecha de devolución: {prestamo['fecha_devolucion']}\n")

    #si no hay registros de prestamos mostrara que no hay

    else:
        print("No hay préstamos registrados.")


#Función grafica para ingresar los datos

def main():
    print("Bienvenido al sistema de préstamos de la Biblioteca")

    # Creación de la tarjeta del usuario

    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    telefono = input("Ingrese su teléfono: ")
    
    tarjeta = crear_tarjeta(nombre, email, telefono)


    #While básico para crear un bucle para realizar varias consultas seguidas


    while True:
        print("\n1. Registrar un préstamo")
        print("2. Ver préstamos actuales")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")


        #con la consulta '1' ingresamos los prestamos que se cargaran a la tarjeta del usuairo


        if opcion == '1':
            titulo_libro = input("Ingrese el título del libro: ")
            fecha_prestamo = input("Ingrese la fecha de préstamo (DD/MM/AAAA): ")
            fecha_devolucion = input("Ingrese la fecha de devolución (DD/MM/AAAA): ")
            prestamo = registrar_prestamo(tarjeta, titulo_libro, fecha_prestamo, fecha_devolucion)
            print(f"\nPréstamo registrado: {prestamo['titulo_libro']} hasta el {prestamo['fecha_devolucion']}")


        #Consulta '2' para mostrar los prestamos por tarjeta


        elif opcion == '2':
            mostrar_prestamos(tarjeta)

            #para finalizar el bucle y salir de la interfaz

        elif opcion == '3':
            print("Gracias por usar el sistema de préstamos. ¡Hasta luego!")
            break
        
            #Si se genera una opción invaliuida
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()