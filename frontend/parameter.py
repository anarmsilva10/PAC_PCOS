import tkinter as tk
from tkinter import Toplevel, Label
import io
from PIL import Image, ImageTk
import plotly.graph_objects as go


def show_parameters_window(data):
    pit = Toplevel()
    pit.title("Exploratory statistical analysis")
    pit.iconbitmap('images/image.ico')
    pit.geometry("400x400")
    pit.configure(bg="mistyrose")

    pcos = data[data['PCOS (Y/N)'] == 1]
    no_pcos = data[data['PCOS (Y/N)'] == 0]

    # -------------------------
    # Helper function to show tables
    # -------------------------
    def display_table(fig):
        img_bytes = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_bytes))

        image_window = tk.Toplevel(pit)
        image_window.title("Table")
        image_window.iconbitmap('images/image.ico')

        img = ImageTk.PhotoImage(img)
        panel = Label(image_window, image=img)
        panel.image = img
        panel.pack(expand=True, fill='both')

    # -------------------------
    # Parameter: Age
    # -------------------------
    def age():
        mean_with = pcos[' Age (yrs)'].mean()
        max_with = pcos[' Age (yrs)'].max()
        min_with = pcos[' Age (yrs)'].min()

        mean_without = no_pcos[' Age (yrs)'].mean()
        max_without = no_pcos[' Age (yrs)'].max()
        min_without = no_pcos[' Age (yrs)'].min()

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['PCOS', 'Average', 'Maximum', 'Minimum'],
                line_color='black', fill_color='salmon',
                align='center', font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[
                    ['With', 'Without'],
                    [f"{mean_with:.2f}", f"{mean_without:.2f}"],
                    [max_with, max_without],
                    [min_with, min_without]
                ],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11)
            )
        )])

        fig.update_layout(
            title="Analysis of age in relation to the presence/absence of disease",
            title_font=dict(color="black", size=14)
        )

        display_table(fig)

    # -------------------------
    # Parameter: Mentruation Cycle
    # -------------------------
    def mens():
        mean_with = pcos['Cycle length(days)'].mean()
        max_with = pcos['Cycle length(days)'].max()
        min_with = pcos['Cycle length(days)'].min()

        mean_without = no_pcos['Cycle length(days)'].mean()
        max_without = no_pcos['Cycle length(days)'].max()
        min_without = no_pcos['Cycle length(days)'].min()

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['PCOS', 'Average', 'Maximum', 'Minimum'],
                line_color='black', fill_color='salmon',
                align='center', font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[
                    ['With', 'Without'],
                    [f"{mean_with:.2f}", f"{mean_without:.2f}"],
                    [max_with, max_without],
                    [min_with, min_without]
                ],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11)
            )
        )])

        fig.update_layout(
            title="Analysis of Menstrual Duration (in days) in relation to the presence/absence of disease",
            title_font=dict(color="black", size=14)
        )

        display_table(fig)

    # -------------------------
    # Parameter: Glucose
    # -------------------------
    def glu():
        mean_with = pcos['RBS(mg/dl)'].mean()
        max_with = pcos['RBS(mg/dl)'].max()
        min_with = pcos['RBS(mg/dl)'].min()

        mean_without = no_pcos['RBS(mg/dl)'].mean()
        max_without = no_pcos['RBS(mg/dl)'].max()
        min_without = no_pcos['RBS(mg/dl)'].min()

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['PCOS', 'Average', 'Maximum', 'Minimum'],
                line_color='black', fill_color='salmon',
                align='center', font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[
                    ['With', 'Without'],
                    [f"{mean_with:.2f}", f"{mean_without:.2f}"],
                    [max_with, max_without],
                    [min_with, min_without]
                ],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11)
            )
        )])

        fig.update_layout(
            title="Glucose (mg/dl) analysis in relation to the presence/absence of disease",
            title_font=dict(color="black", size=14)
        )

        display_table(fig)

    # -------------------------
    # Parameter: Folículos
    # -------------------------
    def fol():
        follicle_parameters = {
            'Follicle No. (L)': 'Left',
            'Follicle No. (R)': 'Right'
        }

        ovary_sides, parameter_types, With_values, Without_values = [], [], [], []

        for parameter, side in follicle_parameters.items():
            mean_with = pcos[parameter].mean()
            max_with = pcos[parameter].max()
            min_with = pcos[parameter].min()

            mean_without = no_pcos[parameter].mean()
            max_without = no_pcos[parameter].max()
            min_without = no_pcos[parameter].min()

            ovary_sides.extend([side] * 3)
            parameter_types.extend(['Average', 'Maximum', 'Minimum'])
            With_values.extend([f"{mean_with:.2f}", f"{max_with:.2f}", f"{min_with:.2f}"])
            Without_values.extend([f"{mean_without:.2f}", f"{max_without:.2f}", f"{min_without:.2f}"])

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['Ovary', 'Parameter', 'PCOS:Without', 'PCOS:With'],
                line_color='black', fill_color='salmon',
                align='center', font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[ovary_sides, parameter_types, Without_values, With_values],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11)
            )
        )])

        fig.update_layout(
            title="Analysis of the Number of Follicles in relation to the presence/absence of disease",
            title_font=dict(color="black", size=14)
        )

        display_table(fig)

    # -------------------------
    # Parameter: Hormonas
    # -------------------------
    def hormona():
        hormone_parameters = {
            'AMH(ng/mL)': 'AMH',
            'TSH (mIU/L)': 'TSH',
            'FSH(mIU/mL)': 'FSH',
            'LH(mIU/mL)': 'LH',
            'PRG(ng/mL)': 'PRG'
        }

        hormones, parameter_types, With_values, Without_values = [], [], [], []

        for parameter, hormone in hormone_parameters.items():
            mean_with = pcos[parameter].mean()
            max_with = pcos[parameter].max()
            min_with = pcos[parameter].min()

            mean_without = no_pcos[parameter].mean()
            max_without = no_pcos[parameter].max()
            min_without = no_pcos[parameter].min()

            hormones.extend([hormone] * 3)
            parameter_types.extend(['Average', 'Maximum', 'Minimum'])
            With_values.extend([f"{mean_with:.2f}", f"{max_with:.2f}", f"{min_with:.2f}"])
            Without_values.extend([f"{mean_without:.2f}", f"{max_without:.2f}", f"{min_without:.2f}"])

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['Hormone', 'Parameter', 'PCOS:Without', 'PCOS:With'],
                line_color='black', fill_color='salmon',
                align='center', font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[hormones, parameter_types, Without_values, With_values],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11)
            )
        )])

        fig.update_layout(
            title="Analysis of hormones in relation to the presence/absence of disease",
            title_font=dict(color="black", size=14),
            width=800, height=600
        )

        display_table(fig)

    # -------------------------------------------------------
    # Buttons
    # -------------------------------------------------------
    for col in range(6):
        pit.grid_columnconfigure(col, weight=1)

    buttons = [
        ("Age", age),
        ("Menstruation Cycle", mens),
        ("Glucose", glu),
        ("Follicle Size", fol),
        ("Hormones", hormona)
    ]

    for i, (text, command) in enumerate(buttons, start=1):
        tk.Button(pit, text=text, command=command, bg="#FFD6BA", fg="black", font=('Garamond', 12), relief="raised",
                  bd=3, activebackground="#F3A26D", activeforeground="black", padx=20, pady=8
                  ).grid(row=i, column=0, columnspan=5, pady=5)

    tk.Button(pit, text="Back to Menu", command=pit.destroy, bg="#FCD8CD", fg="black", font=('Times New Roman', 11),
              relief="raised", bd=3, activebackground="#F3A26D", activeforeground="black",padx=20, pady=8
              ).grid(row=len(buttons)+1, column=0, columnspan=5, pady=10)