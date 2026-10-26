import pandas as pd
import json

df = pd.read_csv('power_bi_ready_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M').astype(str)
df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)

# Monthly metrics
monthly = df.groupby('Month').agg(
    revenue=('USD_Revenue', 'sum'),
    transactions=('USD_Revenue', 'count'),
    active_users=('user_id', 'nunique'),
    avg_order=('USD_Revenue', 'mean')
).reset_index().to_dict(orient='records')

# Quarterly metrics
quarterly = df.groupby('Quarter').agg(
    revenue=('USD_Revenue', 'sum'),
    transactions=('USD_Revenue', 'count'),
    active_users=('user_id', 'nunique'),
    avg_order=('USD_Revenue', 'mean')
).reset_index().to_dict(orient='records')

# Top 5 customers overall
top5_overall = df.groupby(['user_id', 'name'])['USD_Revenue'].sum().reset_index()
top5_overall = top5_overall.sort_values(by='USD_Revenue', ascending=False).head(5).to_dict(orient='records')

# Top customers by quarter
top5_by_q = {}
for q in ['Q1', 'Q2', 'Q3', 'Q4']:
    df_q = df[df['Quarter'] == q]
    top_q = df_q.groupby(['user_id', 'name'])['USD_Revenue'].sum().reset_index()
    top5_by_q[q] = top_q.sort_values(by='USD_Revenue', ascending=False).head(5).to_dict(orient='records')

# Sample 50 transactions
sample_transactions = df[['Date', 'user_id', 'name', 'product_id', 'eur_val', 'EUR_to_USD', 'USD_Revenue']].head(50).copy()
sample_transactions['Date'] = sample_transactions['Date'].dt.strftime('%Y-%m-%d')
sample_records = sample_transactions.to_dict(orient='records')

overall_metrics = {
    'total_revenue': float(df['USD_Revenue'].sum()),
    'total_transactions': int(len(df)),
    'unique_active_users': int(df['user_id'].nunique()),
    'avg_transaction_val': float(df['USD_Revenue'].mean()),
    'min_date': df['Date'].min().strftime('%Y-%m-%d'),
    'max_date': df['Date'].max().strftime('%Y-%m-%d'),
    'monthly': monthly,
    'quarterly': quarterly,
    'top5_overall': top5_overall,
    'top5_by_q': top5_by_q,
    'sample_records': sample_records
}

with open('dashboard_data.json', 'w', encoding='utf-8') as f:
    json.dump(overall_metrics, f, indent=2)

print("Dashboard data JSON generated successfully!")
