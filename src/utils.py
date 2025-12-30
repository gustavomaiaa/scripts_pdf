from datetime import datetime

def validar_dados(dados):
    # Município
    if not dados["Municipio"]:
        dados["Municipio"] = "NÃO IDENTIFICADO"

    # Estado
    if not dados["Estado"]:
        dados["Estado"] = "NA"

    # Data
    try:
        datetime.strptime(dados["Data"], "%d/%m/%Y")
    except:
        dados["Data"] = None

    # Orçamento
    try:
        dados["Orcamento"] = float(
            dados["Orcamento"]
            .replace(".", "")
            .replace(",", ".")
        )
    except:
        dados["Orcamento"] = 0.0

    # Prefeito
    if not dados["Prefeito"]:
        dados["Prefeito"] = "NÃO INFORMADO"

    # Secretário Financeiro
    if not dados["Secretario_Financeiro"]:
        dados["Secretario_Financeiro"] = "NÃO INFORMADO"

    return dados
