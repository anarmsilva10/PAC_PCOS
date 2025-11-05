import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

col1, col2 = st.columns([1, 8])
with col1:
    st.image("images/medical-report.png", width=100)
with col2:
    st.title("Assess your medical condition")
st.markdown(
        "Please enter your values below to get a personalized clinical assessment. "
        "A PDF report will also be generated."
    )

if 'data' not in st.session_state:
    st.warning("No data, please upload the correct dataset.")
else:
    data = st.session_state['data']

    # -------------------------------------------------------
    # Input fields
    # -------------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        TSH_val = st.number_input("TSH (mIU/L)", min_value=0.0, max_value=10.0, step=0.1)
        AMH_val = st.number_input("AMH (ng/mL)", min_value=0.0, max_value=20.0, step=0.1)
        VitD_val = st.number_input("Vitamin D3 (ng/mL)", min_value=0.0, max_value=100.0, step=0.1)

    with col2:
        Hb_val = st.number_input("Hemoglobin (g/dL)", min_value=0.0, max_value=20.0, step=0.1)
        Ciclo_val = st.number_input("Menstruation Cycle Duration (days)", min_value=0.0, max_value=50.0, step=1.0)

    # -------------------------------------------------------
    # Evaluation logic
    # -------------------------------------------------------
    reference_ranges = {
        'TSH': (0.4, 4),
        'AMH': (1, 4),
        'VitD': (20, 40),
        'Hb': (12, 16),
        'Duration': (3, 8)
    }

    def evaluate_values():
        values = {
            'TSH': TSH_val,
            'AMH': AMH_val,
            'VitD': VitD_val,
            'Hb': Hb_val,
            'Duration': Ciclo_val
        }
        results = {}
        for param, val in values.items():
            ref = reference_ranges[param]
            if ref[0] <= val <= ref[1]:
                results[param] = f"{val} is within the reference range ({ref[0]} - {ref[1]})."
            else:
                results[param] = f"{val} is outside the reference range ({ref[0]} - {ref[1]}). Please consult your doctor."
        return results

    # -------------------------------------------------------
    # Submit button and display results
    # -------------------------------------------------------
    if st.button("Submit values"):
        results = evaluate_values()

        st.subheader("Evaluation results")
        for param, res in results.items():
            st.write(f"**{param}:** {res}")

        # -------------------------------------------------------
        # PDF generation
        # -------------------------------------------------------
        pdf_path = "clinical_evaluation.pdf"
        pdf = canvas.Canvas(pdf_path, pagesize=letter)
        pdf.setFont("Times-Roman", 12)

        # Header
        try:
            logo = ImageReader("images/image_1.png")
            pdf.drawImage(logo, 30, 760, width=40, height=40)
        except Exception:
            pass

        pdf.drawString(80, 770, "Polycystic Ovary Syndrome")
        pdf.drawString(50, 740, "Personalized clinical assessment")

        y = 700
        pdf.drawString(50, y, "Evaluation results:")
        y -= 20

        for param, res in results.items():
            pdf.drawString(70, y, f"{param}: {res}")
            y -= 15

        pdf.drawString(50, y - 20, "Please be aware of the signs and symptoms. Best regards!")

        try:
            etiologia = ImageReader("images/etiologia.png")
            pdf.drawImage(etiologia, 50, 200, width=500, height=200)
        except Exception:
            pass

        pdf.save()

        # Show download link
        with open(pdf_path, "rb") as f:
            st.download_button("Download clinical report (PDF)", f, file_name="clinical_evaluation.pdf")