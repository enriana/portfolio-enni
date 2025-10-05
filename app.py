import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Enni Jermias | Data Analyst Portfolio",
    page_icon="🌸",
    layout="wide"
)

# --- CUSTOM CSS FOR CREAM/PINK THEME ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# You can create a style.css file with the content below, or embed it directly.
# For simplicity, we'll embed it.
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
    # You can upload a professional headshot to your GitHub repo and link it here
    # Placeholder for a profile picture
    st.title("Enni Jermias")
    st.subheader("Data Analyst")
    st.markdown("""
    A results-oriented professional with 14+ years in banking, now applying a deep understanding of business operations and data to solve complex problems as a Data Analyst.
    """)
    
    st.divider()
    st.subheader("📬 Contact Information")
    st.markdown(f"""
    📧 **Email:** `enni.jermias@gmail.com`
    📞 **Phone:** `+62 881082942028`
    """
    )
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/enni-jermias)") # Uncomment and add your LinkedIn

# --- MAIN CONTENT ---

# --- HERO SECTION ---
st.title("👩‍💻 Data Analyst Portfolio")
st.divider()

# --- ABOUT ME ---
st.subheader("About Me")
st.markdown("""
Hello! My career has been centered on using data to solve real-world business problems, from optimizing multi-billion rupiah budgets to streamlining core operational processes.

My unique strength is the combination of a **proven business mindset with modern technical capabilities**. I don't just process data; I understand the "why" behind it, ensuring my analysis is always grounded in business context to deliver relevant and impactful insights.
""")
st.divider()

# --- SKILLS ---
st.subheader("🛠️ Skills")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Technical Skills")
    st.markdown("""
    - **📊 BI & Visualization:** Tableau, Streamlit
    - **🐍 Python:** Pandas, Matplotlib, Seaborn, Scikit-learn
    - **🗃️ Database:** SQL
    - **📈 Spreadsheets:** Advanced Microsoft Excel
    """)
    
with col2:
    st.markdown("#### Professional Skills")
    st.markdown("""
    - **💼 Business Acumen & Financial Analysis**
    - **🧠 Root Cause & Problem Solving**
    - **🤝 Stakeholder Management & Communication**
    - **⚙️ Process Optimization**
    """)
st.divider()

# --- PORTFOLIO PROJECTS ---
st.subheader("📂 Portfolio Projects")

# --- Project 1: Spotify ---
with st.expander("▶️ **Project 1: Predicting Spotify Track Skips to Improve User Engagement**", expanded=True):
    p1_col1, p1_col2 = st.columns([2, 1])
    with p1_col1:
        st.markdown("**Objective:** Develop a machine learning model to predict track skips with >70% accuracy to refine Spotify's recommendation algorithm.")
        st.markdown("""
        **Methodology:**
        - Analyzed ~150,000 streaming records using **Python (Pandas)**.
        - Built and tuned a **Weighted Random Forest** model using **Scikit-learn**.
        - Visualized findings and created an interactive dashboard with **Streamlit**.
        """)
        
        st.markdown("**Key Results & Metrics:**")
        metric_cols = st.columns(3)
        metric_cols[0].metric(label="Model Accuracy", value="91.12%")
        metric_cols[1].metric(label="Skips in First 30s", value="77.4%")
        metric_cols[2].metric(label="Skips on Android", value="93.5%")
    
    with p1_col2:
        # Placeholder image - replace with an actual chart from your project
        # st.image("https://i.imgur.com/M2L3s5p.png", caption="Feature Importance for Skip Prediction")
        
        st.markdown("**Actionable Recommendations:**")
        st.info("""
        1.  **Optimize the First 30 Seconds:** Prioritize tracks with strong openings.
        2.  **Investigate the Android Platform:** Conduct a UX audit on the Android app.
        3.  **Implement Time-Aware Recommendations:** Adapt suggestions to user context (e.g., time of day).
        """)
        # st.markdown("[View on GitHub](https://github.com/your-username/your-repo-name)") # Add your link here


# --- Project 2: RevoBank ---
with st.expander("💳 **Project 2: RevoBank Sales Performance & Customer Segmentation**"):
    p2_col1, p2_col2 = st.columns([2, 1])
    with p2_col1:
        st.markdown("**Objective:** Analyze sales performance and segment credit card customers to develop targeted engagement strategies for RevoBank.")
        st.markdown("""
        **Methodology:**
        - Performed data cleaning and feature engineering using **Python (Pandas)**.
        - Applied **K-Means Clustering (Scikit-learn)** to segment users.
        - Visualized segment characteristics using **Matplotlib and Seaborn**.
        """)
        
        st.markdown("**Identified Customer Segments:**")
        st.success("""
        - **The Engaged Spender:** Highly active, financially healthy, and high-value.
        - **The Latent User:** Inactive but with high income, representing significant untapped potential.
        """)

    with p2_col2:
        # Placeholder image - replace with an actual chart from your project
        # st.image("https://i.imgur.com/2s3ScCa.png", caption="Customer Segments by Income and Spending")

        st.markdown("**Actionable Recommendations:**")
        st.info("""
        1.  **For "The Engaged Spender" (Retention):** Implement tiered loyalty programs and personalized offers.
        2.  **For "The Latent User" (Activation):** Launch campaigns with first-transaction incentives.
        """)
        # st.markdown("[View on GitHub](https://github.com/your-username/your-repo-name)") # Add your link here

st.divider()

# --- PROFESSIONAL EXPERIENCE ---
st.subheader("🏢 Professional Experience")
exp_col1, exp_col2 = st.columns([1, 4])
with exp_col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Bank_Central_Asia.svg/1200px-Bank_Central_Asia.svg.png", width=80) # BCA Logo
with exp_col2:
    st.markdown("#### Office Administration Supervisor | PT Bank Central Asia, Tbk (BCA)")
    st.caption("August 2013 – June 2023")

st.markdown("""
- **Analyzed** the multi-billion rupiah operational budget to achieve a **12% annual cost reduction**.
- **Streamlined** core administrative workflows using data, resulting in a **40% reduction in process lead times**.
- **Ensured 100% accuracy** in key financial reconciliations by conducting forensic data analysis.
- **Led** a team to a **25% increase in on-time completion rate** by implementing a metrics-based performance system.
""")
