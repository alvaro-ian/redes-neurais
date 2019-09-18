from perceptron import Perceptron
from treinamento_perceptron import treinamento
import excel_operations as ex

arquivo = r'Treinamento_Perceptron.xls'

p2 = Perceptron([])
treinamento(p2, [0, 0, 0, 0], 0.01, ex.getEntradas(arquivo), ex.getSaidasDesejadas(arquivo))

print(p2.w)