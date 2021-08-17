def invertir(N,lista):
    lista = lista[:N]
    cont = N-1
    while cont >= 0:
        print(lista[cont],'',end='')
        cont -= 1
    print("")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    # print(arr)
    invertir(n,arr)
