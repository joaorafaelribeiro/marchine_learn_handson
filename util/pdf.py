import pandas as pd
from fpdf import FPDF


# Função para gerar o PDF a partir do DataFrame
def generate_pdf(data_frame: pd.DataFrame, output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.write_html(data_frame.to_html())
    pdf.output(output_filename)
