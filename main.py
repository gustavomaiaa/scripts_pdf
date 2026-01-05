import os
import logging

from src.leitor_pdf import ler_pdf_texto, ler_pdf_ocr
from src.extrator import extrair_dados
from src.utils import validar_dados
from src.exportador import exportar_excel
from datetime import datetime


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
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
ARQUIVO_EXCEL = os.path.join(PASTA_OUTPUT, f"resultado_{timestamp}.xlsx")
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
            # 1) Lê PDF como texto
            texto = ler_pdf_texto(caminho_pdf)

            if not texto:
                logging.warning(f"Texto vazio em {arquivo}")
                continue

            # 2) Extrai dados (ASSINATURA CORRETA)
            dados = extrair_dados(texto, arquivo)
            print("DEBUG:", dados)

            # 3) Validação mínima (CAMPO-CHAVE)
            if not dados or not dados.get("Municipio"):
                logging.warning(f"Dados inválidos em {arquivo}")
                continue

            # 4) Validação complementar (opcional)
            dados = validar_dados(dados)

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
