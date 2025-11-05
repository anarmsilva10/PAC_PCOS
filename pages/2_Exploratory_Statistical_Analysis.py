import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="PCOS Analysis App",
    page_icon="images/image.ico",
    layout="centered",
)

col1, col2 = st.columns([1, 8])
with col1:
    st.image("images/exploration.png", width=100)
with col2:
    st.title("Exploratory Statistical Analysis")

if 'data' not in st.session_state:
    st.warning("No data, please upload the correct dataset.")
else:
    data = st.session_state['data']

    col_disease = "PCOS (Y/N)"
    if col_disease not in data.columns:
        st.error("Dataset must contain a column named 'PCOS (Y/N)'.")
        st.stop()

    # Datasets
    pcos = data[data[col_disease] == 1]
    no_pcos = data[data[col_disease] == 0]

    # Numeric variables
    numeric_vars = [
        c for c in data.columns
        if pd.api.types.is_numeric_dtype(data[c]) and c != col_disease
    ]
    
    st.subheader("Choose a variable to explore")
    selected_var = st.selectbox("Select variable:", numeric_vars)

    # Compute metrics
    metrics = {
        "Average": (pcos[selected_var].mean(), no_pcos[selected_var].mean()),
        "Maximum": (pcos[selected_var].max(), no_pcos[selected_var].max()),
        "Minimum": (pcos[selected_var].min(), no_pcos[selected_var].min())
    }

    # ===================================================================
    # TABLE
    # ===================================================================
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=["Metric", "PCOS: Presence", "PCOS: Absence"],
            fill_color="#FFE8CD", align="center", font=dict(color="black", size=12)
        ),
        cells=dict(
            values=[
                list(metrics.keys()),
                [f"{v[0]:.2f}" for v in metrics.values()],
                [f"{v[1]:.2f}" for v in metrics.values()]
            ],
            fill_color="#FFD6BA", align="center", font=dict(color="black", size=11)
        )
    )])

    fig.update_layout(
        title=f"{selected_var} vs PCOS presence/absence",
        title_font=dict(color="white", size=16),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    st.plotly_chart(fig, use_container_width=True)

    # ===================================================================
    # Graph
    # ===================================================================
    st.subheader("Comparison Chart")

    pcos_mean = pcos[selected_var].mean()
    nopcos_mean = no_pcos[selected_var].mean()

    fig_bar = go.Figure()
    fig_bar.add_bar(name="PCOS", x=["Average"], y=[pcos_mean], marker_color="maroon")
    fig_bar.add_bar(name="No PCOS", x=["Average"], y=[nopcos_mean], marker_color="lightcoral")

    fig_bar.update_layout(
        title=f"Comparison of {selected_var} average between PCOS and non-PCOS groups",
        title_font=dict(color="white", size=16),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        barmode="group",
    )

    st.plotly_chart(fig_bar, use_container_width=True)