import streamlit as st
from load_data import load_data

# Page configuration
st.set_page_config(
    page_title="PCOS Analysis App",
    page_icon="images/image.ico",
    layout="centered",
)

bg_color = "#FFE8CD"
button_color = "#FFD6BA"

# Title
col1, col2 = st.columns([1, 8])
with col1:
    st.image("images/image_1.png", width=100)
with col2:
    st.header("Polycystic Ovary Syndrome")
st.subheader("Exploratory statistical analysis and assessment of the clinical situation")

# Welcome message
st.write("""
Dear user,

**Welcome!**

Polycystic ovary syndrome (PCOS) is an endocrine-gynecological disorder
that affects many women of childbearing age.

In this program, you can:

- Observe frequency tables for parameters  -> **Frequency Tables Page**
- Check averages, maximums, and minimums for different parameters  -> **Exploratory Statistical Analysis Page**
- View graphs showing relationships between parameters  -> **Analysis Charts Page**
- Assess your clinical situation (a PDF will be created) -> **Clinical Evaluation Page**

---
""")

# Loading data
data = load_data("PCOS_data.csv")

if data is not None:
    st.session_state['data'] = data
    st.success("Dataset uploaded with success!")
else:
    st.warning("No dataset in your folder.")