import pandas as pd

def exportar_excel(lista_dados, caminho_saida):
    df = pd.DataFrame(lista_dados)
    df.to_excel(caminho_saida, index=False)
