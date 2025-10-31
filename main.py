import tkinter as tk
from load_data import load_data
from frontend.parameter import show_parameters_window
from frontend.tables import show_tables_window
from frontend.graph import show_graphs_window
from frontend.clinical_val import show_clinical_eval_window

bg_color = "#FFE8CD"
button_color = "#FFD6BA"
button_hover = "black"
font_main = ("Garamond", 12)
font_tittle = ("Times New Roman", 16, "bold")


def center_window(window, width=700, height=400):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")

# Load dataset globally
data = load_data("PCOS_data.csv")

def main():
    interface = tk.Tk()
    interface.title("PCOS Analysis App")
    interface.iconbitmap('images/image.ico')
    interface.geometry("700x700")
    interface.configure(bg=bg_color)

    message = (
        "Dear user,\n"
        "Welcome.\n\n"
        "Polycystic ovary syndrome (PCOS) is an endocrine-gynecological disorder "
        "that affects many women of childbearing age.\n\n"
        "In this program, we provide an interactive menu where you can:\n"
        "   -> Check averages, maximums, and minimums for different parameters;\n"
        "   -> View graphs showing the relationship between different parameters;\n"
        "   -> Observe tables showing the frequency of different parameters;\n"
        "   -> Assess your clinical situation (a PDF with the assessment will be created).\n"
        "By clicking on the buttons below, you can navigate through the menu.\n"
        "We hope you enjoy this program and explore some parameters related to this condition.\n\n"
        "Best regards!"
    )

    tk.Label(interface, text="""Polycystic Ovary Syndrome: \nExploratory statistical analysis and assessment of the clinical situation""", 
        bg=bg_color, font=font_tittle).pack(pady=20)

    tk.Label(interface, text=message, bg=bg_color, justify="left",
         font=('Georgia', 10), wraplength=650).pack(pady=10)
    
    frame_buttons = tk.Frame(interface, bg=bg_color)
    frame_buttons.pack(pady=20)

    tk.Button(frame_buttons, text="Exploratory statistical analysis", command=lambda: show_parameters_window(data),
              bg=button_color, font=font_main, width=35, relief="groove").pack(pady=8)

    tk.Button(frame_buttons, text="Frequency tables by parameters", command=lambda: show_tables_window(data),
              bg=button_color, font=font_main,  width=35, relief="groove").pack(pady=8)

    tk.Button(frame_buttons, text="Analysis charts", command=lambda: show_graphs_window(data),
              bg=button_color, font=font_main,  width=35, relief="groove").pack(pady=8)

    tk.Button(frame_buttons, text="Clinical Evaluation", command=lambda: show_clinical_eval_window(data),
              bg=button_color, font=font_main,  width=35, relief="groove").pack(pady=8)
    
    tk.Button(frame_buttons, text="Exit", command=interface.quit,
              bg="#FCD8CD", font=("Times New Roman", 11), width=35, relief="groove").pack(pady=15)

    interface.mainloop()

if __name__ == "__main__":
    main()
