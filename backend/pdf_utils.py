from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

def generate_pdf(results: dict):
    doc = SimpleDocTemplate("avaliacao_clinica.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = [Paragraph("Relatório de Avaliação Clínica", styles['Title']), Spacer(1, 20)]

    for key, value in results.items():
        story.append(Paragraph(f"<b>{key}:</b> {value}", styles['BodyText']))
        story.append(Spacer(1, 10))

    doc.build(story)
