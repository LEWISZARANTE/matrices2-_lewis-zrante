import os
mtrz_abecedario = [['A','B','C','D','E','F'],
                   ['G','H','I','J','K','L'],
                   ['M','N','Ñ','O','P','Q'],
                   ['R','S','T','U','V','W'],
                   ['X','Y','Z','CH','LL','RR']
                    ]
mtrz_rellenar = [['🕳', '🕳', '🕳', '🕳', '🕳', '🕳'],
                 ['🕳', '🕳', '🕳', '🕳', '🕳', '🕳'],
                 ['🕳', '🕳', '🕳', '🕳', '🕳', '🕳'],
                 ['🕳', '🕳', '🕳', '🕳', '🕳', '🕳'],
                 ['🕳', '🕳', '🕳', '🕳', '🕳', '🕳']]
def fnt_impresion_matriz():
    os.system('cls')
    for i in range(len(mtrz_rellenar)):
        for b in range(len(mtrz_rellenar[i])):
            if b == len(mtrz_rellenar[i])-1:
                print(mtrz_rellenar[i][b])
            else:
                print(mtrz_rellenar[i][b], end='\t')
    print('\n\n')
def fnt_rellenar(dato,fila,columna):
    salir = False
    for i in range (len(mtrz_abecedario)):
        for b in range (len(mtrz_abecedario[i])):
            if dato == mtrz_abecedario[fila][columna]:
                mtrz_rellenar[fila][columna] = dato
                input(f'{dato} Agregado correctamente')
                salir = True
                break
            else:
                input(f'Posición invalida para {dato}')
                salir = True
                break
        if salir:
            break
                
while (True):
    fnt_impresion_matriz()
    fnt_rellenar(input('Dato: ').upper(),int(input('Fila: ')),int(input('Columna: ')))