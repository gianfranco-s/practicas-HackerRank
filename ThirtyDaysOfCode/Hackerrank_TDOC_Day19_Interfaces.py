class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
    # ------------------- Mi código -----------------
        divisores = []
        cont = n
        while cont >= 1:
            if self.__isDivisor(n,cont):
                divisores.append(cont)
            cont -= 1
        # No es muy eficiente, pero hace lo que me piden.
        # Acá hay una mejor implementación:
        # https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/

        sum_of_divisors = 0
        for _ in range(len(divisores)):
            sum_of_divisors += divisores[_]

        return sum_of_divisors

    def __isDivisor(self,n,pd):
        if n % pd == 0:
            return True
        else:
            return False
    # -----------------------------------------------

# n = int(input())
# my_calculator = Calculator()
# s = my_calculator.divisorSum(n)
# print("I implemented: " + type(my_calculator).__bases__[0].__name__)
# print(s)

n = 1
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print(s)