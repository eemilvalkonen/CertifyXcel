import os
import pandas as pd
from fpdf import FPDF
import re
from datetime import datetime

file_path = "../Osallistujat.xlsx"
xls = pd.ExcelFile(file_path)

df_tilaisuudet = pd.read_excel(xls, sheet_name="Tilaisuudet")
df_henkilot = pd.read_excel(xls, sheet_name="Henkilöt")
df_yleiset = pd.read_excel(xls, sheet_name="Yleiset")

output_dir = "../Osallistumistodistukset"
os.makedirs(output_dir, exist_ok=True)

ajankohdat = pd.to_datetime(df_tilaisuudet['Ajankohta'], errors='coerce')
ensimmainen_ajankohta = ajankohdat.min()
viimeinen_ajankohta = ajankohdat.max()

ajankohta_teksti = f"Ajankohta {ensimmainen_ajankohta.month}-{viimeinen_ajankohta.month}/{viimeinen_ajankohta.year}"

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-åäöÅÄÖ]', '-', name)

def clean_text(text):
    if isinstance(text, str):
        return text.encode('latin-1', 'ignore').decode('latin-1')
    return ""

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("ArialBlack", "", "fonts/ArialBlack.ttf", uni=True)
        self.add_font("ArialNova", "", "fonts/ArialNova.ttf", uni=True)
        self.add_font("ArialNova-Bold", "", "fonts/ArialNova-Bold.ttf", uni=True)
        self.add_font("ArialNovaCond", "", "fonts/ArialNovaCond.ttf", uni=True)
        self.add_font("Calibri", "", "fonts/Calibri.ttf", uni=True)
        self.add_font("Calibri Bold", "", "fonts/Calibri-Bold.ttf", uni=True)

date_columns = df_henkilot.columns[1:]
for index, row in df_henkilot.iterrows():
    nimi = clean_text(row["Nimi"])
    osallistumiset = []

    for date in date_columns:
        if pd.notna(row[date]) and row[date] == "x":
            tilaisuus = df_tilaisuudet[df_tilaisuudet["Ajankohta"] == date]
            if not tilaisuus.empty:
                osallistumiset.append(tilaisuus)

    if osallistumiset:
        pdf = PDF()
        pdf.set_auto_page_break(auto=True, margin=12)
        pdf.add_page()

        pdf.ln(5)
        pdf.set_font("ArialNova-Bold", "", 22)
        pdf.cell(0, 10, clean_text("Osallistumistodistus"), ln=True, align='C')

        pdf.ln(4)
        pdf.set_font("ArialNovaCond", "", 16)
        pdf.cell(0, 10, clean_text(f"{nimi}"), ln=True, align='C')

        pdf.ln(2)
        pdf.set_font("ArialNovaCond", "", 16)
        pdf.cell(0, 10, clean_text(ajankohta_teksti), ln=True, align='C')
        pdf.ln(8)

        pdf.image("images/line-break-wide.png", x=15, w=180)
        pdf.ln(5)

        pdf.set_font("ArialBlack", "", 16)
        doc_title = clean_text(df_yleiset.iloc[0]['Dokumentin otsikko'])
        pdf.cell(190, 10, clean_text(doc_title), ln=True)
        pdf.ln(1)

        pdf.set_font("Calibri", "", 11)
        doc_desc = clean_text(df_yleiset.iloc[0]['Dokumentin kuvaus'])
        pdf.multi_cell(190, 5, clean_text(doc_desc))
        pdf.ln(1)

        pdf.set_font("ArialBlack", "", 14)
        pdf.cell(190, 10, clean_text("Henkilö on osallistunut seuraaviin osuuksiin"), ln=True)

        for tilaisuus in osallistumiset:
            for _, t in tilaisuus.iterrows():
                paivamaara = pd.to_datetime(t['Ajankohta']).strftime("%d.%m.%Y")
                kellonaika = t['Kellonaika']
                if pd.notna(kellonaika):
                    alku, loppu = kellonaika.split('-')
                    kellonaika = f"Klo {int(alku[:2])}-{int(loppu[:2])}"
                else:
                    kellonaika = ""
                pdf.set_font("Calibri Bold", "", 11)
                pdf.cell(190, 4, clean_text(f"{paivamaara}, {kellonaika} | {t['Nimi']} | {t['Paikka']}"), ln=True)
                pdf.ln(1)
                pdf.set_font("Calibri", "", 11)
                for aihe in t["Aiheet":"Unnamed: 6"].dropna().values:
                    pdf.cell(3)
                    pdf.cell(0, 5, u'\u2022 ' + clean_text(f"{aihe}"), ln=True)
                pdf.ln(2)

        pdf.ln(5)
        image_width = 95
        page_width = 210
        x_position = (page_width - image_width) / 2
        pdf.image("images/line-break-wide.png", x=x_position, w=image_width)
        pdf.ln(2)

        pdf.set_font("ArialNovaCond", "", 16)
        pdf.cell(0, 10, clean_text(datetime.now().strftime("%d.%m.%Y")), ln=True, align='C')

        signature_width = 65
        x_position = (210 - signature_width) / 2
        pdf.image("images/signature.png", x=x_position, w=signature_width)
        allekirjoittaja = clean_text(df_yleiset.iloc[0]['Allekirjoittaja'])
        pdf.set_font("ArialNovaCond", "", 14)
        pdf.cell(0, 10, clean_text(allekirjoittaja), ln=True, align='C')
        pdf.ln(4)

        pdf.image("images/logo.png", x=87.5, w=35)
        pdf.ln(4)

        pdf.set_font("ArialNovaCond", "", 11)
        pdf.cell(0, 5, clean_text("www.google.com"), ln=True, align='C')
        pdf.cell(0, 5, clean_text("+358 123 456 789"), ln=True, align='C')
        pdf.ln(2)

        safe_nimi = sanitize_filename(nimi)
        pdf_filename = os.path.join(output_dir, f"{safe_nimi}-Osallistumistodistus.pdf")
        pdf.output(pdf_filename)

print("Osallistumistodistukset on luotu onnistuneesti!")