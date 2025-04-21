from fpdf import FPDF
from datetime import datetime
import os

class PDF(FPDF):
    def __init__(self, font_path, title='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font_path = font_path
        self.title_text = title
        self.add_font('kaiu', '', self.font_path, uni=True)
        self.set_font('kaiu', '', 12)

    def header(self):
        self.set_font('kaiu', '', 16)
        self.cell(0, 10, self.title_text, ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('kaiu', '', 9)
        self.cell(0, 10, f'第 {self.page_no()} 頁', align='C')

def generate_pdf_report(df, title='CPBL 報表'):
    font_path = r'C:\Windows\Fonts\kaiu.ttf'
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"❌ 找不到字型檔案：{font_path}")

    pdf = PDF(font_path=font_path, title=title)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font('kaiu', '', 11)

    col_widths = [pdf.epw / len(df.columns)] * len(df.columns)
    line_height = pdf.font_size * 2.5

    pdf.set_fill_color(200, 200, 200)
    for i, col in enumerate(df.columns):
        pdf.multi_cell(col_widths[i], line_height, str(col), border=1, align='C', fill=True, ln=3)
    pdf.ln(line_height)

    pdf.set_fill_color(255, 255, 255)
    for _, row in df.iterrows():
        for i, col in enumerate(df.columns):
            text = str(row[col])
            pdf.multi_cell(col_widths[i], line_height, text, border=1, align='C', ln=3)
        pdf.ln(line_height)

    output_dir = "report"
    os.makedirs(output_dir, exist_ok=True)
    date_str = datetime.now().strftime('%Y%m%d')
    filename = os.path.join(output_dir, f"{date_str}.pdf")
    pdf.output(filename)
    print(f"✅ PDF 報表已產出：{filename}")
    return filename
