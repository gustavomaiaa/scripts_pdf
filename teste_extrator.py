from src.leitor_pdf import ler_pdf_texto
from src.extrator import extrair_dados

caminho_pdf = "pdfs_entrada/alphanorte.pdf"
#caminho_pdf = "pdfs_entrada/betaverde.pdf"
#caminho_pdf = "pdfs_entrada/gamazul.pdf"

texto = ler_pdf_texto(caminho_pdf)

print("\n====== TEXTO EXTRAÍDO ======\n")
print(texto)

dados = extrair_dados(texto, "alpharnorte.pdf")

print("\n====== DADOS EXTRAÍDOS ======\n")
print(dados)
