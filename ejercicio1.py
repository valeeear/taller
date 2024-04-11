diccionario = {}
import os
sw = True
os.system('cls')


def fnt_agregar(diccionario, nombre, telefono):
    os.system('cls')
    if nombre == '' or telefono == '':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[nombre] = {'Telefono': telefono}
        enter = input(f'\nLa persona {nombre} ha sido registrada con éxito <ENTER>')
    


def fnt_selector():
        os.system('cls')
        nombre = input('Nombre: ')
        telefono = input('Telefono: ')
        fnt_agregar(diccionario, nombre, telefono)

def fnt_buscar():
    os.system('cls')
    if buscar in diccionario:
        print(diccionario [buscar])
        enter = input('\n Presiona <ENTER> para continuar')
        
    else:
        print("El contacto no se encuentra en la agenda.")
        
while sw == True:
    
    opcion = input('1. Registrar\n2. Buscar\n3. Salir\n-->  ')
    if opcion == '1':
        fnt_selector()
    elif opcion == '2':
        buscar = input('Ingrese el nombre del personal: ')
        fnt_buscar()

    elif opcion == '3':
        sw = False
