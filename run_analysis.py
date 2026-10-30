"""
Master Pipeline Runner
----------------------
Executes the end-to-end data analysis workflow:
1. Synthetic Enterprise Transaction Generation
2. Data Preprocessing, Cleaning & Feature Engineering
3. Customer RFM Segmentation & Churn Profiling
4. Publication-Ready Figure Generation with Matplotlib & Seaborn
5. Console Executive Summary Generation
"""

import os
import sys
import time

# Ensure src modules are resolvable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_generator import generate_retail_dataset
from src.data_preprocessing import inspect_and_clean_data
from src.rfm_segmentation import calculate_rfm_metrics
from src.visualization import generate_all_visualizations

def run_pipeline():
    start_time = time.time()
    print("=" * 80)
    print("   OMNICHANNEL RETAIL & CUSTOMER ANALYTICS PLATFORM")
    print("   Industrial Training Project | Python Data Analysis Pipeline")
    print("=" * 80)

    raw_path = "data/raw/retail_customer_churn_transactions.csv"
    clean_path = "data/processed/cleaned_transactions.csv"
    rfm_path = "data/processed/customer_rfm_segments.csv"
    fig_dir = "reports/figures"

    # Step 1: Synthesize Raw Dataset
    print("\n[STEP 1/4] Synthesizing raw enterprise transactional dataset...")
    df_raw = generate_retail_dataset(n_records=6500, random_seed=42)
    os.makedirs("data/raw", exist_ok=True)
    df_raw.to_csv(raw_path, index=False)
    print(f"-> Generated {len(df_raw)} raw records saved to '{raw_path}'")

    # Step 2: Data Preprocessing & Cleaning
    print("\n[STEP 2/4] Executing data cleaning, imputation, and feature engineering...")
    df_clean, audit = inspect_and_clean_data(raw_path)
    os.makedirs("data/processed", exist_ok=True)
    df_clean.to_csv(clean_path, index=False)
    print(f"-> Cleaned dataset saved to '{clean_path}'")

    # Step 3: Customer RFM Segmentation
    print("\n[STEP 3/4] Performing RFM customer segmentation and churn classification...")
    rfm_df = calculate_rfm_metrics(df_clean)
    rfm_df.to_csv(rfm_path, index=False)
    print(f"-> Customer segments saved to '{rfm_path}'")

    # Step 4: Visualizations
    print("\n[STEP 4/4] Rendering 7 publication-quality Seaborn and Matplotlib figures...")
    generate_all_visualizations(clean_path, rfm_path, fig_dir)

    # Executive Output Summary
    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print("   EXECUTIVE ANALYTICS SUMMARY")
    print("=" * 80)
    print(f" Total Transactions Processed: {audit['clean_rows']:,}")
    print(f" Unique Customers Analyzed:    {len(rfm_df):,}")
    print(f" Total Gross Revenue:          ${audit['total_revenue']:,.2f}")
    print(f" Total Net Profit:             ${audit['total_profit']:,.2f}")
    print(f" Overall Profit Margin:        {(audit['total_profit'] / audit['total_revenue'] * 100):.2f}%")
    print(f" Total Outlier Transactions:   {audit['outlier_transactions']} (detected via IQR)")
    print(f" Pipeline Execution Time:      {elapsed:.2f} seconds")
    print("=" * 80)
    print("Project run finished successfully! All figures saved in 'reports/figures/'.\n")

if __name__ == "__main__":
    run_pipeline()
