#peliculas

mi_diccionario = {}
import os
sw = True

def fnt_agregar(mi_diccionario, nombre, genero, año):
    if nombre == '' or genero == '' or año == '':
        enter= input('Debe diligenciar toda la información...>ENTER<')
    else:
        mi_diccionario[nombre] = {'GÉNERO': genero, 'AÑO': año}
        enter = input('\n\nLa pelicula ha sido registrada.Presione ENTER para continuar...')
        
def fnt_registro():
    nombre = input('Ingrese el nombre de la pelicula:  ') 
    genero = input('Ingrese su genero:  ')
    año = input('Ingrese el año de creación:  ')
    fnt_agregar(mi_diccionario, nombre, genero, año)

def fnt_buscar():
    if buscar in mi_diccionario:
        print(mi_diccionario[buscar])
    else:
        print('La pelicula no se encuentra registrada')
        enter = input('\n\nPresione ENTER para continuar...')
        
while sw == True:
    opcion = input('\n1. REGISTRAR\n2. BUSCAR\n3. SALIR\n->')
    if opcion == '1':
        fnt_registro()
    if opcion == '2':
        buscar = input('Ingrese el nombre de la pelicula a buscar:  ')
        fnt_buscar()
    if opcion == '3':
        sw = False
    