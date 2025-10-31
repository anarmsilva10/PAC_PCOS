import tkinter as tk
from tkinter import messagebox
import pandas as pd
from load_data import load_data
from frontend.parameter import show_parameters_window
from frontend.tables import show_tables_window
from frontend.graph import show_graphs_window
from frontend.clinical_val import show_clinical_eval_window

# Load dataset globally
data = load_data("PCOS_data.csv")

def main():
    interface = tk.Tk()
    interface.title("PCOS Analysis App")
    interface.iconbitmap('images/image.ico')
    interface.geometry("700x700")
    interface.configure(bg="mistyrose")

    message = """
    Dear user,
    Welcome.

    Polycystic ovary syndrome (PCOS) is an endocrine-gynecological disorder 
    that affects many women of childbearing age.

    In this program, we provide an interactive menu where you can:
     -> Check averages, maximums, and minimums for different parameters
     -> View graphs showing the relationship between different parameters
     -> Observe tables showing the frequency of different parameters
     -> Assess your clinical situation (a PDF with the assessment will be created)
    By clicking on the buttons below, you can navigate through the menu.
    We hope you enjoy this program and that you 
    are able to explore some parameters related to this condition.

    Best regards!
    """

    tk.Label(interface, text="""Polycystic Ovary Syndrome: 
        Exploratory statistical analysis and assessment of the clinical situation""", 
        bg="mistyrose", font=('calibri', 16, 'bold')).pack(pady=20)

    tk.Label(interface, text=message, bg="mistyrose", justify="left",
         font=('calibri', 10), wraplength=650).pack(pady=10)

    tk.Button(interface, text="Exploratory statistical analysis", command=lambda: show_parameters_window(data),
              bg="lightpink", font=('calibri', 12)).pack(pady=10)

    tk.Button(interface, text="Frequency tables by parameters", command=lambda: show_tables_window(data),
              bg="lightpink", font=('calibri', 12)).pack(pady=10)

    tk.Button(interface, text="Analysis charts", command=lambda: show_graphs_window(data),
              bg="lightpink", font=('calibri', 12)).pack(pady=10)

    tk.Button(interface, text="Clinical Evaluation", command=lambda: show_clinical_eval_window(data),
              bg="lightpink", font=('calibri', 12)).pack(pady=10)

    tk.Button(interface, text="Exit", command=interface.quit,
              bg="salmon", font=('calibri', 12)).pack(pady=20)

    interface.mainloop()

if __name__ == "__main__":
    main()
