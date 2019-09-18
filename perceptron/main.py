import random as rd
import excel_operations as ex
from perceptron import Perceptron, funcaoDegrauBipolar

N_ENTRADAS = 3
N_TESTES = 5
TAXA_APRENDIZADO = 0.01
ARQUIVO_TREINAMENTO = r'Treinamento_Perceptron.xls'
ARQUIVO_TESTES = r'Teste_Perceptron.xls'

def gerarParametrosIniciais(entradas):
    lista = [0.0] * entradas
    for i in range(lista.__len__()):
        lista[i] = rd.uniform(0, 1)
    return lista

param_teste = []
for i in range(N_TESTES):
    param_teste.append(gerarParametrosIniciais(N_ENTRADAS+1))

# LOG DO TREINAMENTO
f = open('treinamento.txt', 'w')
f.write('PARAMETROS LIVRES DE TREINAMENTO INICIAIS\n')
for i in range(N_TESTES):
    f.write('TREINAMENTO ' + str(i+1) + ': ')
    for j in range(N_ENTRADAS+1):
        f.write('w' + str(j) + '=' + str(param_teste[i][j]) + ', ')
    f.write('\n')
f.close()
# FIM DE SESSAO DE LOG

# Carregando entradas das amostras de treinamento e saidas desejadas
entradas_treinamento = ex.getEntradas(ARQUIVO_TREINAMENTO)
saidas_treinamento = ex.getSaidasDesejadas(ARQUIVO_TREINAMENTO)

# Inicializando os perceptrons de treinamento
perceptrons = []
for i in range(N_TESTES):
    perceptrons.append(Perceptron([], funcaoDegrauBipolar))

# Realizando treinamento
epocas = []
for i in range(N_TESTES):
    epocas.append(perceptrons[i].treinamento(param_teste[i], TAXA_APRENDIZADO, entradas_treinamento, saidas_treinamento))

# LOG DO TREINAMENTO
f = open('treinamento.txt', 'a')
f.write('\nPARAMETROS LIVRES FINAIS E NUMERO DE EPOCAS DE TREINAMENTO\n')
for i in range(N_TESTES):
    f.write('TREINAMENTO ' + str(i+1) + ': ')
    for j in range(N_ENTRADAS+1):
        f.write('w' + str(j) + '=' + str(perceptrons[i].w[j]) + ', ')
    f.write('epocas=' + str(epocas[i]) + '\n')
f.close()
# FIM DE SESSAO DE LOG

# Carregando amostras de operacao
amostras = ex.getEntradas(ARQUIVO_TESTES)
N_AMOSTRAS = amostras.__len__()

# Realizando processamento das amostras pelos perceptrons treinados
saidas = []
for i in range(N_AMOSTRAS):
    saidas.append([])
    for j in range(N_TESTES):
        saidas[i].append(perceptrons[j].operacao(perceptrons[j].w, amostras[i]))

# LOG DAS OPERACOES NAS AMOSTRAS
f = open('treinamento.txt', 'a')
f.write('\nRESULTADO DO PROCESSAMENTO DAS AMOSTRAS PELOS PERCEPTRONS TREINADOS\n')
for i in range(N_AMOSTRAS):
    f.write('AMOSTRA ' + str(i+1) + ': ')
    for j in range(N_TESTES):
        f.write('PERCEPTRON ' + str(j+1) + '=' + saidas[i][j] + ', ')
    f.write('\n')
# FIM DE SESSAO DE LOG