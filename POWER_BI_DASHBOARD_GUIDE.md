# GlobalTech FinTech Solutions | Power BI Dashboard & Audit Guide
**Project:** Enterprise Data Reconciliation & Business Intelligence Capstone  
**Audience:** Chief Financial Officer (CFO) & Board of Directors  
**Dataset:** `power_bi_ready_dataset.csv` (53,899 reconciled records)  

---

## 1. Executive Summary

Following GlobalTech's acquisition of European competitor **EuroSystems**, transaction data, user records, and currency exchange rates were siloed across three disparate legacy systems with structural inconsistencies. 

By engineering a vectorized, production-grade Python ETL pipeline, the data was successfully extracted, wrangled, currency-standardized into USD, and merged into a single audit-ready dataset: [`power_bi_ready_dataset.csv`](file:///c:/Users/VINEESHA/OneDrive/Desktop/MINI%20PROJECTS/power_bi_ready_dataset.csv).

### Core Audit Key Performance Indicators (KPIs)
* **Total Reconciled USD Revenue:** **$148,274,622.91**
* **Total Clean Transactions:** **53,899**
* **Active Reconciled Customers:** **14,183**
* **Average Transaction Value:** **$2,750.97**
* **Pipeline Execution SLA:** **< 1.0 second** (Target SLA: < 120 seconds)

---

## 2. Technical Traps Overcome in Pipeline

| Trap | Challenge | Technical Solution | Result |
| :--- | :--- | :--- | :--- |
| **1. Scale & Optimization** | 100,000 raw server logs causing `for` / `iterrows()` timeout | Vectorized Pandas operations & C-optimized batch regex extraction | Completed in **0.25 seconds** |
| **2. Unstructured Data** | Transaction payloads buried in strings; corrupted system errors | Custom regex pattern `\[(\d{4}-\d{2}-\d{2}).*?\].*?"u":"?([A-Za-z0-9_-]+)"?.*?"item_code":"?([A-Za-z0-9_-]+)"?.*?"eur_val":\s*([0-9.]+)` | Dropped **5,098 ERRORs**, parsed **94,902** clean records with **0 nulls** |
| **3. Temporal Reconciliation** | FX market closed on weekends; 104 missing weekend rates | Chronological sorting followed by forward-fill (`.ffill()`) | Rolled Friday rate into Saturday & Sunday; **100% weekend logs preserved** |
| **4. Version Control (SQL)** | Historical log with 47,464 updates for 25,000 users | SQL Window Function `ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY updated_at DESC)` | Isolated latest state; filtered **14,183 Active users** |

---

## 3. Power BI Implementation Guide

Follow these exact steps to load the dataset and build the interactive CFO Dashboard in **Power BI Desktop**:

### Step 1: Ingest Data
1. Launch **Power BI Desktop**.
2. Click **Get Data** > **Text/CSV**.
3. Browse and select [`power_bi_ready_dataset.csv`](file:///c:/Users/VINEESHA/OneDrive/Desktop/MINI%20PROJECTS/power_bi_ready_dataset.csv).
4. Click **Transform Data** to inspect data types in Power Query, then click **Close & Apply**.

### Step 2: Validate Data Types
Ensure columns are set to the correct data types in the **Data** pane:
* `Date` → **Date** (`YYYY-MM-DD`)
* `user_id` → **Text**
* `name` → **Text**
* `product_id` → **Text**
* `eur_val` → **Decimal Number** (Format: Currency `€`)
* `EUR_to_USD` → **Decimal Number** (Format: Decimal `0.0000`)
* `USD_Revenue` → **Decimal Number** (Format: Currency `$`)
* `status` → **Text**
* `updated_at` → **Date/Time**

---

### Step 3: DAX Measures

In Power BI, click **New Measure** on the **Modeling** or **Home** tab and enter the following DAX calculations:

#### 1. Total USD Revenue (Required Deliverable)
```dax
Total USD Revenue = 
SUM(power_bi_ready_dataset[USD_Revenue])
```
*Format: Currency ($), 2 decimal places.*

#### 2. Supporting KPI Measures
```dax
Total Verified Transactions = 
COUNTROWS(power_bi_ready_dataset)
```
*Format: Whole number with comma separators.*

```dax
Active Reconciled Customers = 
DISTINCTCOUNT(power_bi_ready_dataset[user_id])
```
*Format: Whole number with comma separators.*

```dax
Average Transaction Value = 
DIVIDE([Total USD Revenue], [Total Verified Transactions], 0)
```
*Format: Currency ($), 2 decimal places.*

---

### Step 4: Build Required Dashboard Visuals

#### Visual 1: Date Slicer (Month / Quarter Filter)
1. Add a **Slicer** visual from the Visualizations pane.
2. Drag `Date` into the **Field** well.
3. In **Format visual** > **Slicer settings**:
   * Style: **Between** (slider) or **Dropdown** / **Tile**.
   * Turn ON **Date Hierarchy** if you wish to filter by **Quarter** or **Month**.

#### Visual 2: Line Chart (Revenue Trends Over Time)
1. Add a **Line Chart** visual.
2. Configure fields:
   * **X-axis:** `Date` (Hierarchy: Select **Month** or **Date**).
   * **Y-axis:** `[Total USD Revenue]`.
3. In **Format visual**:
   * **Lines:** Color: `#0284C7` (Corporate Blue), Stroke width: 3 px.
   * **Data Labels:** Turn **ON**. Display units: **Millions ($M)**.
   * **Title:** `"Monthly Revenue Trend in USD (2023)"`.

#### Visual 3: Bar Chart (Top 5 Customers by Revenue)
1. Add a **Clustered Bar Chart** visual.
2. Configure fields:
   * **Y-axis:** `name` (Customer Name).
   * **X-axis:** `[Total USD Revenue]`.
3. Filter for Top 5:
   * Open the **Filters** pane.
   * Under **Filters on this visual**, click on `name`.
   * Change Filter Type from *Basic filtering* to **Top N**.
   * Show items: **Top 5**.
   * By value: Drag and drop `[Total USD Revenue]` into the field.
   * Click **Apply filter**.
4. In **Format visual**:
   * **Bars:** Color: `#10B981` (Emerald) or gradient.
   * **Data Labels:** Turn **ON**. Display units: **Thousands ($K)**.
   * **Title:** `"Top 5 Customers by Revenue (USD)"`.

#### Visual 4: Executive KPI Cards
Add four **Card** visuals across the top of the canvas:
* **Card 1:** `[Total USD Revenue]` → Title: `"Total Reconciled Revenue"`.
* **Card 2:** `[Total Verified Transactions]` → Title: `"Verified Transactions"`.
* **Card 3:** `[Active Reconciled Customers]` → Title: `"Active Customers"`.
* **Card 4:** `[Average Transaction Value]` → Title: `"Average Order Value"`.

---

## 4. Reconciled Financial Metrics Reference

### Monthly Revenue Breakdown (2023)
| Month | Clean Transactions | Active Users | Monthly USD Revenue | % of Total |
| :--- | :---: | :---: | :---: | :---: |
| **2023-01** | 4,675 | 3,892 | $12,841,761.38 | 8.66% |
| **2023-02** | 4,149 | 3,554 | $11,436,130.90 | 7.71% |
| **2023-03** | 4,539 | 3,825 | $12,348,931.84 | 8.33% |
| **2023-04** | 4,374 | 3,712 | $12,015,376.19 | 8.10% |
| **2023-05** | 4,557 | 3,858 | $12,333,644.45 | 8.32% |
| **2023-06** | 4,345 | 3,695 | $12,084,355.82 | 8.15% |
| **2023-07** | 4,535 | 3,812 | $12,444,163.58 | 8.39% |
| **2023-08** | 4,611 | 3,874 | $12,812,730.66 | 8.64% |
| **2023-09** | 4,453 | 3,782 | $12,228,952.05 | 8.25% |
| **2023-10** | 4,635 | 3,896 | $12,501,330.36 | 8.43% |
| **2023-11** | 4,464 | 3,803 | $12,588,223.09 | 8.49% |
| **2023-12** | 4,562 | 3,865 | $12,639,022.60 | 8.52% |
| **Total** | **53,899** | **14,183** | **$148,274,622.91** | **100.00%** |

### Top 5 Most Valuable Customers
| Rank | User ID | Customer Name | Total Spend (USD) | Transaction Count |
| :---: | :--- | :--- | :---: | :---: |
| **1** | `U-06582` | `User_U-06582` | **$40,050.99** | 13 |
| **2** | `U-23313` | `User_U-23313` | **$39,555.81** | 13 |
| **3** | `U-03805` | `User_U-03805` | **$39,529.95** | 14 |
| **4** | `U-20018` | `User_U-20018` | **$38,649.97** | 13 |
| **5** | `U-06489` | `User_U-06489` | **$38,629.14** | 13 |

---

## 5. Deliverables Checklist

- [x] **Jupyter Notebook:** [`Student_work_file.ipynb`](file:///c:/Users/VINEESHA/OneDrive/Desktop/MINI%20PROJECTS/Student_work_file.ipynb) fully executed with all markdown notes, code comments, output prints, and embedded charts.
- [x] **Production Python Pipeline:** [`run_pipeline.py`](file:///c:/Users/VINEESHA/OneDrive/Desktop/MINI%20PROJECTS/run_pipeline.py) standalone script that executes in under 1 second.
- [x] **Reconciled Clean CSV Dataset:** [`power_bi_ready_dataset.csv`](file:///c:/Users/VINEESHA/OneDrive/Desktop/MINI%20PROJECTS/power_bi_ready_dataset.csv) ready for instant Power BI import.
- [x] **High-Resolution Visuals:** [`cfo_dashboard_charts.png`](file:///c:/Users/VINEESHA/OneDrive/Desktop/MINI%20PROJECTS/cfo_dashboard_charts.png) exported at 300 DPI.
- [x] **Interactive CFO Web Dashboard:** [`cfo_interactive_dashboard.html`](file:///c:/Users/VINEESHA/OneDrive/Desktop/MINI%20PROJECTS/cfo_interactive_dashboard.html) with real-time date slicers, dynamic KPIs, and SVG charts.
- [x] **Power BI Implementation Guide:** [`POWER_BI_DASHBOARD_GUIDE.md`](file:///c:/Users/VINEESHA/OneDrive/Desktop/MINI%20PROJECTS/POWER_BI_DASHBOARD_GUIDE.md) complete with DAX measures and layout steps.
