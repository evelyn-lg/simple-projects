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
NIVELES = {
    1: {'nombre': 'Fácil', 'min': 1, 'max': 100},
    2: {'nombre': 'Medio', 'min': 1, 'max': 500},
    3: {'nombre': 'Difícil', 'min': 1, 'max': 1000}
}

def cargar_record():
    try:
        with open(NOMBRE_ARCHIVO, "r") as f:
            return [int(linea.strip()) for linea in f if linea.strip().isdigit()]
    except (FileNotFoundError, ValueError, IndexError):
        return [LIMITE_INTENTOS] * len(NIVELES)

def guardar_record(records):
    with open(NOMBRE_ARCHIVO, "w") as f:
        for n in records:
            f.write(f'{n}\n')

def mostrar_records(records):
    print('\n' + "="*30)
    print("MEJORES PUNTUACIONES")
    print("="*30)
    for i, record in enumerate(records, 1):
        nombre = NIVELES[i]['nombre']
        if record >= LIMITE_INTENTOS:
            print(f"{i}. Nivel {nombre}: No jugado")
        else:
            print(f"{i}. Nivel {nombre}: {record} intentos")

def main():
    repetir = True
    records = cargar_record()
    
    while repetir:
        print("\n" + "="*30)
        print("¡ADIVINA EL NÚMERO!")
        print("="*30)
        
        # Selección de nivel
        while True:
            try:
                print("\nSelecciona un nivel:")
                for i, nivel in NIVELES.items():
                    print(f" {i}. {nivel['nombre']} ({nivel['min']}-{nivel['max']})")
                
                nivel = int(input('\nOpción: '))
                if nivel in NIVELES:
                    break
                print('Opción no válida. Elige 1, 2 o 3')
            except ValueError:
                print('Por favor, ingresa un número')
                continue
        
        config = NIVELES[nivel]
        numero_secreto = random.randint(config['min'], config['max'])
        intentos = 0
        
        print(f'\n{"-"*30}')
        print(f'Nivel: {config["nombre"]}')
        #print(f'Para debug, el número es: {numero_secreto}')
        print("-"*30)
        
        # Juego principal
        while True:
            try:
                guess = int(input(f'\nIntento #{intentos+1}: Adivina el número ({config["min"]}-{config["max"]}): '))
                intentos += 1
                
                if guess < config['min'] or guess > config['max']:
                    print(f'El número debe estar entre {config["min"]} y {config["max"]}')
                elif guess < numero_secreto:
                    print('Demasiado bajo')
                elif guess > numero_secreto:
                    print('Demasiado alto')
                else:
                    print(f'\n{"¡FELICIDADES!":^30}')
                    print(f'{"="*30}')
                    print(f'Adivinaste en {intentos} intentos')
                    print(f'Número secreto: {numero_secreto}')
                    
                    # Actualizar récord
                    if intentos < records[nivel-1]:
                        records[nivel-1] = intentos
                        guardar_record(records)
                        print(f'¡Nuevo récord en nivel {config["nombre"]}!')
                    
                    print(f'Récord actual: {records[nivel-1]} intentos')
                    break
                    
            except ValueError:
                print('Por favor, ingresa un número válido')
                continue
        
        # ¿Jugar de nuevo?
        while True:
            opcion = input('\n¿Qué quieres hacer?\n1. Jugar otra vez\n2. Ver récords\n3. Reiniciar récords\n4. Salir\n\nOpción: ').strip()
            
            if opcion == '1':
                break  # Salir solo del menú post-juego
            elif opcion == '2':
                mostrar_records(records)
            elif opcion == '3':
                records = [LIMITE_INTENTOS] * len(NIVELES)
                guardar_record(records)
                print('¡Todos los récords han sido reiniciados!')
            elif opcion == '4':
                mostrar_records(records)
                print('\n¡Gracias por jugar!')
                repetir = False
                break
            else:
                print('Opción no válida. Elige del 1 al 4')

if __name__ == "__main__":
    main()