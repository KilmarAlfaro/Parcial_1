"""Un consultorio médico atiende a una serie de pacientes, solo está una
secretaria y en el consultorio hay varios doctores cada paciente llega y
deja sus datos además del motivo de su consulta y posteriormente la
secretaria les asigna la fecha de su consulta.
 En el caso que una persona ya tenga una consulta previa en lugar
de tomar datos se le pasará a sala de esperas. Implementa esta
problemática a tu código"""

"""En esta primera parte haremos una función para alamacenar las citas de los pacientes para que
el identificador que en nuestro caso sería el nombre nos suelte los datos que serían la fecha y 
el motivo de la consulta"""

citas = {}

def registrar_paciente(nombre, motivo):

    #si el nombre del paciente ya pertenece al diccionario significa que ya tiene cita y se enviará a la sala de espera

    if nombre in citas:
        print(f"El paciente {nombre} ya tiene una cita previa y ha sido enviado a sala de espera.")
        
        #si no está registrado lo registramos en el diccionario 'citas'
        
    else:
        fecha_cita = input("Ingrese la fecha en la que se desea registrar la cita (DD/MM/AAAA): ")
        citas[nombre] = {'motivo': motivo, 'fecha': fecha_cita}
        print(f"El Paciente {nombre} se ha registrado con cita para el {fecha_cita}.")


#ahora una función para cuando querramos saber los pacientes registrados

def mostrar_pacientes():

   #con len sabremos si hay registros en el diccionario 'cilentes' lo cual si es 0 nos indicara que no hay

    if len(citas) == 0:
        print("No hay pacientes registrados.")
        
        #si los hay simplemente nos mostrara los registros presentes en el diccionario

    else:
        for nombre, info in citas.items():
            print(f"Paciente: {nombre}, Motivo: {info['motivo']}, Fecha de Cita: {info['fecha']}")


"""luego haremos un while para presentar las opciones que tiene la secretaria para consultar
pudiendo seleccionarlas con 1 para registrar un paciente, 2 para mostrar los pacientes ya registrados y 3
si desea terminar el proceso de registro"""


def main():
    while True:
        print("\n--- Consultorio Médico ---")
        print("1. Registrar paciente")
        print("2. Mostrar pacientes")
        print("3. Salir")

        opcion = input("Seleccione una opción (1/2/3): ")
        

        """En esta sección podremos ingresar el nombre del paciente para luego ejecutar la función de mas arriba
        llamada registar_paciente en el cuál incluiremos nombre, motivo y fecha de la consulta"""


        if opcion == '1':
            nombre = input("Ingrese el nombre del paciente: ")
            motivo = input("Ingrese el motivo de la consulta: ")
            registrar_paciente(nombre, motivo)


            #En esta sección simplemete ejecutaremos la función de mas arribita llamada mostrar_pacientes


        elif opcion == '2':
            mostrar_pacientes()


            #y si terminamos con los registros simplemte salimos del bucle while con el break


        elif opcion == '3':
            print("Saliendo del programa.")
            break


            #si no seleccionamos una opción válida nos presentara un aviso de error y volveremos a intentarlo por el while


        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()