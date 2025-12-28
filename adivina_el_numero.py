'''La computadora elige un número aleatorio entre 1 y 100, o el rango especificado,
y el usuario debe adivinarlo con pistas ("mayor" o "menor").
- Cuenta los intentos en los que adivinaste
- Solo permite números enteros y te dice si ingresaste algo no valido
- Pregunta si quieres volver a jugar
- Sistema de puntuación máxima
'''

import random

LI = 1
LS = 100
repetir = True
c = 0
mejor = float('inf')

while repetir:
    s_num = random.randint(LI, LS)
    c = 0
    print("\n" + "="*20)
    print("¡ADIVINA EL NÚMERO!")
    print("="*20)
    print('Para debug, el número es: ', s_num)
    
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
            
            if c < mejor:
                mejor = c
                print(f'- Felicidades! tu nuevo record es de {mejor} intentos')
            else:
                print(f'-- Te tomó {c} intentos')
                print(f'- Tu record actual es de: {mejor} intentos')
            break
    
    # lower() convierte a minusculas y strip() elimina espacios
    res_repetir = input('\n¿Quieres volver a jugar? (s = sí) ').lower().strip()
    if res_repetir != 's':
        if mejor != float('inf'):
            print(f'\nTu mejor récord fue de {mejor} intentos')
        print('Gracias por jugar!')
        repetir = False

        
        
    
        
