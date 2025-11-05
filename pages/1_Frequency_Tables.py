import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="PCOS Analysis App",
    page_icon="images/image.ico",
    layout="centered",
)

col1, col2 = st.columns([1, 8])
with col1:
    st.image("images/frequency.png", width=100)
with col2:
    st.title("Frequency Tables")

data = st.session_state.get("data", None)
if data is None:
    st.warning("No dataset loaded.")
    st.stop()

# Disease variable (Y-1/N-0)
col_disease = "PCOS (Y/N)"

# Selection of variable to study
variable = [c for c in data.columns if c != col_disease]
var = st.selectbox("Select a variable to analyze:", variable)

# Variable type
if np.issubdtype(data[var].dtype, np.number):
    type = "numeric"
else:
    type = "categorical"

# ===================================================================
# Numeric Variable
# ===================================================================

if type == 'numeric':
    bins = st.slider("Number of intervals:", min_value=3, max_value=20, value=6)

    data['_interval'] = pd.cut(data[var], bins=bins)
    group_var = '_interval'
else:
    group_var = var

# ===================================================================
# TABLE
# ===================================================================
table = pd.crosstab(data[group_var], data[col_disease], margins=True)
table.columns = ['No PCOS', 'PCOS', 'Total']
table = table.reset_index().rename(columns={group_var: "Category"})

# Percentages
total_obs = table.loc[table["Category"] == "All", "Total"].values[0]
table["Percent (%)"] = (table["Total"] / total_obs * 100).round(1)

table_display = table[table["Category"] != "All"].copy()

table_display["Category"] = table_display["Category"].apply(
    lambda x: f"[{x.left:.1f} – {x.right:.1f}]" if isinstance(x, pd.Interval) else str(x)
)

st.subheader(f"Distribution of {var} by PCOS presence")

# Table configuration
fig = go.Figure(data=[go.Table(
    header=dict(values=["Category", "No PCOS", "PCOS", "Total", "Percent (%)"],
                fill_color='#FFE8CD', align='center', font=dict(color='black', size=12)),
    cells=dict(values=[
        table_display["Category"],
        table_display["No PCOS"],
        table_display["PCOS"],
        table_display["Total"],
        table_display["Percent (%)"]
    ],
        fill_color='#FFD6BA', align='center', font=dict(color='black', size=12)))
])
fig.update_layout(title=f"Distribution of {var} by PCOS presence")
st.plotly_chart(fig, use_container_width=True)

# ===================================================================
# Graph
# ===================================================================

st.subheader("Comparison chart")
table_display["Category"] = table_display["Category"].astype(str)

fig_bar = px.bar(
    table_display,
    x="Category",
    y=["No PCOS", "PCOS"],
    barmode="stack", 
    color_discrete_map={
        "No PCOS": "lightcoral",  
        "PCOS": "maroon"      
    },
    title=f"Comparison of {var} between PCOS and non-PCOS groups"
)

# Optional: tweak layout
fig_bar.update_layout(
    xaxis_title="Category",
    yaxis_title="Number of individuals",
    title_font=dict(size=16, color="white"),
    legend_title_text="Group",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)", 
    font=dict(color="white"),
)

st.plotly_chart(fig_bar, use_container_width=True)

# Clean data
if "_interval" in data.columns:
    data.drop(columns=["_interval"], inplace=True)