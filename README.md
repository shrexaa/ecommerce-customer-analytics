# 📊 Omnichannel Retail & Customer Behavior Analytics

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.1.0-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.5.4-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.11.2-11557c.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-3776ab.svg)](https://seaborn.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**An End-to-End Industrial Training Data Analytics Project on E-Commerce Revenue Dynamics, RFM Customer Segmentation, and Churn Risk Modeling.**

[Key Findings](#-key-findings--executive-kpis) •
[Visual Gallery](#-visual-analytics-gallery) •
[RFM Segmentation](#-rfm-customer-segmentation-framework) •
[Installation & Usage](#-installation--reproducibility) •
[Push to GitHub](#-how-to-push-this-project-to-github)

</div>

---

## 📌 Project Overview
This repository contains the complete industrial training capstone project for **Data Analysis and Business Intelligence**. 

In modern retail and e-commerce enterprises, high-volume transactions generate vast datasets that must be translated into actionable commercial strategy. This project models an omnichannel retail enterprise with **6,500 transactions** across **1,811 unique customers** spanning over 2.5 years (2024–2026), evaluating revenue growth, discount elasticity, category profit margins, customer lifetime behavior, and churn probability.

### Core Analytical Objectives:
1. **Data Hygiene & Auditing:** Systematic missing-value imputation, deduplication, and IQR-based financial outlier detection.
2. **Time-Series Sales Dynamics:** Uncovering macro revenue trajectories, holiday seasonality surges (Q4), and rolling moving averages.
3. **Product Margin Economics:** Dissecting high-volume vs high-margin categories and identifying discount-driven margin erosion.
4. **Behavioral Customer Segmentation (RFM):** Classifying 1,800+ customer profiles into actionable cohorts (*Champions, Loyalists, At-Risk, Inactive*).
5. **Retention & Churn Analytics:** Evaluating loyalty membership elasticity and formulating automated retention workflows.

---

## 📈 Key Findings & Executive KPIs

| Metric | Analyzed Value | Business Interpretation |
|:---|:---:|:---|
| **Total Gross Revenue** | **$2,612,179.35** | Cumulative net sales analyzed across 5 core retail sectors |
| **Total Operating Profit** | **$553,115.27** | Net realized operating profit after merchant discounts |
| **Blended Operating Margin** | **21.17%** | Sustainable aggregate margin with wide category variance |
| **Analyzed Customer Base** | **1,811 Customers** | Classified across 8 RFM behavioral cohorts |
| **Average Order Value (AOV)** | **$401.87** | Baseline transaction size across all product lines |
| **At-Risk Recoverable Value** | **$220,000+** | Immediate revenue at stake in lapsed high-value accounts |

---

## 🏗️ Repository Architecture

```text
ecommerce-customer-analytics/
├── .gitignore                                 # Git rules for Python, artifacts, cache
├── requirements.txt                           # Strict dependency manifest
├── README.md                                  # Complete GitHub presentation document
├── run_analysis.py                            # One-click master pipeline execution runner
├── data/
│   ├── raw/
│   │   └── retail_customer_churn_transactions.csv   # Raw transaction logs
│   └── processed/
│       ├── cleaned_transactions.csv                 # Cleaned, imputed & feature-engineered data
│       └── customer_rfm_segments.csv                # Customer-level RFM metrics & segment labels
├── notebooks/
│   └── industrial_training_data_analysis.ipynb      # Complete interactive Jupyter Notebook
├── reports/
│   ├── executive_summary_report.md            # Formal industrial training technical report
│   └── figures/                               # Publication-quality charts (300 DPI)
│       ├── 01_sales_trend_and_seasonality.png
│       ├── 02_category_revenue_and_margins.png
│       ├── 03_rfm_customer_segments_distribution.png
│       ├── 04_discount_vs_profit_bivariate.png
│       ├── 05_correlation_heatmap.png
│       ├── 06_churn_and_retention_by_membership.png
│       └── 07_regional_payment_and_demographics.png
└── src/
    ├── __init__.py
    ├── data_generator.py                      # Realistic enterprise transactional data generator
    ├── data_preprocessing.py                  # Cleaning, type casting, IQR outlier detection, features
    ├── rfm_segmentation.py                    # RFM quantile scoring, segment categorization, churn flags
    └── visualization.py                       # Matplotlib & Seaborn visualization suite
```

---

## 🖼️ Visual Analytics Gallery

### 1. Monthly Revenue Trajectory & Holiday Seasonality
> Demonstrates consistent monthly sales volume with prominent spikes in Q4 (November & December) during Black Friday and Cyber Week promotions. A 3-month rolling moving average highlights underlying growth.
![Sales Trend](reports/figures/01_sales_trend_and_seasonality.png)

---

### 2. Category Revenue Breakdown & Profit Margin Distributions
> **Volume vs. Value:** `Electronics` drives the highest gross revenue (~$850K+), but `Beauty & Wellness` and `Fashion & Apparel` provide significantly superior operating margins (32%–38% vs 18%).
![Category Performance](reports/figures/02_category_revenue_and_margins.png)

---

### 3. RFM Customer Segmentation & Monetary Contribution
> **Pareto Principle in Action:** 478 **Champions** account for over **$1.1M** (42%) of total company revenue. Meanwhile, 178 **At-Risk Customers** represent $220K in high-priority win-back potential.
![RFM Segments](reports/figures/03_rfm_customer_segments_distribution.png)

---

### 4. Bivariate Analysis: Discount Percentage vs Net Profit
> The scatterplot and regression trendline demonstrate that discounts exceeding 20% severely degrade gross margin and push multiple transactions into net negative profit territory.
![Discount vs Profit](reports/figures/04_discount_vs_profit_bivariate.png)

---

### 5. Multivariate Correlation Heatmap (Triangular Mask)
> Correlation analysis between customer age, quantities, unit prices, discounts, delivery times, and ratings. Shows strong negative correlation between delivery delay (>5 days) and customer satisfaction scores.
![Correlation Heatmap](reports/figures/05_correlation_heatmap.png)

---

### 6. Customer Retention vs Churn Rate Across Loyalty Tiers
> Demonstrates the power of customer loyalty programs: **Platinum** members experience only 11.2% churn, whereas **Regular** non-loyalty accounts experience 24.6% churn.
![Retention by Membership](reports/figures/06_churn_and_retention_by_membership.png)

---

### 7. Regional Revenue by Payment Channel & Demographics
> Cross-tabulation of geographical sales channels against preferred payment methods (UPI, Cards, COD), alongside customer age probability densities across membership tiers.
![Regional Analysis](reports/figures/07_regional_payment_and_demographics.png)

---

## 👥 RFM Customer Segmentation Framework

Customers were evaluated using quantile-based Recency, Frequency, and Monetary scores (1 to 4):

| Customer Segment | Criteria (R, F, M) | Profile & Strategy |
|:---|:---:|:---|
| **Champions** | $R \ge 3, F \ge 3, M \ge 3$ | Most valuable patrons. Reward with exclusive VIP perks, early product drops, and ambassador rewards. |
| **Loyal Customers** | $R \ge 2, F \ge 3, M \ge 3$ | Frequent, steady buyers. Cross-sell premium accessories and higher-margin categories. |
| **Potential Loyalists** | $R \ge 3, F \ge 2, M \ge 2$ | Recent buyers with above-average spend. Nudge with tiered loyalty points to increase frequency. |
| **Recent Customers** | $R \ge 3, F \le 2$ | First-time or new buyers. Onboard with seamless customer support and a 2nd-order welcome incentive. |
| **Promising** | $R = 2, F \ge 2$ | Moderately recent repeat buyers. Deliver targeted product recommendations based on past purchase history. |
| **At-Risk Customers** | $R \le 2, (F \ge 3 \text{ or } M \ge 3)$ | **Critical cohort:** Previously spent high amounts, but inactive for >90 days. Target with aggressive win-back campaigns. |
| **Needs Attention** | $R = 2, F \le 2$ | Average recency and spend. Re-engage with limited-time seasonal promotional discounts. |
| **Lost / Inactive** | $R = 1, F \le 2, M \le 2$ | Dormant accounts (>120 days). Maintain minimal spend automated email flows to minimize CAC. |

---

## 💡 Strategic Business Recommendations

1. **Establish Discount Guardrails:** Cap standard promotional discounts at **18%**. Disallow discounting $>22\%$ on consumer electronics where supplier cost margins are thin.
2. **Execute Automated Win-Back Flows:** Trigger automated personalized email/SMS sequences offering a 15% incentive to the 178 *At-Risk Customers* upon passing 90 days of inactivity.
3. **Incentivize Loyalty Upgrades:** Accelerate customer transitions from *Regular* to *Silver/Gold* tier when lifetime spend crosses $\$300$, capturing a 50% reduction in churn probability.
4. **Optimize Logistics SLAs:** Ensure delivery fulfillment within 5 business days to safeguard customer review ratings and reduce product return requests.

---

## 💻 Installation & Reproducibility

### Prerequisites
- Python 3.10+ (Tested on Python 3.13)
- pip package manager

### 1. Clone or Download Repository
```bash
git clone https://github.com/<your-username>/ecommerce-customer-analytics.git
cd ecommerce-customer-analytics
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

### 3. Run the Complete Analysis Pipeline
Execute the master runner to generate datasets, perform data cleaning, compute RFM metrics, and render all 7 figures in seconds:
```bash
python run_analysis.py
```

### 4. Explore the Interactive Jupyter Notebook
```bash
jupyter notebook notebooks/industrial_training_data_analysis.ipynb
```

---

## 🚀 How to Push This Project to GitHub

Follow these simple steps to put this project on your personal GitHub profile:

### Option A: Using the Command Line (Git CLI)
```bash
# 1. Navigate to the project directory
cd "C:\Users\shrey\.gemini\antigravity\scratch\ecommerce-customer-analytics"

# 2. Initialize git repository
git init

# 3. Add all files and make initial commit
git add .
git commit -m "feat: complete industrial training data analysis project with pandas, numpy, seaborn, matplotlib"

# 4. Create a new repository on GitHub (named 'ecommerce-customer-analytics')
# Then link your remote and push:
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/ecommerce-customer-analytics.git
git push -u origin main
```

### Option B: Using GitHub Web Interface (No Command Line Needed)
1. Go to [GitHub.com](https://github.com) and click **New Repository**.
2. Name it `ecommerce-customer-analytics` (keep it **Public**), and do not initialize with a README (as we already have a full README).
3. Click **Upload an existing file**.
4. Drag and drop the files/folders from `C:\Users\shrey\.gemini\antigravity\scratch\ecommerce-customer-analytics`.
5. Enter commit message `Initial commit: Data Analysis Industrial Training Project` and click **Commit changes**.

---

## 📜 License
This project is licensed under the [MIT License](LICENSE) - feel free to use, adapt, and showcase this project for academic and professional portfolio purposes.

## 👤 Author
- **Industrial Training Capstone Project**  
- **Domain:** Data Analytics, Business Intelligence & Customer Lifetime Economics
- **Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn
