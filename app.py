import streamlit as st
import pandas as pd
import altair as alt

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
st.title("🗂️ Data Analyst Portfolio")
st.divider()

# --- ABOUT ME ---
st.header("🙋‍♀️ About Me")
st.markdown("""
As an aspiring Data Analyst driven by core values of integrity, accuracy, and proactive problem-solving, I leverage a strong foundation from my previous role as an Office Administration Section Head. In that capacity, I moved beyond traditional management to spearhead data-informed initiatives, leading my team to a **25% increase in on-time service completion** by implementing a metrics-based performance system and improving overall process efficiency by **40%**. 

This experience honed my business acumen and stakeholder communication skills, which are now complemented by my proficiency in modern analytical tools including **SQL, Python, and Tableau**. I offer a unique combination of proven business problem-solving experience and the technical capabilities required to translate complex data into actionable, high-impact insights.
""")

# --- EDUCATION ---
st.header("🎓 Education")

# Create columns for Education
edu1, edu2, edu3 = st.columns(3)

with edu1:
    st.markdown("**[RevoU](https://www.google.com/search?q=RevoU)**")
    st.caption("June 2025 – September 2025")
    st.markdown("Full-stack Data Analytics")
    
with edu2:
    st.markdown("**[Program Pendidikan Akuntansi (PPA) BCA](https://www.google.com/search?q=Program+Pendidikan+Akuntansi+(PPA)+BCA)**")
    st.caption("2006 – 2009")
    st.markdown("PT. Bank Central Asia, Tbk")
    
with edu3:
    st.markdown("**[SMAK Santa Maria Malang](https://www.google.com/search?q=SMAK+Santa+Maria+Malang)**")
    st.caption("2003 – 2006")
    st.markdown("Senior High School")

# --- PROFESSIONAL EXPERIENCE ---
st.header("🏢 Professional Experience")
# --- REFINED SECTION ---
# Create columns for the logo and the subheader
logo_col, title_col = st.columns([1,5])  # Adjust ratio as needed
with logo_col:
    # Add the BCA logo. You can find a good URL online.
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Bank_Central_Asia.svg/1200px-Bank_Central_Asia.svg.png", width=150)
with title_col:
    st.subheader("PT. Bank Central Asia, Tbk - KCU Tuban")
    
col1, col2 = st.columns(2)
with col1:
    st.markdown("**➤ Office Administration Section Head**")
    st.caption("    August 2013 – June 2023")
    st.markdown("**➤ Office Administration Staff**")
    st.caption("    May 2011 – July 2013")
with col2:
    st.markdown("**➤ Finance Staff**")
    st.caption("    July 2009 – April 2011")
    st.markdown("**➤ Operational Support Staff**")
    st.caption("    April 2009 – June 2009")

# --- SKILLS ---
st.header("🛠️ Skills")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Technical Skills")
    st.markdown("""
    - **Programming Languages:** SQL, Python
    - **Libraries:** Pandas, Matplotlib, Seaborn, Scikit-learn
    - **Data Visualization:** Tableau, Streamlit. Power BI
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
with st.expander("🎧 **Project 1: Predicting Spotify Track Skips to Improve User Engagement**", expanded=True):
    st.markdown("**Objective:** To improve user engagement and retention, the project's goal was to develop a machine learning model that predicts whether a user will skip a track with at least 70% accuracy, enabling the refinement of Spotify's recommendation algorithm.")
    st.markdown("**Methodology:** Analyzed ~150,000 streaming records using **Python (Pandas)**, built a **Tuned Weighted Random Forest** model with **Scikit-learn**, and visualized findings in an interactive **Streamlit** dashboard.")
    
    st.markdown("**Key Results & Metrics:**")
    metric_cols = st.columns(3)
    metric_cols[0].metric(label="Model Accuracy", value="91.12%")
    
    metric_cols[1].metric(label="Skips in First 30s of a Track", value="77.4%")
    metric_cols[1].caption("Highlights the importance of immediate engagement, as most skips occur in the first 30s.")
    
    metric_cols[2].metric(label="Skips on Android", value="93.5%")
    metric_cols[2].caption("Suggests potential platform-specific (UX/technical) issues on Android.")
    
    st.markdown("[View PDF 📋](https://drive.google.com/file/d/1vSLozk2oMHycUSwZh4fb0z8em722d369/view?usp=sharing)")
    st.markdown("[View Dashboard 📊](https://spotify-skip-prediction-dashboard.streamlit.app/?embed_options=light_theme)")
    
# --- Project 2: RevoBank ---
with st.expander("💳 **Project 2: RevoBank Sales Performance & Customer Segmentation**"):
    st.markdown("**Objective:** To segment existing credit card clients into distinct user personas based on their financial profiles and transaction behaviors to drive higher, more targeted engagement.")
    st.markdown("**Methodology:** Performed data cleaning and feature engineering using **Python (Pandas)** and applied **K-Means Clustering (Scikit-learn)** to segment users based on metrics like transaction recency, frequency, and Debt-to-Income ratio.")
    
    st.markdown("**Identified Customer Segments:**")
    st.success("""
    - **The Engaged Spender:** Highly active, financially healthy, and high-value.
    - **The Latent User:** Inactive but with high income, representing significant untapped potential.
    """)
    st.markdown("[View PDF 📋](https://drive.google.com/file/d/1VDYS6UszIILwdLmW7Uprcayvae9vEqYG/view?usp=sharing)")

# --- Project 3: QuickU ---
with st.expander("🛒 **Project 3: QuickU Demand Forecasting**"):
    st.markdown("**Objective:** To generate an accurate stock demand forecast for August 2022 to minimize expired inventory (waste) and prevent stockouts across QuickU's network of 5 hubs.")
    st.markdown("**Methodology:** Analyzed 7 months of historical data using **Python (Statsmodels)**. Developed **50 unique SARIMA models** to handle seasonality and trend variations across specific product categories and locations.")
    
    st.write("") # Spacer

    # Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Forecast (Aug '22)", value="417,082")
        st.caption("Units predicted across all hubs")
        
    with col2:
        st.metric(label="Model Accuracy (MAPE)", value="21.3%")
        st.caption("Reliable directional accuracy")

    with col3:
        st.metric(label="Top Growth Location", value="Hub E")
        st.caption("Highest projected demand")

    st.write("") # Spacer

    # Visualization: Historical vs Forecast
    st.subheader("H. Sayur & Buah (Hub E): Historical vs. Forecasted Demand")
    st.caption("Showing the demand trajectory with a forecasted peak in August Week 4.")

    # Data Source: User provided specific historical and forecast figures.
    chart_data = pd.DataFrame({
        'Week': [
            # Historical Data (Jan - Jul)
            'Jan 1 (W1)', 'Jan 8 (W2)', 'Jan 15 (W3)', 'Jan 22 (W4)',
            'Feb 1 (W5)', 'Feb 8 (W6)', 'Feb 15 (W7)', 'Feb 22 (W8)',
            'Mar 1 (W9)', 'Mar 8 (W10)', 'Mar 15 (W11)', 'Mar 22 (W12)',
            'Apr 1 (W13)', 'Apr 8 (W14)', 'Apr 15 (W15)', 'Apr 22 (W16)',
            'May 1 (W17)', 'May 8 (W18)', 'May 15 (W19)', 'May 22 (W20)',
            'Jun 1 (W21)', 'Jun 8 (W22)', 'Jun 15 (W23)', 'Jun 22 (W24)',
            'Jul 1 (W25)', 'Jul 8 (W26)', 'Jul 15 (W27)', 'Jul 22 (W28)',
            # Forecast Data (Aug)
            'Aug 5 (W1)', 'Aug 12 (W2)', 'Aug 19 (W3)', 'Aug 26 (W4)'
        ],
        'Demand': [
            # Historical Values
            525, 700, 875, 1400,
            2431, 3241, 4051, 6482,
            4424, 5899, 7373, 11797,
            6547, 8730, 10912, 17460,
            5631, 7508, 9385, 15016,
            5856, 7808, 9760, 15616,
            5505, 7340, 9174, 14679,
            # Forecast Values
            4817, 6836, 8804, 14407
        ],
        'Type': [
            'Historical', 'Historical', 'Historical', 'Historical',
            'Historical', 'Historical', 'Historical', 'Historical',
            'Historical', 'Historical', 'Historical', 'Historical',
            'Historical', 'Historical', 'Historical', 'Historical',
            'Historical', 'Historical', 'Historical', 'Historical',
            'Historical', 'Historical', 'Historical', 'Historical',
            'Historical', 'Historical', 'Historical', 'Historical',
            'Forecast', 'Forecast', 'Forecast', 'Forecast'
        ]
    })

    # Altair Chart distinguishing Historical vs Forecast
    chart = alt.Chart(chart_data).mark_bar().encode(
        x=alt.X('Week', sort=None, title='Week (Jan - Aug 2022)'),
        y=alt.Y('Demand', title='Units Sold'),
        color=alt.Color('Type', scale=alt.Scale(domain=['Historical', 'Forecast'], range=['#4B4453', '#D8A7B1'])),
        tooltip=['Week', 'Demand', 'Type']
    ).properties(
        height=300
    )

    st.altair_chart(chart, use_container_width=True)

    # Link to Full Deck
    st.divider()
    st.markdown("[View Full Presentation Deck 📋](https://drive.google.com/file/d/1LTjc5bXmnOqWQVNxAnfqEbgUOQjqht6N/view?usp=sharing)")

st.divider()


