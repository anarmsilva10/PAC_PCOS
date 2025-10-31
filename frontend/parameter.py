import streamlit as st
import plotly.graph_objects as go

def show_parameters_window(data):
    st.subheader("📈 Exploratory Statistical Analysis")

    # Datasets
    pcos = data[data['PCOS (Y/N)'] == 1]
    no_pcos = data[data['PCOS (Y/N)'] == 0]

    # Selection Menu
    option = st.selectbox(
        "Select the parameter to analyze:",
        [
            "Age",
            "Menstruation Cycle",
            "Glucose",
            "Follicle Size",
            "Hormones"
        ]
    )

    def show_table(fig):
        st.plotly_chart(fig, use_container_width=True)

    # -------------------------------------------------------
    # Age
    # -------------------------------------------------------
    if option == "Age":
        mean_with = pcos[' Age (yrs)'].mean()
        max_with = pcos[' Age (yrs)'].max()
        min_with = pcos[' Age (yrs)'].min()

        mean_without = no_pcos[' Age (yrs)'].mean()
        max_without = no_pcos[' Age (yrs)'].max()
        min_without = no_pcos[' Age (yrs)'].min()

        fig = go.Figure(data=[go.Table(
            header=dict(values=['PCOS', 'Average', 'Maximum', 'Minimum'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[
                ['With', 'Without'],
                [f"{mean_with:.2f}", f"{mean_without:.2f}"],
                [max_with, max_without],
                [min_with, min_without]
            ],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11))
        )])
        fig.update_layout(
            title="Analysis of age in relation to PCOS presence/absence",
            title_font=dict(color="black", size=14)
        )
        show_table(fig)

    # -------------------------------------------------------
    # Menstrual Cycle
    # -------------------------------------------------------
    elif option == "Menstruation Cycle":
        mean_with = pcos['Cycle length(days)'].mean()
        max_with = pcos['Cycle length(days)'].max()
        min_with = pcos['Cycle length(days)'].min()

        mean_without = no_pcos['Cycle length(days)'].mean()
        max_without = no_pcos['Cycle length(days)'].max()
        min_without = no_pcos['Cycle length(days)'].min()

        fig = go.Figure(data=[go.Table(
            header=dict(values=['PCOS', 'Average', 'Maximum', 'Minimum'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[
                ['With', 'Without'],
                [f"{mean_with:.2f}", f"{mean_without:.2f}"],
                [max_with, max_without],
                [min_with, min_without]
            ],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11))
        )])
        fig.update_layout(
            title="Menstrual Cycle Length (days) vs PCOS presence/absence",
            title_font=dict(color="black", size=14)
        )
        show_table(fig)

    # -------------------------------------------------------
    # Glucose
    # -------------------------------------------------------
    elif option == "Glucose":
        mean_with = pcos['RBS(mg/dl)'].mean()
        max_with = pcos['RBS(mg/dl)'].max()
        min_with = pcos['RBS(mg/dl)'].min()

        mean_without = no_pcos['RBS(mg/dl)'].mean()
        max_without = no_pcos['RBS(mg/dl)'].max()
        min_without = no_pcos['RBS(mg/dl)'].min()

        fig = go.Figure(data=[go.Table(
            header=dict(values=['PCOS', 'Average', 'Maximum', 'Minimum'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[
                ['With', 'Without'],
                [f"{mean_with:.2f}", f"{mean_without:.2f}"],
                [max_with, max_without],
                [min_with, min_without]
            ],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11))
        )])
        fig.update_layout(
            title="Glucose (mg/dl) vs PCOS presence/absence",
            title_font=dict(color="black", size=14)
        )
        show_table(fig)

    # -------------------------------------------------------
    # Follicle Size
    # -------------------------------------------------------
    elif option == "Follicle Size":
        follicle_parameters = {'Follicle No. (L)': 'Left', 'Follicle No. (R)': 'Right'}

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
            header=dict(values=['Ovary', 'Parameter', 'PCOS:Without', 'PCOS:With'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[ovary_sides, parameter_types, Without_values, With_values],
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])
        fig.update_layout(
            title="Number of Follicles vs PCOS presence/absence",
            title_font=dict(color="black", size=14)
        )
        show_table(fig)

    # -------------------------------------------------------
    # Hormones
    # -------------------------------------------------------
    elif option == "Hormones":
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
            header=dict(values=['Hormone', 'Parameter', 'PCOS:Without', 'PCOS:With'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[hormones, parameter_types, Without_values, With_values],
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])
        fig.update_layout(
            title="Hormone Levels vs PCOS presence/absence",
            title_font=dict(color="black", size=14),
            width=800, height=600
        )
        show_table(fig)