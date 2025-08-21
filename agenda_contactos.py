
import re

def mostrar_menu():
    print("\n Bienvenidos a la Agenda de Contactos:")
    print("1. Adicionar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contacto")
    print("5. Salir del programa")
    print(("*" * 20))

def validar_email(correo):
  patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  return bool(re.match(patron, correo))

def agregar_contacto(agenda):
    nombre = input("Por favor ingrese el nombre del contacto: ")
    if nombre in agenda:
        print(f"El contacto {nombre} ya existe en la agenda")
        return
    while True:
      telefono = input("Por favor ingrese el número de teléfono del contacto: ")
      if telefono.isdigit() and (len(telefono) > 7 and len(telefono) <= 11):
             break
      else:  
             print("El número de teléfono ingresado no es válido. Debe contener solo dígitos y tener al menos 8 caracteres.")
    while True:
       correo = input("Por favor ingrese el correo electrónico del contacto: ")
       resultado_validacion = validar_email(correo)
       if resultado_validacion:
             agenda[nombre] = {"telefono": telefono, "correo": correo} 
             print(f"El contacto {nombre} fue agregado exitosamente")
             break  
       else:
             print("El correo electrónico ingresado no tiene un formato válido. Por favor, intente nuevamente")

def eliminar_contacto(agenda):
    nombre = input("Por favor ingrese el nombre del contacto que desea eliminar: ") 
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} fue eliminado exitosamente")   
    else:
        print(f"El contacto {nombre} no existe en la agenda")

def buscar_contacto(agenda):
    nombre = input("Por favor ingrese el nombre del contacto que desea buscar: ")   
    if nombre in agenda:
        contacto = agenda[nombre]
        print(f"Los datos del contacto {nombre} son: \nTeléfono: {contacto['telefono']} \nCorreo: {contacto['correo']}") 
    else:
        print(f"El contacto {nombre} no existe en la agenda")

def listar_contactos(agenda):
    if not agenda:
        print("La agenda de contactos está vacía")
        return
    else:
        print("Lista de contactos:")
        for nombre, datos in agenda.items():
          print(f"Nombre: {nombre}\nTeléfono: {datos['telefono']}\nCorreo: {datos['correo']}")
          print("-" * 20)


def agenda_contactos():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("Por favor seleccione el numero de la opción que desea realizar: ")
        print("\n")
        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            eliminar_contacto(agenda)    
        elif opcion == '3':
            buscar_contacto(agenda)
        elif opcion == '4':
            listar_contactos(agenda)    
        elif opcion == '5':
            print("Usted ha salido de la Agenda de Contactos. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, debe entrar un numero del 1 al 5")
       
agenda_contactos()