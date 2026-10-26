import sqlite3
import pandas as pd
import re
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import matplotlib.ticker as ticker
import seaborn as sns
import time
import os

print("=== STARTING FULL RECONCILIATION PIPELINE ===")
start_total_time = time.time()

# -------------------------------------------------------------
# PHASE 1: SQL EXTRACTION
# -------------------------------------------------------------
phase1_start = time.time()
conn = sqlite3.connect('enterprise_database.db')

sql_query = """
WITH RankedUsers AS (
    SELECT 
        user_id, 
        name, 
        status, 
        updated_at,
        ROW_NUMBER() OVER (
            PARTITION BY user_id 
            ORDER BY updated_at DESC
        ) AS row_num
    FROM users
)
SELECT 
    user_id, 
    name, 
    status, 
    updated_at
FROM RankedUsers
WHERE row_num = 1 
  AND status = 'Active';
"""

df_active_users = pd.read_sql_query(sql_query, conn)
conn.close()

phase1_duration = time.time() - phase1_start
print(f"Phase 1 completed in: {phase1_duration:.4f} seconds")
print(f"Total Active Users extracted: {len(df_active_users):,}")
print(df_active_users.head())

# -------------------------------------------------------------
# PHASE 2: REGEX & UNSTRUCTURED DATA WRANGLING
# -------------------------------------------------------------
phase2_start = time.time()
df_raw_logs = pd.read_csv('server_logs.txt')
total_raw_rows = len(df_raw_logs)

log_col = df_raw_logs.columns[0]
df_clean_logs = df_raw_logs[~df_raw_logs[log_col].str.contains("ERROR", regex=False, na=False)].copy()
error_rows_dropped = total_raw_rows - len(df_clean_logs)
print(f"Phase 2: Dropped {error_rows_dropped:,} error records. Clean logs: {len(df_clean_logs):,}")

regex_pattern = r'\[(\d{4}-\d{2}-\d{2}).*?\].*?"u":"?([A-Za-z0-9_-]+)"?.*?"item_code":"?([A-Za-z0-9_-]+)"?.*?"eur_val":\s*([0-9.]+)'

extracted_data = df_clean_logs[log_col].str.extract(regex_pattern)
extracted_data.columns = ['Date', 'user_id', 'product_id', 'eur_val']
extracted_data['eur_val'] = pd.to_numeric(extracted_data['eur_val'])

phase2_duration = time.time() - phase2_start
print(f"Phase 2 completed in: {phase2_duration:.4f} seconds")
print(extracted_data.head())

# -------------------------------------------------------------
# PHASE 3: FINANCIAL RECONCILIATION & MERGING
# -------------------------------------------------------------
phase3_start = time.time()
df_exchange_rates = pd.read_csv('daily_exchange_rates.csv')
print(f"Missing exchange rates before forward-fill: {df_exchange_rates['EUR_to_USD'].isnull().sum()}")

df_exchange_rates['Date'] = pd.to_datetime(df_exchange_rates['Date'])
df_exchange_rates = df_exchange_rates.sort_values('Date').reset_index(drop=True)
df_exchange_rates['EUR_to_USD'] = df_exchange_rates['EUR_to_USD'].ffill()
df_exchange_rates['Date'] = df_exchange_rates['Date'].dt.strftime('%Y-%m-%d')
print(f"Missing exchange rates after forward-fill: {df_exchange_rates['EUR_to_USD'].isnull().sum()}")

# Merge logs with rates
df_reconciled = pd.merge(extracted_data, df_exchange_rates, on='Date', how='inner')

# Merge with active users
df_final = pd.merge(df_reconciled, df_active_users, on='user_id', how='inner')

# Calculate USD_Revenue
df_final['USD_Revenue'] = df_final['eur_val'] * df_final['EUR_to_USD']

phase3_duration = time.time() - phase3_start
print(f"Phase 3 completed in: {phase3_duration:.4f} seconds")
print(f"Total Reconciled USD Revenue: ${df_final['USD_Revenue'].sum():,.2f}")
print(df_final.head())

# -------------------------------------------------------------
# PHASE 4: AGGREGATION & VISUALIZATION (CFO DASHBOARD)
# -------------------------------------------------------------
phase4_start = time.time()
df_final['Month'] = pd.to_datetime(df_final['Date']).dt.to_period('M').astype(str)
monthly_revenue = df_final.groupby('Month')['USD_Revenue'].sum().reset_index()

customer_revenue = df_final.groupby(['user_id', 'name'])['USD_Revenue'].sum().reset_index()
top_5_customers = customer_revenue.sort_values(by='USD_Revenue', ascending=False).head(5).reset_index(drop=True)

print("\n=== Monthly Revenue Summary ===")
for _, row in monthly_revenue.iterrows():
    print(f"Month: {row['Month']} -> USD Revenue: ${row['USD_Revenue']:,.2f}")

print("\n=== Top 5 Most Valuable Customers ===")
for i, row in top_5_customers.iterrows():
    print(f"{i+1}. {row['name']} ({row['user_id']}) -> USD Revenue: ${row['USD_Revenue']:,.2f}")

# Chart generation
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(18, 6), dpi=100)
fig.suptitle('GlobalTech FinTech Solutions - Q1-Q4 Financial Audit Dashboard', fontsize=18, fontweight='bold', y=1.02)

# Chart 1: Revenue Trends Over Time
ax1 = axes[0]
sns.lineplot(
    data=monthly_revenue, 
    x='Month', 
    y='USD_Revenue', 
    marker='o', 
    markersize=8, 
    linewidth=2.5, 
    color='#1f77b4', 
    ax=ax1
)
ax1.set_title('Monthly Revenue Trend in USD (2023)', fontsize=14, fontweight='bold', pad=12)
ax1.set_xlabel('Month', fontsize=12, fontweight='bold')
ax1.set_ylabel('Total Revenue ($ USD)', fontsize=12, fontweight='bold')
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"${x*1e-6:.1f}M"))
ax1.tick_params(axis='x', rotation=45)
ax1.fill_between(monthly_revenue['Month'], monthly_revenue['USD_Revenue'], color='#1f77b4', alpha=0.15)
for _, row in monthly_revenue.iterrows():
    ax1.annotate(f"${row['USD_Revenue']*1e-6:.2f}M", 
                 (row['Month'], row['USD_Revenue']),
                 textcoords="offset points", xytext=(0, 8), ha='center', fontsize=8, fontweight='semibold')

# Chart 2: Top 5 Customers
ax2 = axes[1]
palette = sns.color_palette("mako", n_colors=5)
sns.barplot(
    data=top_5_customers, 
    x='USD_Revenue', 
    y='name', 
    palette=palette, 
    ax=ax2
)
ax2.set_title('Top 5 Most Valuable Customers (USD)', fontsize=14, fontweight='bold', pad=12)
ax2.set_xlabel('Total Spend ($ USD)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Customer Name', fontsize=12, fontweight='bold')
ax2.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"${x:,.0f}"))
for i, row in top_5_customers.iterrows():
    ax2.text(row['USD_Revenue'] * 0.98, i, f" ${row['USD_Revenue']:,.2f}", 
             ha='right', va='center', color='white', fontweight='bold', fontsize=10)

plt.tight_layout()
chart_path = 'cfo_dashboard_charts.png'
plt.savefig(chart_path, bbox_inches='tight', dpi=300)
plt.close()

# -------------------------------------------------------------
# PHASE 5: BI HANDOFF
# -------------------------------------------------------------
output_csv_filename = 'power_bi_ready_dataset.csv'
df_final.to_csv(output_csv_filename, index=False)

total_elapsed = time.time() - start_total_time
print(f"\n[SUCCESS] Pipeline executed in: {total_elapsed:.2f} seconds!")
print(f"[SAVED] Chart saved as '{chart_path}'")
print(f"[EXPORT] CSV exported as '{output_csv_filename}' with {len(df_final):,} rows.")
