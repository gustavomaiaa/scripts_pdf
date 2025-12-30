import re

def extrair_dados(texto):
    dados = {}

    padroes = {
        "Municipio": r"Município:\s*(.*)",
        "Estado": r"Estado:\s*([A-Z]{2})",
        "Data": r"Data:\s*(\d{2}/\d{2}/\d{4})",
        "Orcamento": r"Orçamento:\s*R\$\s*([\d\.,]+)",
        "Prefeito": r"Prefeito:\s*(.*)",
        "Secretario_Financeiro": r"Secretário Financeiro:\s*(.*)"
    }

    for campo, padrao in padroes.items():
        resultado = re.search(padrao, texto)
        dados[campo] = resultado.group(1).strip() if resultado else None

    return dados
