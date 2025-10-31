import tkinter as tk
from tkinter import Toplevel, Button
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure matplotlib and seaborn are configured for Tkinter
plt.rcParams.update({'figure.autolayout': True})

def show_graphs_window(data):
    tip = Toplevel()
    tip.title("Charts")
    tip.iconbitmap('images/image.ico')
    tip.geometry("430x500")

    colors = {0: 'lightcoral', 1: 'maroon'}
    pcos = data[data['PCOS (Y/N)'] == 1]

    # --- GRAPH FUNCTIONS ---

    def g_age():
        sns.histplot(data=pcos, x=" Age (yrs)", hue="PCOS (Y/N)",
                     element='step', multiple="dodge", palette=colors,
                     edgecolor='black', legend=False)
        plt.title('Age Distribution in PCOS', fontsize=14, fontweight='bold')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()

    def vitD():
        data.boxplot(column='Vit D3 (ng/mL)', by='PCOS (Y/N)', figsize=(10,5),
                      whis=[5,95], return_type='axes', showfliers=False, patch_artist=True,
                      boxprops=dict(facecolor="mistyrose"),
                      medianprops=dict(color="salmon", linewidth=1),
                      whiskerprops=dict(color="black", linewidth=1.5))
        plt.suptitle('')
        plt.title('Vitamin D among patients and non-patients', fontsize=14, fontweight='bold')
        plt.ylabel('Vit D3 (ng/mL)')
        plt.xlabel('PCOS')
        plt.xticks([1,2], ['Without', 'With'])
        plt.show()

    def FSHLH():
        data.boxplot(column='FSH/LH', by='PCOS (Y/N)', figsize=(10,5),
                      whis=[5,95], return_type='axes', showfliers=False, patch_artist=True,
                      boxprops=dict(facecolor="mistyrose"),
                      medianprops=dict(color="salmon", linewidth=1),
                      whiskerprops=dict(color="black", linewidth=1.5))
        plt.suptitle('')
        plt.title('FSH/LH ratio among patients and non-patients', fontsize=14, fontweight='bold')
        plt.ylabel('FSH/LH')
        plt.xlabel('PCOS')
        plt.xticks([1,2], ['Without', 'With'])
        plt.show()

    def abortions():
        sns.histplot(data=data, x="No. of abortions", hue="PCOS (Y/N)",
                     element='step', multiple="dodge", palette=colors, legend=False)
        plt.title('No. of abortions among patients and non-patients', fontsize=14, fontweight='bold')
        plt.legend(title='PCOS', labels=['Without', 'With'],
                   loc='upper right', fontsize=10, ncol=1)
        plt.ylabel('Frequency')
        plt.xlabel('No. of abortions')
        plt.show()

    def cycle():
        sns.histplot(data=data, x="Cycle length(days)", hue="PCOS (Y/N)",
                     element='step', multiple="dodge", palette=colors, legend=False)
        plt.title('Menstruation Cycle among patients and non-patients', fontsize=14, fontweight='bold')
        plt.legend(title='PCOS', labels=['Without', 'With'],
                   loc='upper right', fontsize=10, ncol=1)
        plt.ylabel('Frequency')
        plt.xlabel('Menstruation Cycle (days)')
        plt.show()

    def AMHLH():
        sns.relplot(data=pcos, x="AMH(ng/mL)", y="LH(mIU/mL)",
                    color="maroon", legend=False)
        plt.title('Correlation between AMH and LH in patients', fontsize=14, fontweight='bold')
        plt.ylabel('LH(mIU/mL)')
        plt.xlabel('AMH(ng/mL)')
        plt.ylim(-1, 14)
        plt.xlim(-1, 40)
        plt.xticks(range(0, 40, 5))
        plt.gcf().set_size_inches(8, 6)
        plt.tight_layout()
        plt.show()

    def bmi():
        sns.lmplot(data=data, x="RBS(mg/dl)", y="BMI", hue="PCOS (Y/N)",
                   palette=colors, legend=False)
        plt.title('Correlation between BMI and RBS among patients and non-patients', fontsize=14, fontweight='bold')
        plt.ylabel('BMI')
        plt.xlabel('RBS (mg/dl)')
        plt.ylim(0, 60)
        plt.xlim(0, 250)
        plt.gcf().set_size_inches(8, 6)
        plt.tight_layout()

        legend_labels = ['Without', 'With']
        handles = [
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[0], markersize=8),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[1], markersize=8)
        ]
        plt.legend(handles=handles, labels=legend_labels, title="PCOS",
                   loc='upper right', fontsize=10, ncol=1)
        plt.show()

    def follicle():
        sns.lmplot(data=data, x='Follicle No. (R)', y='Follicle No. (L)',
                   hue="PCOS (Y/N)", palette=colors, legend=False)
        plt.title('Number of follicles among patients and non-patients', fontsize=14, fontweight='bold')
        plt.ylabel('Follicle No. (L)')
        plt.xlabel('Follicle No. (R)')
        plt.ylim(-2, 30)
        plt.xlim(-2, 25)
        plt.gcf().set_size_inches(10, 10)
        plt.tight_layout()
        legend_labels = ['Without', 'With']
        handles = [
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[0], markersize=8),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[1], markersize=8)
        ]
        plt.legend(handles=handles, labels=legend_labels, title="PCOS",
                   loc='upper right', fontsize=10, ncol=1)
        plt.show()

    def endometrium():
        data.boxplot(column='Endometrium (mm)', by='PCOS (Y/N)', figsize=(10,5),
                      whis=[5,95], return_type='axes', showfliers=False, patch_artist=True,
                      boxprops=dict(facecolor="mistyrose"),
                      medianprops=dict(color="salmon", linewidth=1),
                      whiskerprops=dict(color="black", linewidth=1.5))
        plt.suptitle('')
        plt.title('Endometrial thickening among patients and non-patients', fontsize=14, fontweight='bold')
        plt.ylabel('Endometrium (mm)')
        plt.xlabel('PCOS')
        plt.xticks([1,2], ['Without', 'With'])
        plt.show()

    # -------------------------------------------------------
    # Buttons
    # -------------------------------------------------------
    for col in range(5):
        tip.grid_columnconfigure(col, weight=1)

    buttons = [
        ("Age distribution in PCOS", g_age),
        ("Vitamin D among patients and non-patients", vitD),
        ("FSH/LH ratio among patients and non-patients", FSHLH),
        ("No. of abortions among patients and non-patients", abortions),
        ("Menstruation Cycle among patients and non-patients", cycle),
        ("Correlation between AMH and LH in patients", AMHLH),
        ("Correlation between BMI and RBS among patients and non-patients", bmi),
        ("Number of follicles among patients and non-patients", follicle),
        ("Endometrial thickening among patients and non-patients", endometrium)
    ]

    for i, (text, command) in enumerate(buttons, start=1):
        tk.Button(tip, text=text, command=command, bg="#FFD6BA", fg="black", font=('Garamond', 12), relief="raised",
                  bd=3, activebackground="#F3A26D", activeforeground="black", padx=20, pady=8
                  ).grid(row=i, column=0, columnspan=5, pady=5)

    tk.Button(tip, text="Back to Menu", command=tip.destroy, bg="#FCD8CD", fg="black", font=('Times New Roman', 11),
              relief="raised", bd=3, activebackground="#F3A26D", activeforeground="black" ,padx=20, pady=8
              ).grid(row=len(buttons)+1, column=0, columnspan=5, pady=10)