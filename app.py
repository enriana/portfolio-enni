import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Enni Jermias | Data Analyst Portfolio",
    page_icon="🌸",
    layout="wide"
)

# --- CUSTOM CSS FOR CREAM/PINK THEME ---
st.markdown("""
<style>
/* Main color theme */
:root {
    --primary-color: #D8A7B1; /* Darker pink for headers and accents */
    --secondary-color: #FADADD; /* Lighter pink for backgrounds */
    --background-color: #FAF4F4; /* Creamy off-white background */
    --text-color: #4B4453; /* Dark text for readability */
    --sidebar-background: #FFF8F0; /* Light cream for sidebar */
}
.stApp { background-color: var(--background-color); }
[data-testid="stSidebar"] { background-color: var(--sidebar-background); }
h1, h2 { color: var(--primary-color); }
h3 { color: var(--text-color); }
[data-testid="stExpander"] {
    background-color: white;
    border-radius: 10px;
    border: 1px solid var(--secondary-color);
}
[data-testid="stExpander"] > div[role="button"] {
    color: var(--text-color);
    font-weight: bold;
}
[data-testid="stMetricLabel"] { color: var(--text-color); }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://i.imgur.com/8HIgpLT.jpeg", width=150)
    st.title("Enni Jermias")
    st.subheader("Data Analyst")
    
    st.divider()
    st.subheader("📬 Contact")
    st.markdown("""
    - **Email:** [enni.jermias@gmail.com](mailto:enni.jermias@gmail.com)
    - **Location:** Malang, Indonesia (Open to relocate)
    """)
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/enni-jermias)")

# --- MAIN CONTENT ---
st.title("👩‍💻 Data Analyst Portfolio")
st.divider()

# --- ABOUT ME ---
st.header("About Me")
st.markdown("""
As an aspiring Data Analyst driven by core values of integrity, accuracy, and proactive problem-solving, I leverage a strong foundation from my previous role as an Office Administration Section Head. In that capacity, I moved beyond traditional management to spearhead data-informed initiatives, leading my team to a **25% increase in on-time service completion** by implementing a metrics-based performance system and improving overall process efficiency by **40%**. 

This experience honed my business acumen and stakeholder communication skills, which are now complemented by my proficiency in modern analytical tools including **SQL, Python, and Tableau**. I offer a unique combination of proven business problem-solving experience and the technical capabilities required to translate complex data into actionable, high-impact insights.
""")

# --- PROFESSIONAL EXPERIENCE ---
st.header("🏢 Professional Experience")
st.subheader("PT. Bank Central Asia, Tbk - KCU Tuban")
col1, col2 = st.columns(2)
with col1:
    st.subheader("➤ Office Administration Section Head")
    st.caption("August 2013 – June 2023")
    st.subheader("➤ Office Administration Staff")
    st.caption("May 2011 – July 2013")
with col2:
    st.subheader("➤ Finance Staff")
    st.caption("July 2009 – April 2011")
    st.subheader("➤ Operational Support Staff")
    st.caption("April 2009 – June 2009")

# --- SKILLS ---
st.header("🛠️ Skills")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Technical Skills")
    st.markdown("""
    - **Programming Languages:** SQL, Python
    - **Libraries:** Pandas, Matplotlib, Seaborn, Scikit-learn
    - **Data Visualization:** Tableau, Streamlit
    - **Other Tools:** Advanced Microsoft Excel
    """)
with col2:
    st.subheader("Professional Skills")
    st.markdown("""
    - **Business Acumen & Financial Analysis**
    - **Problem Solving & Root Cause Analysis**
    - **Stakeholder Management & Communication**
    - **Project Management & Process Optimization**
    """)
st.divider()

# --- PROJECTS ---
st.header("📂 Projects")

# --- Project 1: Spotify ---
with st.expander("▶️ **Project 1: Predicting Spotify Track Skips to Improve User Engagement**", expanded=True):
    st.markdown("**Objective:** To improve user engagement and retention, the project's goal was to develop a machine learning model that predicts whether a user will skip a track with at least 70% accuracy, enabling the refinement of Spotify's recommendation algorithm.")
    st.markdown("**Methodology:** Analyzed ~150,000 streaming records using **Python (Pandas)**, built a **Tuned Weighted Random Forest** model with **Scikit-learn**, and visualized findings in an interactive **Streamlit** dashboard.")
    
    st.markdown("**Key Results & Metrics:**")
    metric_cols = st.columns(3)
    metric_cols[0].metric(label="Model Accuracy", value="91.12%")
    metric_cols[1].metric(label="Skips in First 30s", value="77.4%")
    metric_cols[2].metric(label="Skips on Android", value="93.5%")
    
    st.markdown("[View PDF](https://drive.google.com/file/d/1vSLozk2oMHycUSwZh4fb0z8em722d369/view?usp=sharing)")
    st.markdown("[View Dashboard](https://spotify-skip-prediction-dashboard.streamlit.app/?embed_options=light_theme)")
    
# --- Project 2: RevoBank ---
with st.expander("💳 **Project 2: RevoBank Sales Performance & Customer Segmentation**"):
    st.markdown("**Objective:** To segment existing credit card clients into distinct user personas based on their financial profiles and transaction behaviors to drive higher, more targeted engagement.")
    st.markdown("**Methodology:** Performed data cleaning and feature engineering using **Python (Pandas)** and applied **K-Means Clustering (Scikit-learn)** to segment users based on metrics like transaction recency, frequency, and Debt-to-Income ratio.")
    
    st.markdown("**Identified Customer Segments:**")
    st.success("""
    - **The Engaged Spender:** Highly active, financially healthy, and high-value.
    - **The Latent User:** Inactive but with high income, representing significant untapped potential.
    """)
    st.markdown("[View Deck](https://docs.google.com/presentation/d/1qrlX4-W6nHXHCN2Qsdh9sn0r_aMyTPKx1tzqrYytwj4/edit?usp=sharing)")

st.divider()


