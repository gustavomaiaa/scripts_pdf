import pdfplumber
import pytesseract
from pdf2image import convert_from_path


def ler_pdf(caminho_pdf: str) -> str:
    """
    Tenta ler PDF como texto. Se falhar, usa OCR.
    """

    texto = ler_pdf_texto(caminho_pdf)

    if texto:
        print("\n================ TEXTO EXTRAÍDO (PDF TEXTO) =================\n")
        print(texto)
        print("\n=============================================================\n")
        return texto

    print(f"[INFO] Texto não encontrado em {caminho_pdf}. Usando OCR...")
    texto_ocr = ler_pdf_ocr(caminho_pdf)

    print("\n================ TEXTO EXTRAÍDO (OCR) =================\n")
    print(texto_ocr)
    print("\n=======================================================\n")

    return texto_ocr


def ler_pdf_texto(caminho_pdf: str) -> str | None:
    texto_total = ""

    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_total += texto + "\n"

    except Exception as e:
        print(f"[ERRO] Falha ao ler PDF como texto: {e}")
        return None

    return texto_total if texto_total.strip() else None


def ler_pdf_ocr(caminho_pdf: str) -> str:
    texto_total = ""

    imagens = convert_from_path(caminho_pdf)
    for img in imagens:
        texto_total += pytesseract.image_to_string(img, lang="por")

    return texto_total
