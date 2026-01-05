# 📄 Scripts de Leitura de PDFs e Exportação para Excel

Projeto em **Python** para automação da leitura de arquivos **PDF** contendo dados estruturados (municípios, orçamento, datas, etc.) e exportação automática para **Excel**, com tratamento adequado de dados numéricos.

---

## 🎯 Objetivo

Automatizar o processo de:
- Leitura de múltiplos PDFs
- Extração de informações textuais e numéricas
- Validação e padronização dos dados
- Geração de planilha Excel pronta para análise

O projeto foi desenvolvido com foco em **boas práticas**, **organização de código** e **uso profissional de Git/GitHub**.

---

## 🧩 Funcionalidades

- 📥 Leitura de PDFs do tipo texto
- 🔁 Fallback automático para OCR (quando necessário)
- 🧠 Normalização de texto (remoção de acentos e ruídos)
- 🔍 Extração de dados via Regex
- 💰 Conversão correta de valores monetários para `float`
- 📊 Exportação para Excel (`.xlsx`)
- 🪟 Abertura automática do Excel no Windows
- 📝 Registro de logs de execução

---

## 📁 Estrutura do Projeto

```text
scripts_pdf/
│
├── main.py                # Pipeline principal
├── README.md              # Documentação do projeto
│
├── pdfs_entrada/          # PDFs de entrada
├── output/                # Arquivo Excel gerado
├── logs/                  # Logs de execução
│
└── src/
    ├── leitor_pdf.py      # Leitura de PDF (texto + OCR)
    ├── extrator.py        # Extração de dados com regex
    ├── utils.py           # Normalização e validação
    └── exportador.py      # Exportação para Excel
