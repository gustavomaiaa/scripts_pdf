import re
from src.utils import normalizar_texto


def extrair_dados(texto_pdf: str, nome_arquivo: str = "") -> dict:
    """
    Extrai dados estruturados do texto de um PDF.
    """

    texto = normalizar_texto(texto_pdf)

    def buscar(padrao):
        match = re.search(padrao, texto, re.IGNORECASE)
        return match.group(1).strip() if match else None

    municipio = buscar(r"municipio\s*:?\s*(.+)")
    estado = buscar(r"estado\s*:?\s*([A-Z]{2})")
    data = buscar(r"data\s*:?\s*(\d{2}/\d{2}/\d{4})")

    # 🔴 REGEX ROBUSTO PARA ORÇAMENTO
    orcamento_raw = buscar(
        r"orcamento\s*:?\s*(?:r\$)?\s*([\d\.]+,\d{2})"
    )

    prefeito = buscar(r"prefeito\s*:?\s*(.+)")
    secretario = buscar(r"secretario\s*financeiro\s*:?\s*(.+)")

    orcamento = tratar_orcamento(orcamento_raw)

    return {
        "Municipio": municipio,
        "Estado": estado,
        "Data": data,
        "Orcamento": orcamento,
        "Prefeito": prefeito,
        "Secretario_Financeiro": secretario,
        "Arquivo": nome_arquivo
    }


def tratar_orcamento(valor: str):
    """
    Converte '12.450.000,00' → 12450000.00
    """
    if not valor:
        return None

    valor = valor.replace(".", "").replace(",", ".")
    try:
        return float(valor)
    except ValueError:
        return None
