import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Enni Jermias | Data Analyst Portfolio",
    page_icon="🌸",
    layout="wide"
)

# --- CUSTOM CSS FOR CREAM/PINK THEME (VISUAL ASPECT INTACT) ---
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

/* Apply background colors */
.stApp {
    background-color: var(--background-color);
}

[data-testid="stSidebar"] {
    background-color: var(--sidebar-background);
}

/* Style headers */
h1, h2 {
    color: var(--primary-color);
}

h3 {
    color: var(--text-color);
}

/* Style expanders */
[data-testid="stExpander"] {
    background-color: white;
    border-radius: 10px;
    border: 1px solid var(--secondary-color);
}

[data-testid="stExpander"] > div[role="button"] {
    color: var(--text-color);
    font-weight: bold;
}

/* Style metric labels */
[data-testid="stMetricLabel"] {
    color: var(--text-color);
}

</style>
""", unsafe_allow_html=True)


# --- SIDEBAR ---
with st.sidebar:
    # st.image("https://i.imgur.com/6f20s2s.png", width=150) # Uncomment as a Placeholder for a profile picture
    st.title("Enni Jermias")
    st.subheader("Data Analyst")
    
    st.divider()
    st.subheader("📬 Contact")
    st.markdown("""
    - **Email:** [enni.jermias@gmail.com](mailto:enni.jermias@gmail.com)
    - **Phone:** [+62 881082942028](https://wa.me/qr/56T47ETWWYZ3D1)
    - **Location:** Malang, Indonesia (Open to relocate)
    """)
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/enni-jermias)") # Uncomment and add your LinkedIn

# --- MAIN CONTENT ---

# --- HERO SECTION ---
st.title("👩‍💻 Data Analyst Portfolio")
st.divider()

# --- ABOUT ME ---
st.header("About Me")
st.markdown("""
As an aspiring Data Analyst driven by core values of integrity, accuracy, and proactive problem-solving, I leverage a strong foundation from my previous role as an Office Administration Section Head. In that capacity, I moved beyond traditional management to spearhead data-informed initiatives, successfully **cutting operational costs by 12%** and **improving process efficiency by 40%** by analyzing operational data. 

This experience honed my business acumen and stakeholder communication skills, which are now complemented by my proficiency in modern analytical tools including **SQL, Python, and Tableau**. I offer a unique combination of proven business problem-solving experience and the technical capabilities required to translate complex data into actionable, high-impact insights.
""")
st.divider()

# --- SKILLS ---
st.header("🛠️ Skills")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Technical Skills")
    st.markdown("""
    - **Languages:** SQL, Python (Pandas, Matplotlib, Seaborn, Scikit-learn)
    - **BI & Visualization:** Tableau, Streamlit
    - **Spreadsheets:** Advanced Microsoft Excel
    - **Statistical Concepts:** Descriptive Statistics, K-Means Clustering
    """)
    
with col2:
    st.subheader("Professional Skills")
    st.markdown("""
    - **Business Acumen & Financial Analysis**
    - **Problem Solving & Root Cause Analysis**
    - **Stakeholder Management & Communication**
    - **Process Optimization & Operations Management**
    """)
st.divider()

# --- PORTFOLIO PROJECTS ---
st.header("📂 Portfolio Projects")

# --- Project 1: Spotify ---
with st.expander("▶️ **Project 1: Predicting Spotify Track Skips to Improve User Engagement**", expanded=True):
    p1_col1, p1_col2 = st.columns([2, 1])
    with p1_col1:
        st.markdown("**Objective:** Develop a machine learning model to predict track skips with over 70% accuracy to refine Spotify's recommendation algorithm.")
        st.markdown("""
        **Methodology:** Analyzed ~150,000 streaming records using **Python (Pandas)**, built a **Tuned Weighted Random Forest** model with **Scikit-learn**, and visualized findings in an interactive **Streamlit** dashboard.
        """)
        
        st.markdown("**Key Results & Metrics:**")
        metric_cols = st.columns(3)
        metric_cols[0].metric(label="Model Accuracy", value="91.12%")
        metric_cols[1].metric(label="Skips in First 30s", value="77.4%")
        metric_cols[2].metric(label="Skips on Android", value="93.5%")
    
    with p1_col2:
        # Image removed as requested, only caption remains
        st.caption("Feature Importance for Skip Prediction")
        
        st.markdown("**Actionable Recommendations:**")
        st.info("""
        1.  **Optimize the First 30 Seconds:** Prioritize tracks with strong openings.
        2.  **Investigate the Android Platform:** Conduct a full UX audit on the Android app.
        3.  **Implement Time-Aware Recommendations:** Adapt suggestions to user context (e.g., time of day).
        """)
        # st.markdown("[View on GitHub](https://github.com/your-username/your-repo-name)") # Uncomment & Add your link here

# --- Project 2: RevoBank ---
with st.expander("💳 **Project 2: RevoBank Sales Performance & Customer Segmentation**"):
    p2_col1, p2_col2 = st.columns([2, 1])
    with p2_col1:
        st.markdown("**Objective:** Analyze sales performance and segment credit card customers to develop targeted engagement strategies.")
        st.markdown("""
        **Methodology:** Performed data cleaning using **Python (Pandas)** and applied **K-Means Clustering (Scikit-learn)** to segment users based on financial profiles and transaction behaviors.
        """)
        
        st.markdown("**Identified Customer Segments:**")
        st.success("""
        - **The Engaged Spender:** Highly active, financially healthy, and high-value.
        - **The Latent User:** Inactive but with high income, representing untapped potential.
        """)

    with p2_col2:
        # Image removed as requested, only caption remains
        st.caption("Chart: Customer Segments by Income and Spending")

        st.markdown("**Actionable Recommendations:**")
        st.info("""
        1.  **For "The Engaged Spender" (Retention):** Implement tiered loyalty programs and personalized offers.
        2.  **For "The Latent User" (Activation):** Launch campaigns with first-transaction incentives.
        """)
        # st.markdown("[View on GitHub](https://github.com/your-username/your-repo-name)") # Uncomment & Add your link here

st.divider()

# --- PROFESSIONAL & PROJECT EXPERIENCE ---
st.header("🏢 Professional & Project Experience")

st.subheader("Office Administration Section Head | PT. Bank Central Asia, Tbk")
st.caption("August 2013 – June 2023")
st.markdown("""
- **Analyzed** the multi-billion rupiah operational budget to achieve a **12% annual cost reduction** by identifying and resolving critical spending anomalies.
- **Streamlined** core administrative workflows using data, resulting in a **40% reduction in process lead times**.
- **Ensured 100% accuracy** in key financial reconciliations by conducting forensic data analysis.
- **Led** a team to a **25% increase in on-time completion rate** by implementing a metrics-based performance system.
""")

st.subheader("Key Project: New Branch Office Building Construction | PT. Bank Central Asia, Tbk")
st.caption("December 2019 – September 2021")
st.markdown("""
- **Managed** all on-site vendor logistics and asset lifecycle, coordinating installation of **800+ new assets** while generating over **IDR 300 Million** from the sale of old equipment.
- **Orchestrated** the complex overnight relocation of the entire **100+ employee branch**, achieving **zero operational downtime** and ensuring **100% business continuity**.
- **Spearheaded** all branch-level stakeholder coordination, securing all local operational permits ahead of schedule to prevent any project delays.
""")
