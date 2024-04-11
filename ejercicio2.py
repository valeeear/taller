#inventario

mi_diccionario ={}
import os
sw = True

def fnt_agregar(mi_diccionario, producto, cantidad):
    if producto == '' or cantidad == '':
        enter = input('Debe diligenciar toda la información solicitada >ENTER<')
    else:
        mi_diccionario[producto] = {'CANTIDAD': cantidad}
        enter = input('\n\nProducto agregado >ENTER<')
        
def fnt_selector():
    producto = input('Ingrese el producto:  ')
    cantidad = input('Ingrese la cantidad:  ')
    fnt_agregar(mi_diccionario, producto, cantidad)
    
def fnt_buscar():
    if buscar in mi_diccionario:
        print(mi_diccionario[buscar])
    else:
        print('El producto no se encuentra registrado')
        enter = input('\n\nPresione >ENTER< para continuar')

while sw == True:
    opcion= input('\n1. REGISTRAR\n2. BUSCAR\n3. SALIR\n->')
    if opcion == '1':
        fnt_selector()
    if opcion == '2':
        buscar = input('Ingrese el producto:  ')
        fnt_buscar()
    if opcion == '3':
        sw = False  