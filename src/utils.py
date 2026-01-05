import unicodedata


def normalizar_texto(texto: str) -> str:
    """
    Remove acentos, normaliza espaços e padroniza o texto
    """
    if not texto:
        return ""

    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = texto.replace("\r", "\n")

    # remove espaços duplicados
    while "  " in texto:
        texto = texto.replace("  ", " ")

    return texto.strip()


def validar_dados(dados: dict) -> dict:
    """
    Valida e padroniza os dados extraídos
    """
    if not dados:
        return dados

    dados_validados = {}

    for chave, valor in dados.items():

        # 🔹 Orçamento: mantém float válido
        if chave == "Orcamento":
            if isinstance(valor, (int, float)):
                dados_validados[chave] = float(valor)
            else:
                dados_validados[chave] = None
            continue

        # 🔹 Campos de texto
        if isinstance(valor, str):
            valor = valor.strip()
            dados_validados[chave] = valor if valor else None
        else:
            dados_validados[chave] = valor

    return dados_validados
