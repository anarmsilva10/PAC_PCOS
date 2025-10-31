import tkinter as tk
from tkinter import Toplevel, Label, Entry, Text, Button, END, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os


def show_clinical_eval_window(data):

    def evaluate_values(TSH_val, AMH_val, VitD_val, Hb_val, Ciclo_val):
        reference_ranges = {
            'TSH': (0.4, 4),
            'AMH': (1, 4),
            'VitD': (20, 40),
            'Hb': (12, 16),
            'Duration': (3, 8)
        }

        results = {}
        for param, val in zip(
            ['TSH', 'AMH', 'VitD', 'Hb', 'Duration'],
            [TSH_val, AMH_val, VitD_val, Hb_val, Ciclo_val]
        ):
            ref = reference_ranges[param]
            if val is None:
                results[param] = "Value not entered. Please enter a valid value."
            elif ref[0] <= val <= ref[1]:
                results[param] = f"{val} is within the reference values ({ref[0]} - {ref[1]})."
            else:
                results[param] = (
                    f"{val} is outside the reference values ({ref[0]} - {ref[1]}).\n"
                    "Please consult your doctor."
                )
        return results

    def get_float_value(entry):
        value = entry.get().strip()
        try:
            return float(value) if value else None
        except ValueError:
            messagebox.showerror("Error", f"'{value}' is not a valid number.")
            return None

    # -------------------------------------------------------
    # Window setup
    # -------------------------------------------------------
    top = Toplevel()
    top.title("Assess your medical condition")
    top.iconbitmap('images/image.ico')
    top.geometry("550x550")
    top.configure(bg="mistyrose")

    # -------------------------------------------------------
    # Input fields
    # -------------------------------------------------------
    labels = ["TSH (mIU/L)", "AMH (ng/mL)", "Vitamin D3 (ng/mL)",
              "Hemoglobin (g/dL)", "Menstruation Cycle Duration (days)"]
    entries = []

    for i, text in enumerate(labels, start=2):
        Label(top, text=text, bg="mistyrose", font=('calibri', 11)).grid(row=i, column=0, sticky='e', padx=10, pady=5)
        entry = Entry(top, width=30)
        entry.grid(row=i, column=1, padx=10)
        entries.append(entry)

    result_text = Text(top, height=10, width=65, bg="white", font=('calibri', 10))
    result_text.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    # -------------------------------------------------------
    # PDF generation
    # -------------------------------------------------------
    def evaluate_values_and_print():
        TSH_val, AMH_val, VitD_val, Hb_val, Ciclo_val = [get_float_value(e) for e in entries]

        # If any value failed to parse, stop
        if any(v is None for v in [TSH_val, AMH_val, VitD_val, Hb_val, Ciclo_val]):
            messagebox.showwarning("Warning", "Please fill in all fields correctly.")
            return

        results = evaluate_values(TSH_val, AMH_val, VitD_val, Hb_val, Ciclo_val)
        result_text.delete(1.0, END)

        # Show results in the text box
        for param, res in results.items():
            result_text.insert(END, f"{param}: {res}\n\n")

        # Generate PDF
        pdf_path = "clinical_evaluation.pdf"
        pdf = canvas.Canvas(pdf_path, pagesize=letter)
        pdf.setFont("Times-Roman", 12)

        # Header
        try:
            logo = ImageReader("images/image_1.png")
            pdf.drawImage(logo, 30, 760, width=40, height=40)
        except Exception:
            pass  # Skip if missing

        pdf.drawString(80, 770, "Polycystic Ovary Syndrome")
        pdf.drawString(50, 740, "Personalized clinical assessment")

        # Results
        y = 700
        pdf.drawString(50, y, "Evaluation results:")
        y -= 20

        for param, res in results.items():
            lines = res.split('\n')
            pdf.drawString(70, y, f"{param}: {lines[0]}")
            y -= 15
            if len(lines) > 1:
                pdf.drawString(90, y, lines[1])
                y -= 15

        pdf.drawString(50, y - 20, "Please be aware of the signs and symptoms. Best regards!")
        try:
            etiologia = ImageReader("images/etiologia.png")
            pdf.drawImage(etiologia, 50, 200, width=500, height=200)
        except Exception:
            pass

        pdf.save()
        messagebox.showinfo("PDF Created", f"Evaluation saved in:\n{os.path.abspath(pdf_path)}")

    # -------------------------------------------------------
    # Buttons
    # -------------------------------------------------------
    Button(top, text="Submit values", command=evaluate_values_and_print,
           bg="#FFD6BA", fg="black", font=('Garamond', 12), relief="raised",
                  bd=3).grid(row=8, column=0, columnspan=2, pady=10, ipadx=10)

    Button(top, text="Back to Menu", command=top.destroy,
           bg="#FCD8CD", fg="black", font=('Times New Roman', 11), relief="raised",
                  bd=3).grid(row=9, column=0, columnspan=2, pady=10, ipadx=10)

    # Adjust layout
    for i in range(2):
        top.grid_columnconfigure(i, weight=1)