'''La computadora elige un número aleatorio entre 1 y 100, o el rango especificado,
y el usuario debe adivinarlo con pistas ("mayor" o "menor").
- Cuenta los intentos en los que adivinaste
- Solo permite números enteros y te dice si ingresaste algo no valido
- Pregunta si quieres volver a jugar
- Sistema de puntuación máxima
- Guarda el record en un archivo txt
- 3 niveles: fácil, medio, dificil
'''

import random
import os

NOMBRE_ARCHIVO = "record.txt"
LIMITE_INTENTOS = 100

def cargar_record():
    try:
        with open(NOMBRE_ARCHIVO, "r") as f:
            # Leemos cada línea, quitamos espacios y convertimos a int
            return [int(linea.strip()) for linea in f]
    except (FileNotFoundError, ValueError, IndexError):
        # Si el archivo no existe, creamos una lista inicial
        return [LIMITE_INTENTOS, LIMITE_INTENTOS, LIMITE_INTENTOS]

def guardar_record(nuevo_record):
    with open(NOMBRE_ARCHIVO, "w") as f:
        for n in nuevo_record:
            f.write(f'{n}\n')
            

LI = 1
LS = 100
repetir = True
c = 0
nivel_actual = ['Fácil', 'Medio', 'Difícil'] 

while repetir:
    mejor = cargar_record()
    c = 0
    print("\n" + "="*20)
    print("¡ADIVINA EL NÚMERO!")
    print("="*20)
    while True:
        try:
            s_nivel = int(input('\nElige el nivel en el que quieres jugar:\n 1. Fácil\n 2. Medio\n 3. Difícil\n'))
            if s_nivel in [1, 2, 3]:
                break
            else:
                print('Ingresa un número del 1 al 3')       
        except ValueError:
            print('Ingresa un número del 1 al 3')
            continue   
    if s_nivel == 1:
        LS = 100
    elif s_nivel == 2:
        LS = 500
    elif s_nivel == 3:
        LS = 1000
        
    s_num = random.randint(LI, LS)
        
    print('Para debug, el número es: ', s_num)
    print(f'Nivel actual: {nivel_actual[s_nivel-1]}')
    
    while True:
        try:
            u_num = int(input(f'Ingresa el número que crees que es (del {LI} al {LS}): '))
        except ValueError:
            print('Ingresa un valor válido: solo números enteros')
            continue
        
        c += 1
        if u_num < LI or u_num > LS:
            print(f'El número está entre el {LI} y el {LS}')
        elif u_num < s_num:
            print('El número es mayor')
        elif u_num > s_num:
            print('El número es menor')
        elif u_num == s_num:
            print(f'\n--- Acertaste! el número es {s_num}')
                
            if c < mejor[s_nivel - 1]:
                    mejor[s_nivel - 1] = c
                    guardar_record(mejor)
                    print(f'- Felicidades! tu nuevo record en nivel {nivel_actual[s_nivel-1]} es de {mejor[s_nivel - 1]} intentos')
            else:
                print(f'-- Te tomó {c} intentos')
                print(f'- Tu record actual es de: {mejor[s_nivel - 1]} intentos')
                
            break
    
    # lower() convierte a minusculas y strip() elimina espacios
    res_repetir = input('\n¿Quieres volver a jugar? (s = sí) (r = reiniciar record) ').lower().strip()
    if res_repetir == 's' or res_repetir == 'r':
        if res_repetir == 'r':
            mejor[s_nivel - 1] = 100
            guardar_record(mejor)
            print('Record reiniciado...')
    else:
        print('\n* Mejores puntuaciones: ')
        for i, valor in enumerate(mejor):
            if mejor[i] >= 100:
                print(f'Nivel {nivel_actual[i]}: no jugado')
            else: 
                print(f'Nivel {nivel_actual[i]}: {mejor[i]} intentos')
        print('\nGracias por jugar!')
        repetir = False