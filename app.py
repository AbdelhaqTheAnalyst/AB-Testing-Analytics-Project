import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="A/B Testing Analytics", layout="wide")
st.title("Product Growth A/B Testing")
st.caption("Developed b:Abdelhaq El Mandouli - Data Analyst")

st.markdown("""
### 🎯 Project Overview
This interactive web application showcase the final results of an **A/B Testing Analysis** performed on large e-commercedataset (>290k visitors).
The goal of this project is to statistically evaluate whether a new web page (Treatment) outperforms the old web page (Cotrol) based on conversion rates.
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


st.subheader("📅 Daily Conversion Rate Trend (Time-Series Analysis)")


daily_data = df.groupby(['date', 'group'])['converted'].mean().unstack() * 100


fig, ax = plt.subplots(figsize=(12, 4.5))
sns.lineplot(data=daily_data, marker='o', ax=ax)
ax.set_title("Daily CR: Control vs Treatment", fontsize=12)
ax.set_ylabel("Conversion Rate (%)")
ax.set_xlabel("Date")
ax.grid(True, linestyle='--', alpha=0.5)


st.pyplot(fig)


st.markdown("---")
st.subheader("💡 Statistical Conclusion & Business Recommendation")
st.info("""
* **Hypothesis Testing Results:** A **Z-test** was conducted, yielding a **P-value of 18.99%** (which is significantly greater than the 5% significance level).
* **Finding:** The slight drop in the new page's conversion rate is statistically proven to be **random noise**, not a permanent change.
* **Business Decision:** We failed to reject the null hypothesis. The final data-driven recommendation is to **stick with the old page** to avoid unnecessary development costs and safeguard existing revenue.
""")

