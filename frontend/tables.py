import streamlit as st
import plotly.graph_objects as go

def show_tables_window(data):
    st.subheader("📊 Frequency Tables")

    # Datasets
    pcos = data[data['PCOS (Y/N)'] == 1]
    no_pcos = data[data['PCOS (Y/N)'] == 0]

    # Select Table
    option = st.selectbox(
        "Select a table to display:",
        [
            "PCOS Presence",
            "BMI",
            "Pregnancy",
            "Weight Gain",
            "Hair Growth",
            "Physical Activity"
        ]
    )

    # -------------------------------------------------------
    # Table PCOS
    # -------------------------------------------------------
    if option == "PCOS Presence":
        PCOS_tot = data['PCOS (Y/N)'].count()
        PCOS_no = no_pcos.shape[0]
        PCOS_yes = pcos.shape[0]

        tab = go.Figure(data=[go.Table(
            header=dict(
                values=['', 'No. of Individuals'],
                line_color='black', fill_color='salmon',
                align='center', font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[
                    ['Total Observations', 'Non-patients', 'Patients'],
                    [PCOS_tot, PCOS_no, PCOS_yes]
                ],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11)
            )
        )])
        tab.update_layout(
            title="Observations Regarding the Presence/Absence of PCOS",
            title_font=dict(color="black", size=14)
        )
        st.plotly_chart(tab, use_container_width=True)

    # -------------------------------------------------------
    # Table BMI
    # -------------------------------------------------------
    elif option == "BMI":
        def cat_bmi(bmi_val):
            if bmi_val < 18.5:
                return 'Low Weight'
            elif 18.5 <= bmi_val < 24.9:
                return 'Normal Weight'
            elif 25 <= bmi_val < 29.9:
                return 'Overweight'
            elif 30 <= bmi_val < 34.9:
                return 'Obesity Class 1'
            elif 35 <= bmi_val < 39.9:
                return 'Obesity Class 2'
            else:
                return 'Obesity Class 3'

        categorias = {
            cat: {'Non-patients': 0, 'Patients': 0, 'Total': 0}
            for cat in ['Low Weight', 'Normal Weight', 'Overweight',
                        'Obesity Class 1', 'Obesity Class 2', 'Obesity Class 3']
        }

        for _, row in data.iterrows():
            bmi_cat = cat_bmi(row['BMI'])
            grupo = 'Patients' if row['PCOS (Y/N)'] == 1 else 'Non-patients'
            categorias[bmi_cat][grupo] += 1
            categorias[bmi_cat]['Total'] += 1

        tab_BMI_data = [[categ, v['Non-patients'], v['Patients'], v['Total']]
                        for categ, v in categorias.items()]
        tab_BMI_data_tr = list(map(list, zip(*tab_BMI_data)))

        tab_BMI = go.Figure(data=[go.Table(
            header=dict(values=['Category', 'Non-patients', 'Patients', 'Total'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=tab_BMI_data_tr,
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])
        tab_BMI.update_layout(title="Nutritional Status of Individuals",
                              title_font=dict(color="black", size=14))
        st.plotly_chart(tab_BMI, use_container_width=True)

    # -------------------------------------------------------
    # Table Pregnancy
    # -------------------------------------------------------
    elif option == "Pregnancy":
        Grav_tot = data[data['Pregnant(Y/N)'] == 1].shape[0]
        Grav_nd = data[(data['Pregnant(Y/N)'] == 1) & (data['PCOS (Y/N)'] == 0)].shape[0]
        Grav_PCOS = data[(data['Pregnant(Y/N)'] == 1) & (data['PCOS (Y/N)'] == 1)].shape[0]

        tab_Grav = go.Figure(data=[go.Table(
            header=dict(values=['', 'No. of Individuals'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[['Total Observations', 'Non-patients', 'Patients'],
                               [Grav_tot, Grav_nd, Grav_PCOS]],
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])
        tab_Grav.update_layout(title="Number of Pregnant Patients",
                               title_font=dict(color="black", size=14))
        st.plotly_chart(tab_Grav, use_container_width=True)

    # -------------------------------------------------------
    # Table Weight Gain
    # -------------------------------------------------------
    elif option == "Weight Gain":
        gp_tot = data[data['Weight gain(Y/N)'] == 1].shape[0]
        sgp_tot = data[data['Weight gain(Y/N)'] == 0].shape[0]
        gp_nd = data[(data['Weight gain(Y/N)'] == 1) & (data['PCOS (Y/N)'] == 0)].shape[0]
        gp_PCOS = data[(data['Weight gain(Y/N)'] == 1) & (data['PCOS (Y/N)'] == 1)].shape[0]
        sgp_nd = data[(data['Weight gain(Y/N)'] == 0) & (data['PCOS (Y/N)'] == 0)].shape[0]
        sgp_PCOS = data[(data['Weight gain(Y/N)'] == 0) & (data['PCOS (Y/N)'] == 1)].shape[0]

        tab_gp = go.Figure(data=[go.Table(
            header=dict(values=['', 'No weight gain', 'Weight gain'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[['Total Observations', 'Non-patients', 'Patients'],
                               [sgp_tot, sgp_nd, sgp_PCOS],
                               [gp_tot, gp_nd, gp_PCOS]],
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])
        tab_gp.update_layout(title="Weight Gain",
                             title_font=dict(color="black", size=14))
        st.plotly_chart(tab_gp, use_container_width=True)

    # -------------------------------------------------------
    # Table Hair Growth
    # -------------------------------------------------------
    elif option == "Hair Growth":
        cp_tot = data[data['hair growth(Y/N)'] == 1].shape[0]
        scp_tot = data[data['hair growth(Y/N)'] == 0].shape[0]
        cp_nd = data[(data['hair growth(Y/N)'] == 1) & (data['PCOS (Y/N)'] == 0)].shape[0]
        cp_PCOS = data[(data['hair growth(Y/N)'] == 1) & (data['PCOS (Y/N)'] == 1)].shape[0]
        scp_nd = data[(data['hair growth(Y/N)'] == 0) & (data['PCOS (Y/N)'] == 0)].shape[0]
        scp_PCOS = data[(data['hair growth(Y/N)'] == 0) & (data['PCOS (Y/N)'] == 1)].shape[0]

        tab_cp = go.Figure(data=[go.Table(
            header=dict(values=['', 'No growth', 'Growth'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[['Total Observations', 'Non-patients', 'Patients'],
                               [scp_tot, scp_nd, scp_PCOS],
                               [cp_tot, cp_nd, cp_PCOS]],
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])
        tab_cp.update_layout(title="Hair Growth",
                             title_font=dict(color="black", size=14))
        st.plotly_chart(tab_cp, use_container_width=True)

    # -------------------------------------------------------
    # Table Physical Activity
    # -------------------------------------------------------
    elif option == "Physical Activity":
        regex_tot = data[data['Reg.Exercise(Y/N)'] == 1].shape[0]
        sregex_tot = data[data['Reg.Exercise(Y/N)'] == 0].shape[0]
        regex_nd = data[(data['Reg.Exercise(Y/N)'] == 1) & (data['PCOS (Y/N)'] == 0)].shape[0]
        regex_PCOS = data[(data['Reg.Exercise(Y/N)'] == 1) & (data['PCOS (Y/N)'] == 1)].shape[0]
        sregex_nd = data[(data['Reg.Exercise(Y/N)'] == 0) & (data['PCOS (Y/N)'] == 0)].shape[0]
        sregex_PCOS = data[(data['Reg.Exercise(Y/N)'] == 0) & (data['PCOS (Y/N)'] == 1)].shape[0]

        tab_regex = go.Figure(data=[go.Table(
            header=dict(values=['', 'No physical activity', 'Physical activity'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=11)),
            cells=dict(values=[['Total Observations', 'Non-patients', 'Patients'],
                               [sregex_tot, sregex_nd, sregex_PCOS],
                               [regex_tot, regex_nd, regex_PCOS]],
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])
        tab_regex.update_layout(title="Regular Physical Activity",
                                title_font=dict(color="black", size=14))
        st.plotly_chart(tab_regex, use_container_width=True)
