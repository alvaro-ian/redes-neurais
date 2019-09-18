from perceptron import Perceptron

def operacao(perc: Perceptron, parametrosTreinados, amostra):
    # Obter a amostra a ser classificada
    x = list(amostra)
    # Utilizar parametros resultantes do treinamento
    perc.ajustarParametrosLivres(parametrosTreinados)
    # Processar saida com relacao a amostra do perceptron treinado
    y = perc.processarSaida(x)
    if y == 1:
        return "P2"
    elif y == -1:
        return "P1"