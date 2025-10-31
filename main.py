import streamlit as st
from load_data import load_data
from frontend.parameter import show_parameters_window
from frontend.tables import show_tables_window
from frontend.graph import show_graphs_window
from frontend.clinical_val import show_clinical_eval_window

# Configuração da página
st.set_page_config(
    page_title="PCOS Analysis App",
    page_icon="images/image.ico",
    layout="centered",
)

# Cores e estilos (opcional)
bg_color = "#FFE8CD"
button_color = "#FFD6BA"

# Carregar os dados
data = load_data("PCOS_data.csv")

# Título
st.markdown(
    f"""
    <h2 style='text-align:center; color:black;'>
        Polycystic Ovary Syndrome:<br>
        Exploratory statistical analysis and assessment of the clinical situation
    </h2>
    """,
    unsafe_allow_html=True
)

# Mensagem inicial
st.write("""
Dear user,

**Welcome.**

Polycystic ovary syndrome (PCOS) is an endocrine-gynecological disorder
that affects many women of childbearing age.

In this program, you can:

- Check averages, maximums, and minimums for different parameters  
- View graphs showing relationships between parameters  
- Observe frequency tables for parameters  
- Assess your clinical situation (a PDF will be created)

---

Please select one of the options below:
""")

# Menu de navegação (sidebar)
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    (
        "Home",
        "Exploratory statistical analysis",
        "Frequency tables by parameters",
        "Analysis charts",
        "Clinical Evaluation",
    ),
)

# Renderização de cada página
if page == "Home":
    st.info("Use the sidebar to navigate through the available analyses.")

elif page == "Exploratory statistical analysis":
    show_parameters_window(data)

elif page == "Frequency tables by parameters":
    show_tables_window(data)

elif page == "Analysis charts":
    show_graphs_window(data)

elif page == "Clinical Evaluation":
    show_clinical_eval_window(data)
