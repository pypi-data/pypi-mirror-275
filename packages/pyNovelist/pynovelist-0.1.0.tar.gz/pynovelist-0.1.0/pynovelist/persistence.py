import json

from fpdf import FPDF

def export_pdf(content, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf.output(filename)

def save_state(state, filename):
    with open(filename, 'w') as f:
        json.dump(state, f, indent=4)


def load_state(filename):
    with open(filename, 'r') as f:
        return json.load(f)



