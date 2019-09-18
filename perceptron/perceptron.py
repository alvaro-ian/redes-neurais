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

    def treinamento(self, parametrosLivres, taxaAprendizado, entradas, saidasDesejadas):
        # Obter amostras de treinamento
        x = list(entradas)
        d = list(saidasDesejadas)
        n_amostras = x.__len__()
        # Inicializar parametros livres
        parametros = parametrosLivres
        self.w = parametrosLivres
        # Especificar taxa de aprendizado
        n = taxaAprendizado
        # Inicializar contador de epocas
        epocas = 0
        # Inicializar erro
        erro = 1
        #Enquanto existir erro
        while erro:
            # Inexiste erro
            erro = False
            # Para cada amostra
            for i in range(n_amostras):
                # Calcular saida para aquela amostra
                y = self.processarSaida(x[i])
                # Se a saida for diferente da saida desejada
                if y != d[i]:
                    # Atualizar os parametros livres do perceptron
                    aux = [-1] + x[i]
                    for j in range(parametros.__len__()):
                        parametros[j] += n * (d[i] - y) * aux[j]
                    self.w = parametros
                    # Indicar presenca de erro
                    erro = True
            # Incrementar o valor de epocas
            epocas += 1
        return epocas
    
    def operacao(self, parametrosTreinados, amostra):
        # Obter a amostra a ser classificada
        x = list(amostra)
        # Utilizar parametros resultantes do treinamento
        self.w = parametrosTreinados
        # Processar saida com relacao a amostra do perceptron treinado
        y = self.processarSaida(x)
        if y == 1:
            return "P2"
        elif y == -1:
            return "P1"