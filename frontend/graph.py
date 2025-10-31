import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def show_graphs_window(data):
    st.subheader("📊 Analysis Charts")

    colors = {0: 'lightcoral', 1: 'maroon'}
    pcos = data[data['PCOS (Y/N)'] == 1]

    # Available Graph
    graph_option = st.selectbox(
        "Select the chart you want to visualize:",
        [
            "Age distribution in PCOS",
            "Vitamin D among patients and non-patients",
            "FSH/LH ratio among patients and non-patients",
            "No. of abortions among patients and non-patients",
            "Menstruation Cycle among patients and non-patients",
            "Correlation between AMH and LH in patients",
            "Correlation between BMI and RBS among patients and non-patients",
            "Number of follicles among patients and non-patients",
            "Endometrial thickening among patients and non-patients"
        ]
    )

    # Graph figure for each case
    fig, ax = plt.subplots(figsize=(8, 5))

    if graph_option == "Age distribution in PCOS":
        sns.histplot(data=pcos, x=" Age (yrs)", hue="PCOS (Y/N)",
                     element='step', multiple="dodge", palette=colors,
                     edgecolor='black', legend=False, ax=ax)
        ax.set_title('Age Distribution in PCOS', fontsize=14, fontweight='bold')
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')

    elif graph_option == "Vitamin D among patients and non-patients":
        data.boxplot(column='Vit D3 (ng/mL)', by='PCOS (Y/N)', whis=[5,95],
                     showfliers=False, patch_artist=True, boxprops=dict(facecolor="mistyrose"),
                     medianprops=dict(color="salmon"), whiskerprops=dict(color="black"), ax=ax)
        ax.set_title('Vitamin D among patients and non-patients', fontsize=14, fontweight='bold')
        ax.set_ylabel('Vit D3 (ng/mL)')
        ax.set_xlabel('PCOS')
        ax.set_xticklabels(['Without', 'With'])

    elif graph_option == "FSH/LH ratio among patients and non-patients":
        data.boxplot(column='FSH/LH', by='PCOS (Y/N)', whis=[5,95],
                     showfliers=False, patch_artist=True, boxprops=dict(facecolor="mistyrose"),
                     medianprops=dict(color="salmon"), whiskerprops=dict(color="black"), ax=ax)
        ax.set_title('FSH/LH ratio among patients and non-patients', fontsize=14, fontweight='bold')
        ax.set_ylabel('FSH/LH')
        ax.set_xlabel('PCOS')
        ax.set_xticklabels(['Without', 'With'])

    elif graph_option == "No. of abortions among patients and non-patients":
        sns.histplot(data=data, x="No. of abortions", hue="PCOS (Y/N)",
                     element='step', multiple="dodge", palette=colors, ax=ax)
        ax.set_title('No. of abortions among patients and non-patients', fontsize=14, fontweight='bold')
        ax.set_xlabel('No. of abortions')
        ax.set_ylabel('Frequency')

    elif graph_option == "Menstruation Cycle among patients and non-patients":
        sns.histplot(data=data, x="Cycle length(days)", hue="PCOS (Y/N)",
                     element='step', multiple="dodge", palette=colors, ax=ax)
        ax.set_title('Menstruation Cycle among patients and non-patients', fontsize=14, fontweight='bold')
        ax.set_xlabel('Menstruation Cycle (days)')
        ax.set_ylabel('Frequency')

    elif graph_option == "Correlation between AMH and LH in patients":
        sns.scatterplot(data=pcos, x="AMH(ng/mL)", y="LH(mIU/mL)", color="maroon", ax=ax)
        ax.set_title('Correlation between AMH and LH in patients', fontsize=14, fontweight='bold')
        ax.set_xlabel('AMH(ng/mL)')
        ax.set_ylabel('LH(mIU/mL)')
        ax.set_xlim(-1, 40)
        ax.set_ylim(-1, 14)

    elif graph_option == "Correlation between BMI and RBS among patients and non-patients":
        sns.lmplot(data=data, x="RBS(mg/dl)", y="BMI", hue="PCOS (Y/N)", palette=colors, height=6, aspect=1.2)
        plt.title('Correlation between BMI and RBS among patients and non-patients', fontsize=14, fontweight='bold')
        plt.xlabel('RBS (mg/dl)')
        plt.ylabel('BMI')
        plt.xlim(0, 250)
        plt.ylim(0, 60)
        st.pyplot(plt.gcf())
        st.stop()  # Evita renderização dupla

    elif graph_option == "Number of follicles among patients and non-patients":
        sns.lmplot(data=data, x='Follicle No. (R)', y='Follicle No. (L)',
                   hue="PCOS (Y/N)", palette=colors, height=6, aspect=1.2)
        plt.title('Number of follicles among patients and non-patients', fontsize=14, fontweight='bold')
        plt.xlabel('Follicle No. (R)')
        plt.ylabel('Follicle No. (L)')
        plt.xlim(-2, 25)
        plt.ylim(-2, 30)
        st.pyplot(plt.gcf())
        st.stop()

    elif graph_option == "Endometrial thickening among patients and non-patients":
        data.boxplot(column='Endometrium (mm)', by='PCOS (Y/N)', whis=[5,95],
                     showfliers=False, patch_artist=True, boxprops=dict(facecolor="mistyrose"),
                     medianprops=dict(color="salmon"), whiskerprops=dict(color="black"), ax=ax)
        ax.set_title('Endometrial thickening among patients and non-patients', fontsize=14, fontweight='bold')
        ax.set_ylabel('Endometrium (mm)')
        ax.set_xlabel('PCOS')
        ax.set_xticklabels(['Without', 'With'])

    # Exibir gráfico
    st.pyplot(fig)