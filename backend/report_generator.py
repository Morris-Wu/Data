from fpdf import FPDF
from datetime import datetime
import os
#HW5
class PDF(FPDF):
    def __init__(self, font_path, title='', columns=None, col_widths=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font_path = font_path
        self.title_text = title
        self.columns = columns or []
        self.col_widths = col_widths or []
        self.add_font('kaiu', '', self.font_path, uni=True)
        self.set_font('kaiu', '', 12)
    #HW5
    def header(self):
        self.set_font('kaiu', '', 16)
        spaced_title = '  '.join(self.title_text)
        self.cell(0, 10, spaced_title, ln=True, align='C')
        self.ln(10)
        if self.columns and self.col_widths:
            self.set_font('kaiu', '', 11)
            self.set_fill_color(200, 200, 200)
            for col, width in zip(self.columns, self.col_widths):
                self.cell(width, 10, str(col), border=1, align='C', fill=True)
            self.ln()
    #HW5
    def footer(self):
        self.set_y(-15)
        self.set_font('kaiu', '', 9)
        self.cell(0, 10, f'第 {self.page_no()} 頁', align='C')
#HW5
def generate_pdf_report(df, title='CPBL 報表', data_type='batting'):
    font_path = r'C:\Windows\Fonts\kaiu.ttf'
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"找不到字型檔案：{font_path}")

    if data_type == 'batting':
        columns = ['Name', 'Team Name', 'G', 'PA', 'RBI', 'R', 'H', '1B', '2B', 'HR', 'BB']
    else:
        columns = ['Name', 'Team Name', 'G', 'W', 'L', 'SV', 'HLD', 'H', 'HR', 'BB', 'SO']

    df = df[columns]
    pdf_temp = FPDF()
    total_width = pdf_temp.w - 20
    name_width = 70
    team_width = 35
    other_width = (total_width - name_width - team_width) / (len(columns) - 2)

    col_widths = []
    for col in columns:
        if col == 'Name':
            col_widths.append(name_width)
        elif col == 'Team Name':
            col_widths.append(team_width)
        else:
            col_widths.append(other_width)

    pdf = PDF(font_path=font_path, title=title, columns=columns, col_widths=col_widths)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font('kaiu', '', 11)

    for _, row in df.iterrows():
        for col, width in zip(columns, col_widths):
            text = str(row[col])
            if col == 'Name':
                text = ' '.join(text)
            if len(text) > 20:
                text = text[:18] + '…'
            pdf.cell(width, 10, text, border=1, align='C')
        pdf.ln()

    output_dir = "report"
    os.makedirs(output_dir, exist_ok=True)
    date_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(output_dir, f"{date_str}.pdf")
    pdf.output(filename)
    return filename


