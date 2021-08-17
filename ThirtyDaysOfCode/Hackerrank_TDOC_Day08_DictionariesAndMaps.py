def phone_book_input(N):
    '''
    Toma como entradas, pares de nombre y numero de telefono.
    Devuelve un diccionario con los datos.
    '''
    phonebook = {}
    name = []
    number = []
    for entry in range(N):
        name_number = input().strip()
        name_number = name_number.split()
        name = name_number[0]
        number = name_number[1]
        phonebook[name]=number
    return phonebook

def pedidos():
    '''
    Toma la lista de pedidos del teclado, hasta que uno de ellos es vacio.
    '''
    newQuery = input().strip()
    queryList = []
    while newQuery != '':
        queryList.append(newQuery)
        
        try:
            newQuery = input().strip()
        except EOFError:  # Si no, no lo agarra Hackerrank
            break
  
    return queryList

def buscar_si_pertenece(lista,diccionario):
    for cont in range(len(lista)):
        elemento = lista[cont]
        if elemento in diccionario:
            print(f'{elemento}={diccionario[elemento]}')
        else:
            print("Not found")



if __name__ == '__main__':
    n = int(input().strip())
    phoneBook = phone_book_input(n)
    
    queryList = pedidos()
    
    buscar_si_pertenece(queryList,phoneBook)
    
