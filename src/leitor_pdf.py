import pdfplumber
import pytesseract
from pdf2image import convert_from_path

def ler_pdf_texto(caminho_pdf):
    texto_total = ""
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_total += texto + "\n"
    except Exception:
        return None
    return texto_total if texto_total.strip() else None

def ler_pdf_ocr(caminho_pdf):
    texto_total= ""
    imagens = convert_from_path(caminho_pdf)
    for img in imagens:
        texto_total += pytesseract.image_to_string(img, lang='por') 

    return texto_total 
