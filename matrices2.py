import os 

matriz = [
    ['B', 'O', 'O', 'K', ' '],
    ['E', ' ', ' ', 'E', ' '],
    [' ', 'W', 'H', 'Y', ' '],
    [' ', 'H', ' ', ' ', ' '],
    [' ', 'I', ' ', ' ', ' '],
    [' ', 'T', 'R', 'Y', ' '],
    [' ', 'E', ' ', ' ', ' ']
]

matrizVacia = [
    ['B', '★', '★', '★', ' '],
    ['★', ' ', ' ', '★', ' '],
    [' ', 'W', '★', '★', ' '],
    [' ', '★', ' ', ' ', ' '],
    [' ', '★', ' ', ' ', ' '],
    [' ', '★', '★', 'Y', ' '],
    [' ', '★', ' ', ' ', ' ']
]

ls_palabrasAdivinadas = []

resueltaStr = '0/6' 
resueltaAux = 0

total_palabras = 6
palabras_adivinadas = 0

estado = '...' 
def fnt_juegoCrucigrama(): 
    global palabras_adivinadas, total_palabras
    ganar = False
    
    while ganar == False:
        fnt_mostrarTablero()
        
       
        if (fnt_ingresarRespuesta() == True):
            palabras_adivinadas += 1
            
        if palabras_adivinadas == total_palabras:
            ganar = True
        
    if ganar == True:
        os.system('cls')
        print("\n\n========  🤑​🤑​🤑 ​¡CONGRATS! You've completed the game 🤑​🤑​🤑  ========\n\n") 
        for i in range(len(matriz)):
            print('   '.join(matriz[i]))  
        print('\n\n')   
        print("========  🤑​🤑​🤑 ​¡CONGRATS! You've completed the game 🤑​🤑​🤑  ========\n\n") 
        
def fnt_mostrarTablero():
    global matrizVacia
    os.system('cls')
    print('......................................: [ CRUCIGRAMA ] :......................................\n\nBy:\n-Menesex\n-Km1l0\n-3ero')
    print('.........................................: [Pistas] :.........................................\n')
    print("[1]: 💡 It's something you often read for enjoyment or to learn new things                ° (4 Letters | Horizontal)")
    print("[2]: 💡 It's a verb that often indicates existence or action                              ° (2 Letters | Vertical)")
    print("[3]: 💡 It's a small object used to unlock doors or start a vehicle                       ° (3 Letters | Vertical)")
    print("[4]: 💡 It's a word often used to express curiosity or to ask about a reason or cause     ° (3 Letters | Horizontal)")
    print("[5]: 💡 It's a color often associated with purity, cleanliness, and innocence             ° (5 Letters | Vertical)")
    print("[6]: 💡 It's a word that suggests attempting to do something or testing out a possibility ° (3 Letters | Horizontal)\n")
    print('..............................................................................................')
    print('................................: [ CRUCIGRAMA TIEMPO REAL ] :................................\n')   
    
    for i in range(len(matrizVacia)):
        print('   '.join(matrizVacia[i])) 
   
    print('\n..................................: ↓ [ INSTRUCCIONES ] ↓ :..................................\n')
    print('💠 1.) Selecciona el [NÚMERO] asignado a la palabra que deseas ingresar. pj. [3]\n💠 2.) Ingresa la palabra correspondiente (sin espacios)\n')
    print(f'===============================: ↓ [  RESPONDE AQUÍ DEBAJO  ] ↓ :================================\nPalabras resueltas ({resueltaStr}) {estado}\n')

def fnt_determinarPosicion(casilla):
    global fila, columna, direccion
    while True:
        if casilla == 1:
            fila = 0
            columna = 0
            direccion = 'H'
        elif casilla == 2:
            fila = 0
            columna = 0
            direccion = 'V'
        elif casilla == 3:
            fila = 0
            columna = 3
            direccion = 'V'
        elif casilla == 4:
            fila = 2
            columna = 1
            direccion = 'H'
        elif casilla == 5:
            fila = 2
            columna = 1
            direccion = 'V'
        elif casilla == 6:
            fila = 5
            columna = 1
            direccion = 'H'
        break

def fnt_ingresarRespuesta(): 
    global matriz
    
    while True: 
        casilla = int(input("Seleccione la palabra [1] - [6])\n➡️  "))
        if casilla >= 1 and casilla <=6:
            break
        else:
            input('Por favor ingrese un número valido <ENTER>..')    
            
    while True:
        respuesta = input("Digite la palabra \n➡️​​​  ").upper()
        if respuesta != '':
            break
        else:
            input('Por favor ingrese una palabra valida <ENTER>..✌')    
    
    fnt_determinarPosicion(casilla)
    global fila, columna, direccion
    
   
    ''' Se construye la palabra objetivo (según la casilla que escoja el usuario)
    Lineas:
    palabraObjetivo = ''.join(matriz[fila][columna+i] for i in range(len(respuesta)))
    palabraObjetivo = ''.join(matriz[fila+i][columna] for i in range(len(respuesta)))
    
    !! PALABRA OBJETIVO = Usada para determinar si el usuario adivinó la palabra o no !! '''
    
    if direccion == 'H':
        if columna + len(respuesta) > len(matriz[0]):
            input("❌ ¡La palabra excede los límites de la matriz en la dirección horizontal! <ENTER>..✌")
            return False
        else:
            palabraObjetivo = ''.join(matriz[fila][columna+i] for i in range(len(respuesta)))
            
    elif direccion == 'V':
        if fila + len(respuesta) > len(matriz):
            input("❌ ¡La palabra excede los límites de la matriz en la dirección vertical! <ENTER>..✌")
            return False
        else:
            palabraObjetivo = ''.join(matriz[fila+i][columna] for i in range(len(respuesta)))
            
   
   
   
    if palabraObjetivo == respuesta:
        
        if respuesta not in ls_palabrasAdivinadas:
            ls_palabrasAdivinadas.append(respuesta)
            
      
            if direccion == 'H':
                for i in range(len(respuesta)):
                    matrizVacia[fila][columna+i] = respuesta[i]
            elif direccion == 'V':
                for i in range(len(respuesta)):
                    matrizVacia[fila+i][columna] = respuesta[i]
            
            
            
            global resueltaAux, resueltaStr, estado
            resueltaAux += 1
            resueltaStr = str(resueltaAux)+'/6'
            
            estado = '✅'
            
            return True
        else:
            input("Respuesta repetida 📄📄 <ENTER>..")
    else:
        estado = '❌'
        input("❌Respuesta incorrecta. Inténtalo de nuevo✌ <ENTER>..")
        return False
    


fnt_juegoCrucigrama() 