
def ingresar(n):
    '''
    Toma una cantidad n de elementos ingresados por teclado, y los guarda en una      
    variable S
    '''
    S = []
    for cont in range(n):
        S.append(input().strip())
    return S

def separar(S,N):
    '''
    Toma un arreglo de N strings, y opera sobre cada uno.
    '''
    
    for nroElem in range(N):
        U = ''
        V = ''
        palabra = S[nroElem]
        for idxLetra in range(len(palabra)):
            if idxLetra%2 == 0:
                U+=palabra[idxLetra]
            else:
                V+=palabra[idxLetra]
        print(U+' '+V)


if __name__ == '__main__':
    T = int(input().strip())
    S = ingresar(T)
    separar(S,T)

    
