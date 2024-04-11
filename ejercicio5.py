#libros

mi_diccionario = {}
import os
sw = True

def fnt_agregrar(mi_diccionario, titulo,autor, genero):
    os.system('cls')
    if titulo == '' or autor == '' or genero == '':
        enter = input('Debe diligenciar toda la información solicitada >ENTER<')
    else:
        mi_diccionario[titulo] = {'AUTOR': autor, 'GENERO': genero}
        enter = input(f'\nEl libro {titulo} ha sido registrado con éxito <ENTER>')
        
def fnt_registro():
    os.system('cls')
    titulo = input('Ingrese el titulo del libro:  ')
    autor = input('Ingrese el autor del libro:  ')
    genero = input('Ingrese el genero del libro:  ')
    fnt_agregrar(mi_diccionario, titulo, autor, genero)
    
def fnt_buscar():
    os.system('cls')
    if buscar in mi_diccionario:
        print(mi_diccionario[buscar])
    else:
        print('No se encontró el libro')
        
while sw == True:
    opcion = input('1. REGISTRAR\n2. BUSCAR\n3. SALIR\n->')
    if opcion == '1':
        fnt_registro()
    if opcion == '2':
        buscar =input('Ingrese el nombre del libro:  ')
        fnt_buscar()
    if opcion == '3':
        sw = False
    