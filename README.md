# 📊 Product Growth & A/B Testing Analytics Project

## 🎯 Project Overview
This project delivers a data-driven statistical analysis of an A/B testing campaign conducted on a large e-commerce dataset (>290,000 visitors). The primary objective is to evaluate whether a newly designed landing page (Treatment group) leads to a statistically significant increase in conversion rates compared to the existing page (Control group).

## 🚀 Live Interactive Web App
👉 **[Click Here to View the Live Streamlit Dashboard](تترك_فارغة_حالياً_سنضع_الرابط_هنا_لاحقاً)**

---

## 🛠️ Key Project Phases & Technical Implementation

### 1. Data Cleaning & Optimization (`Pandas`)
* Verified a dataset of **290,584 rows** with zero missing values (Nulls = 0).
* Handled and removed data inconsistencies (e.g., users exposed to the wrong page version relative to their assigned group).
* Dropped duplicate entries to ensure strict statistical validity.

### 2. Hypothesis Testing & Statistical Analytics (`SciPy`)
* **Control Group (Old Page) Conversion Rate:** 12.04%
* **Treatment Group (New Page) Conversion Rate:** 11.88%
* Executed a two-tailed **Z-test** to calculate the **Z-score** and **P-value**.
* **Statistical Finding:** The **P-value resulted in 18.99%** (significantly higher than the 5% alpha level), proving that the slight drop in the new page is purely due to random noise.
* **Business Decision:** Failed to reject the Null Hypothesis. Officially recommended sticking with the old page to protect company revenue and avoid unnecessary deployment costs.

### 3. Time-Series & Interactive Visualization (`Matplotlib` & `Seaborn`)
* Performed daily aggregate analysis using modern data manipulation tools like `.groupby()` and `.unstack()`.
* Engineered a clean, dual-line visualization to monitor the stability and fluctuations of both conversion rates day by day.
* Built a lightweight interactive dashboard using **Streamlit** to present these dynamic charts and key performance indicators (KPIs) seamlessly.

---

## 📂 Project Structure
```text
├── venv/                       # Isolated virtual environment
├── cleaned_ab_data.csv         # Cleaned and processed dataset
├── app.py                      # Streamlit application source code
└── README.md                   # Project documentation (This file)
```

## 🧑‍💻 Author
**Abdelhaq El Mandouli**  
*Data Analyst*  
[LinkedIn Profile]: (https://www.linkedin.com/in/abdelhaq-el-mandouli-739b45424/)
