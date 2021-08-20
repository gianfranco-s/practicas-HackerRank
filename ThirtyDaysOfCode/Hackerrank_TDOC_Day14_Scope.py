class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        # self.maximumDifference = None   # ¿Funcionará?
        # self.maximumDifference = self.computeDifference()      # Tiene más sentido esto
	# Add your code here
    def computeDifference(self):
        
        N = len(self.__elements)
        lista = self.__elements
        maximaDif = 0
        
        for _ in range(N-1):
            for j in range(N-1):
                aux = abs(lista[0]-lista[j+1])
                if aux > maximaDif:
                    maximaDif = aux
            lista = self.__rotLeft(lista,1)
        self.maximumDifference = maximaDif
        

    # Rotar una lista hacia la izquierda
    def __rotLeft(self,a,b):
        res = a[b: len(a)] + a[0: b]
        # Explicación:
        # Ejemplo a = [1,5,7,8] | b = 2
        # a[b:len(a)] = a[2:4]  obtiene los valores desde la posición 2
        #                       hasta la posición 3 (sí, 3)
        #                       = [7,8]
        # a[0:b] = a[0:2]       obtiene los valores desde la posición 0
        #                       hasta la posición 1 (sí, 1)
        #                       = [1,5]
        # Al sumarlos, se concatenan las listas:
        # [7,8,1,5]
        return res

    

# End of Difference class


# _ = input()
# print(_)
# a = [int(e) for e in input().split(' ')]
# print(a)


d = Difference([1,2,5])
d.computeDifference()

print(d.maximumDifference)
# print(d.__elements)
# d.computeDifference