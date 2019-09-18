import pandas as pd

ENTRADAS = ['x1', 'x2', 'x3']
SAIDAS_DESEJADAS = ['d']

def getEntradas(fileName):
    df = pd.read_excel(fileName)
    lista = []
    for i in range(len(df.index)):
        lista.append(df.loc[i, ENTRADAS].tolist())
    return lista

def getSaidasDesejadas(fileName):
    df = pd.read_excel(fileName)
    lista = df['d'].tolist()
    return lista