def funcaoDegrau(x):
    if x >= 0:
        return 1
    return 0

def funcaoDegrauBipolar(x):
    if x >= 0:
        return 1
    return -1


class Perceptron:

    def __init__(self, w, g):
        self.w = w
        self.g = g

    def funcaoAtivacao(self, u):
        return self.g(u)

    def calculaPotencialAtivacao(self, x):
        x = [-1] + x
        aux = []
        soma = 0
        for i in range(self.w.__len__()):
            aux.append(self.w[i]*x[i])
            soma += aux[i]
        return soma
    
    def processarSaida(self, x):
        if x.__len__() == self.w.__len__()-1:
            return self.funcaoAtivacao(self.calculaPotencialAtivacao(x))
        return "Número de entradas incompatível, este Perceptron trabalha com " + str(self.w.__len__()-1) + " entradas"

    def ajustarParametrosLivres(self, w):
        self.w = w