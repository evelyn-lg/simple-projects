'''La computadora elige un número aleatorio entre 1 y 100,
y el usuario debe adivinarlo con pistas ("mayor" o "menor").
Conceptos: random.randint(), bucles while, comparaciones.
- Cuenta los intentos en los que adivinaste
'''

import random

LI = 1
LS = 100
s_num = random.randint(LI, LS)
c = 0

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
        print(f'Felicidades, acertaste! el número es {s_num}')
        print(f'Te tomó {c} intentos')
        
        break
    
        
