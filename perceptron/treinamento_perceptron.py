from perceptron import Perceptron

def treinamento(perc: Perceptron, parametrosLivres, taxaAprendizado, entradas, saidasDesejadas):
    # Obter amostras de treinamento
    x = list(entradas)
    d = list(saidasDesejadas)
    n_amostras = x.__len__()
    # Inicializar parametros livres
    parametros = parametrosLivres
    perc.ajustarParametrosLivres(parametros)
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
            y = perc.processarSaida(x[i])
            # Se a saida for diferente da saida desejada
            if y != d[i]:
                # Atualizar os parametros livres do perceptron
                aux = [-1] + x[i]
                for j in range(parametros.__len__()):
                    parametros[j] += + n * (d[i] - y) * aux[j]
                perc.ajustarParametrosLivres(parametros)
                # Indicar presenca de erro
                erro = True
        # Incrementar o valor de epocas
        epocas += 1
    return epocas