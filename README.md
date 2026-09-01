
# 🏦 Automating Bank Cheque Data Extraction from Scanned PDFs

An AI-powered Python application that extracts important cheque information from scanned cheque PDFs using image processing and OCR. The extracted information is displayed in a structured table and can be exported as CSV.

## 🚀 Features

- Upload scanned cheque PDFs through a Streamlit web application
- Convert PDF pages into cheque images
- Extract important cheque regions using OpenCV
- Extract text using Microsoft's TrOCR model
- Extract cheque information such as:
  - Date
  - Payee
  - Name
  - Amount
  - Account Number
- Display extracted information in a structured table
- Export extracted data as a CSV file

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – Web application interface
- **OpenCV** – Image processing and cheque region extraction
- **PyMuPDF** – PDF processing
- **Pillow** – Image handling
- **Hugging Face Transformers** – TrOCR-based OCR
- **Pandas** – Data processing and CSV generation

## 🔄 Project Workflow

```text
Scanned Cheque PDF
        ↓
PDF Page Extraction
        ↓
Cheque Image Processing
        ↓
Region Extraction using OpenCV
        ↓
OCR using TrOCR
        ↓
Structured Cheque Data
        ↓
Streamlit Table + CSV