import os
import logging

from src.leitor_pdf import ler_pdf_texto, ler_pdf_ocr
from src.extrator import extrair_dados
from src.utils import validar_dados
from src.exportador import exportar_excel


# ===============================
# CONFIGURAÇÃO DE LOG
# ===============================
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/execucao.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ===============================
# PASTAS DO PROJETO
# ===============================
PASTA_PDFS = "pdfs_entrada"
PASTA_OUTPUT = "output"
ARQUIVO_EXCEL = os.path.join(PASTA_OUTPUT, "resultado.xlsx")

os.makedirs(PASTA_OUTPUT, exist_ok=True)


# ===============================
# PROCESSAMENTO
# ===============================
resultados = []

logging.info("Início do processamento")

for arquivo in os.listdir(PASTA_PDFS):
    if arquivo.lower().endswith(".pdf"):
        caminho_pdf = os.path.join(PASTA_PDFS, arquivo)
        logging.info(f"Processando arquivo: {arquivo}")

        try:
            # 1) Tenta ler como PDF texto
            texto = ler_pdf_texto(caminho_pdf)

            # 2) Se falhar, usa OCR
            if not texto:
                logging.info(f"OCR acionado para: {arquivo}")
                texto = ler_pdf_ocr(caminho_pdf)

            # 3) Extrai dados
            dados = extrair_dados(texto)

            # 4) Valida e padroniza
            dados = validar_dados(dados)

            # 5) Adiciona nome do arquivo
            dados["Arquivo"] = arquivo

            resultados.append(dados)

        except Exception as erro:
            logging.error(f"Erro ao processar {arquivo}: {erro}")


# ===============================
# EXPORTAÇÃO E ABERTURA DO EXCEL
# ===============================
if resultados:
    exportar_excel(resultados, ARQUIVO_EXCEL)
    logging.info("Arquivo Excel gerado com sucesso")

    # Abre o Excel automaticamente (Windows)
    caminho_absoluto = os.path.abspath(ARQUIVO_EXCEL)
    os.startfile(caminho_absoluto)

else:
    logging.warning("Nenhum dado foi extraído")
    print("Nenhum dado foi extraído dos PDFs.")


logging.info("Processamento finalizado")
