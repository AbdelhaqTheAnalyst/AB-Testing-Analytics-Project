import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="A/B Testing Analytics Project", layout="wide")
st.title("📊 Project: Product Growth & A/B Testing Analytics")
st.caption("Developed by: Abdelhaq El Mandouli - Data Analyst")

st.markdown("""
### 🎯 Project Overview
This interactive web application showcases the final results of an **A/B Testing analysis** performed on a large e-commerce dataset (>290,000 visitors). 
The goal of this project is to statistically evaluate whether a newly designed landing page (Treatment) outperforms the old web page (Control) based on conversion rates.
""")

st.markdown("---")

@st.cache_data 
def load_data():
    df = pd.read_csv("cleaned_ab_data.csv")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    return df

df = load_data()

st.subheader("📈 Key Metrics & Conversion Rates")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sample Size (Visitors)", f"{len(df):,}")
col2.metric("Control group (Old Page) CR", "12.04%")
col3.metric("Treatment group (New Page) CR", "11.88%")

st.markdown("---")

st.subheader("🔍 Cleaned Dataset Preview")
st.dataframe(df.head(50), use_container_width=True)

st.markdown("---")

st.subheader("📅 Daily Conversion Rate Trend (Interactive Chart)")

daily_data = df.groupby(['date', 'group'])['converted'].mean().unstack() * 100
daily_data = daily_data.round(2).reset_index()

daily_melted = daily_data.melt(id_vars=["date"], value_vars=["control", "treatment"], 
                               var_name="Group", value_name="Conversion Rate (%)")

fig = px.line(
    daily_melted, 
    x="date", 
    y="Conversion Rate (%)", 
    color="Group",
    color_discrete_map={"control": "#2ecc71", "treatment": "#e74c3c"},
    labels={"date": "Date"}
)

fig.update_traces(mode="lines+markers", hovertemplate="<b>Date:</b> %{x}<br><b>CR:</b> %{y}%")
fig.update_layout(hovermode="x unified", legend_title_text="Groups")

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("💡 Statistical Conclusion & Business Recommendation")
st.info("""
* **Hypothesis Testing Results:** A **Z-test** was conducted, yielding a **P-value of 18.99%** (which is significantly greater than the 5% significance level).
* **Finding:** The slight drop in the new page's conversion rate is statistically proven to be **random noise**, not a permanent change.
* **Business Decision:** We failed to reject the null hypothesis. The final data-driven recommendation is to **stick with the old page** to avoid unnecessary development costs and safeguard existing revenue.
""")


