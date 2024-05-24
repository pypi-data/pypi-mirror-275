# 機能を提供するモジュール

import os
import comtypes.client
from docx import Document
from xlsxwriter.workbook import Workbook
from pptx import Presentation
import subprocess

class exfile_docfile_converter:
    def doc_to_pdf(doc_path, pdf_path):
        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = False
        doc = word.Documents.Open(doc_path)
        doc.SaveAs(pdf_path, FileFormat=17)  # 17 is for wdFormatPDF
        doc.Close()
        word.Quit()

    def docx_to_pdf(docx_path, pdf_path):
        doc_to_pdf(docx_path, pdf_path)

    def xlsx_to_pdf(xlsx_path, pdf_path):
        excel = comtypes.client.CreateObject('Excel.Application')
        excel.Visible = False
        wb = excel.Workbooks.Open(xlsx_path)
        wb.ExportAsFixedFormat(0, pdf_path)  # 0 is for xlTypePDF
        wb.Close()
        excel.Quit()

    def pptx_to_pdf(pptx_path, pdf_path):
        powerpoint = client.Dispatch("PowerPoint.Application")
        ppt = powerpoint.Presentations.Open(pptx_path, WithWindow=False)
        ppt.SaveAs(pdf_path, FileFormat=32)  # 32 is for ppSaveAsPDF
        ppt.Close()
        powerpoint.Quit()

    def convert_to_pdf(input_path, output_path):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"The file {input_path} does not exist.")

        ext = os.path.splitext(input_path)[1].lower()
        if ext in ['.doc', '.docx']:
            docx_to_pdf(input_path, output_path)
        elif ext == '.xlsx':
            xlsx_to_pdf(input_path, output_path)
        elif ext == '.pptx':
            pptx_to_pdf(input_path, output_path)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")

    if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(description="Convert Office files to PDF.")
        parser.add_argument("input", help="The input file to be converted.")
        parser.add_argument("output", help="The output PDF file.")
        args = parser.parse_args()
    
    convert_to_pdf(args.input, args.output)

