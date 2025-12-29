import csv
import os

NOMBRE_ARCHIVO = "contactos.csv"
contactos = []

def menu():
    while True:
        print('\n - Menú - ')
        print('1. Agregar contacto')
        print('2. Mostrar contactos')
        print('3. Salir')
        try:
            opc = int(input())
            if opc in range(1,5):
                break
            print('Elige una opción válida')
        except ValueError:
            print('Elige una opción válida')
            continue            
    return opc

def guardar_contactos():
    try:
        with open(NOMBRE_ARCHIVO, mode='w', newline='', encoding='utf-8') as file:
            if contactos:
                encabezado = ['nombre', 'telefono', 'email']
                writer = csv.DictWriter(file, fieldnames=encabezado)
                writer.writeheader()
                writer.writerows(contactos)
        print(f'Contacto guardado exitosamente en {NOMBRE_ARCHIVO} - {len(contactos)} contactos')
    except Exception as e:
        print(f'Error al guardar contactos: {e}')

def obtener_contactos():
    try:
        if not os.path.exists(NOMBRE_ARCHIVO):
            print('Archivo no encontrado, se creará uno nuevo')
            return
        
        with open(NOMBRE_ARCHIVO, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            c = list(reader)
        # print(f'No. de contactos guardados: {len(c)}')
        return c
    except Exception as e:
        print(f'Error al cargar contactos: {e}')
        c = []

def agregar_contacto():
    print("\n--- AGREGAR CONTACTO ---")
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    
    if not nombre:
        print('El nombre no puede estar vacío')
        return
    
    nuevo_contacto = {
        'nombre': nombre,
        'telefono': telefono,
        'email': email
    }
    
    contactos.append(nuevo_contacto)
    guardar_contactos()
    # print(f'Contacto {nombre} agregado correctamente')

def listar_contactos():
    print("\n--- LISTA DE CONTACTOS ---")
    if not contactos:
        print('No hay ningun contacto guardado')
        return
    print(f'Total de contactos: {len(contactos)}')
    mostrar_contactos(contactos)

def mostrar_contactos(lista_contactos):
    if not lista_contactos:
        print('No hay contactos registrados')
        return
    print('='*60)
    print(f"{'Nombre':<20} {'Telefono':<15} {'Email':25}")
    print('='*60)
    for contacto in lista_contactos:
        nombre = contacto['nombre'][:18] + '..' if len(contacto['nombre']) > 20 else contacto['nombre']
        telefono = contacto['telefono'][:13] + '..' if len(contacto['telefono']) > 15 else contacto['telefono']
        email = contacto['email'][:23] + '..' if len(contacto['email']) > 25 else contacto['email']
        print(f'{nombre:<20} {telefono:<15} {email:<25}')
    print('='*60)
    


    
contactos = obtener_contactos()
listar_contactos()
while True:
    opcion = menu()
    if opcion == 1:
        agregar_contacto()
    elif opcion == 2:
        listar_contactos()
    elif opcion == 3:
        break
    
