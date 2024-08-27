usuarios = []

def menu():
    """
    Esta función muestra el menú principal del sistema.
    Permite al usuario seleccionar entre diferentes opciones.
    
    """
    print("\nBienvenido al Sistema de Reservas de vuelos")
    print("1. Registrar nuevo Usuario")
    print("2. Mostrar Usuarios registrados")
    print("3. Actualizar información de un Usuario")
    print("4. Eliminar un Usuario")
    print("5. Salir")
    opcion = input("Elige una opción (1/2/3/4/5): ")
    return opcion

def registrar_usuarios():
    """
    Esta función permite registrar un nuevo usuario en el sistema.
    Pide al usuario ingresar el nombre .
    """
    nombre = input("Ingresa el nombre del usuario: ")

    usuarios.append(nombre)
    print(f"Usuario {nombre} registrado con éxito.")
        
def mostrar_usuarios():
    """
    Esta función muestra la lista de estudiantes registrados.
    Si no hay estudiantes registrados, informa al usuario.
    """
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        print("Lista de usuarios registrados:")
        for i, usuarios in enumerate(usuarios, start=1):
            print(f"{i}. Nombre: {usuarios['nombre']}, Edad: {usuarios['edad']}")     
            
def actualizar_usuarios():
    """
    Esta función permite actualizar la información de un estudiante existente.
    Busca al estudiante por su nombre y permite modificar su nombre y edad.
    """
    nombre = input("Ingresa el nombre del estudiante que deseas actualizar: ")
    for usuarios in usuarios:
        if usuarios['nombre'] == nombre:
            print(f"usuarios encontrado: {nombre}")
            nuevo_nombre = input("Ingresa el nuevo nombre (o presiona Enter para no cambiarlo): ")
           

            # Solo actualizamos si el usuario ingresó nuevos valores
            if nuevo_nombre:
                usuarios['nombre'] = nuevo_nombre
           
            print(f"Estudiante {nombre} actualizado con éxito.")
            return
    
    print(f"No se encontró ningún usuario con el nombre {nombre}.")
    
def eliminar_usuarios():
    """
    Esta función permite eliminar a un usuarios del sistema.
    Busca al estudiante por su nombre y lo elimina de la lista.
    """
    nombre = input("Ingresa el nombre del estudiante que deseas eliminar: ")
    for usuarios in usuarios:
        if usuarios['nombre'] == nombre:
            usuarios.remove(usuarios)
            print(f"usuarios {nombre} eliminado con éxito.")
            return
    
    print(f"No se encontró ningún usuario con el nombre {nombre}.")
        
def main():
    """
    Función principal que controla el flujo del programa.
    Usa un bucle while para mostrar el menú y realizar las acciones según la elección del usuario.
    """
    while True:
        opcion = menu()
        if opcion == '1':
            registrar_usuarios()
        elif opcion == '2':
            mostrar_usuarios()
        elif opcion == '3':
            actualizar_usuarios()
        elif opcion == '4':
            eliminar_usuarios()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Ejecutamos la función principal para iniciar el programa
main()   