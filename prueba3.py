from os import system
import time


def menu():
    print("**************************************************")
    print("*                 Vida y Salud                   *")
    print("**************************************************")
    print("*     OPCIONES                                   *")
    print("*                                                *")
    print("* 1 - Grabar                                     *")
    print("* 2 - Buscar                                     *")
    print("* 3 - Imprimir certificados                      *")
    print("* 4 - Salir                                      *")
    print("*                                                *")
    print("**************************************************")
    opcion = int(input("ingrese su opción: "))
    if opcion > 0 and opcion <= 4:
        return opcion
    else:
        print("Opción ingresada no es valida")
        time.sleep(2)
        menu()

def valida_rut(rut):
    rut = int(rut)
    if rut > 5000000 and rut < 99999999:
        return True
    else:
        return False   


def valida_edad(edad):
    edad = int(edad)
    if edad > 18:
        return True
    else:
        return False   


def valida_estadoc(estadoc : str):
    if estadoc.upper() == 'C' or estadoc.upper() == 'S' or estadoc.upper() == 'V':
        return True
    else:
        return False 

opcion = 0  
rut = 0
rut2 = 0
nombre = ""
apellidop = ""
edad = 0
estadoc = ""  
genero = "" 
fechadeafiliacion = 0
registros = ""
  

while opcion != 4:
    system("cls")
    opcion = menu()
    if opcion == 1:
        rut = 0
        nombre = ""
        apellidop = ""
        edad = 0
        estadoc = ""
        genero = ""
        fechadeafiliacion = 0
        system("cls")
        print("Ingrese los valores solicitados")
        print("")
        nombre = input("Ingrese su nombre: ")
        apellidop = input("Ingrese su apellido paterno: ")

        
        while rut < 1:
            rut = int(input("Ingrese su rut: "))
            if not valida_rut(rut):
                system("cls")
                print("Rut ingresado no es valido")
                rut = 0
        while edad < 1:
            edad = int(input("Ingrese su edad: "))
            if not valida_edad(edad):
                system("cls")
                print("La edad ingresada no es valida")
                edad = 0
        while estadoc == "":
            estadoc = input("Ingrese su estado civil: ")
            if not valida_estadoc(estadoc):
                system("cls")
                print("Estado civil ingresado no es valido")
                estadoc = ""   
        genero = input("ingrese su genero: ")
        fechadeafiliacion = input("Ingrese fecha de afiliación: ")

    if opcion == 2:
         rut2 = int(input("Ingrese su rut: "))
         if rut2 == rut:
            system("cls")
            print("Buscar")
            print("Paciente registrado en el sistema")
            system("cls")
            print("*******************************")
            print("*       Datos Registrados     *")
            print("*******************************")
            print("Nombre: " + str(nombre))
            print("Apellido Paterno: " + str(apellidop))
            print("Rut: " + str(rut))
            print("Edad: " + str(edad))
            print("Estado Civil: " + estadoc)
            print("Género: " + genero )
            print("Fecha de Afiliación: " + fechadeafiliacion)
            print("")
            print("")        
            input("Presione Enter para continuar...")  
      
    if opcion == 3:
        print("imprimir certificados de afiliación a la Isapre")
        rut3 = int(input("Ingrese su rut para imprimir certificado: "))
        if rut3 == rut:
            print("Paciente registrado en el sistema")
            system("cls")
            print("*******************************")
            print("*   Afiliación a la Isapre    *")
            print("*******************************")
            print("Datos Personales: ")
            print("Nombre: " + str(nombre))
            print("Apellido Paterno: " + str(apellidop))
            print("Rut: " + str(rut))
            print("Edad: " + str(edad))
            print("Estado Civil: " + estadoc)
            print("Género: " + genero )
            print("Fecha de Afiliación: " + fechadeafiliacion)
            print("")
            print("")        
            input("Presione Enter para continuar...")  

    if opcion == 4:
        print("Salir de Sistema")
      





