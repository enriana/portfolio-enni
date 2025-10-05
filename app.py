import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Enni Jermias | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide"
)

# --- SIDEBAR ---
with st.sidebar:
    st.header("Enni Jermias")
    st.subheader("Data Analyst")
    st.image("https://www.iconpacks.net/icons/2/free-user-icon-3296-thumb.png") # Placeholder image
    st.markdown("""
    A results-oriented professional with 14+ years in banking, now applying a deep understanding of business operations and data to solve complex problems as a Data Analyst.
    """)
    
    st.divider()
    st.subheader("Contact Information")
    st.info(f"""
    📧 **Email:** enni.jermias@gmail.com\n
    📞 **Phone:** +62 881082942028
    """)
    # You can add a link to your LinkedIn profile here if you have one
    # st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/your-profile-url/)")

# --- MAIN CONTENT ---
st.title("📊 Data Analyst Portfolio")
st.markdown("---")

# --- ABOUT ME ---
st.header("About Me")
st.markdown("""
Hello! I'm Enni Jermias. My career has been centered on using data to solve real-world business problems, from optimizing multi-billion rupiah budgets to streamlining core operational processes.

My unique strength is the combination of a **proven business mindset with modern technical capabilities**. I don't just process data; I understand the "why" behind it, ensuring my analysis is always grounded in business context to deliver relevant and impactful insights.
""")
st.markdown("---")


# --- SKILLS ---
st.header("Skills")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Technical Skills")
    st.markdown("""
    - **Languages:** SQL, Python (Pandas, Matplotlib, Seaborn, Scikit-learn)
    - **BI & Visualization:** Tableau, Streamlit
    - **Spreadsheets:** Advanced Microsoft Excel (Pivot Tables, VLOOKUP)
    - **Statistical Concepts:** Descriptive Statistics, K-Means Clustering
    """)
    
with col2:
    st.subheader("Professional Skills")
    st.markdown("""
    - **Business Acumen & Financial Analysis**
    - **Root Cause & Problem Solving**
    - **Stakeholder Management & Communication**
    - **Process Optimization**
    """)
st.markdown("---")

# --- PORTFOLIO PROJECTS ---
st.header("Portfolio Projects")

# Project 1: Spotify
with st.expander("▶️ Project 1: Predicting Spotify Track Skips to Improve User Engagement", expanded=True):
    st.markdown("**Objective:** Develop a machine learning model to predict track skips with >70% accuracy to refine Spotify's recommendation algorithm.")
    
    st.markdown("**Methodology:**")
    st.markdown("""
    - Analyzed ~150,000 streaming records using Python (`pandas`).
    - Built and tuned a **Weighted Random Forest** classification model using `scikit-learn`.
    - Visualized findings with `seaborn` and `matplotlib` and presented them in an interactive `Streamlit` dashboard.
    """)
    
    st.markdown("**Key Insights & Results:**")
    metric1, metric2, metric3 = st.columns(3)
    metric1.metric(label="Model Accuracy", value="91.12%")
    metric2.metric(label="Skips in First 30s", value="77.4%")
    metric3.metric(label="Skips on Android", value="93.5%")
    
    st.markdown("**Actionable Recommendations:**")
    st.markdown("""
    1.  **Optimize the First 30 Seconds:** Prioritize tracks with strong openings as a key signal for recommendations.
    2.  **Investigate the Android Platform:** Conduct a full UX audit on the Android app to resolve potential friction points.
    3.  **Implement Time-Aware Recommendations:** Adapt suggestions to the user's context (e.g., calmer music late at night).
    """)

# Project 2: RevoBank
with st.expander("💳 Project 2: RevoBank Sales Performance & Customer Segmentation"):
    st.markdown("**Objective:** Analyze sales performance and segment credit card customers to develop targeted engagement strategies for RevoBank.")
    
    st.markdown("**Methodology:**")
    st.markdown("""
    - Performed data cleaning and feature engineering on 6 months of transaction data using `Python` and `pandas`.
    - Applied **K-Means Clustering** (`scikit-learn`) to segment users based on transaction behavior and financial profiles.
    - Visualized segment characteristics using `matplotlib` and `seaborn`.
    """)
    
    st.markdown("**Key Insights & Results:**")
    st.markdown("""
    Identified two primary customer segments:
    - **The Engaged Spender:** Highly active, financially healthy, and high-value. Represents a key group for retention.
    - **The Latent User:** Inactive but with high income, representing significant untapped potential.
    """)
    
    st.markdown("**Actionable Recommendations:**")
    st.markdown("""
    1.  **For "The Engaged Spender" (Retention):** Implement tiered loyalty programs and provide personalized offers.
    2.  **For "The Latent User" (Activation):** Launch campaigns with first-transaction incentives and improve the new client onboarding process.
    """)
st.markdown("---")

# --- PROFESSIONAL EXPERIENCE ---
st.header("Professional Experience")
st.subheader("Office Administration Supervisor | PT Bank Central Asia, Tbk (BCA)")
st.caption("August 2013 – June 2023")
st.markdown("""
- **Analyzed** the multi-billion rupiah operational budget to achieve a **12% annual cost reduction** by identifying and resolving critical spending anomalies.
- **Streamlined** core administrative workflows using data, resulting in a **40% reduction in process lead times**.
- **Ensured 100% accuracy** in key financial reconciliations by conducting forensic data analysis to eliminate a recurring systemic error.
- **Led** the administrative team to achieve a **25% increase in the on-time completion rate** of internal service requests by implementing a metrics-based performance system.
""")