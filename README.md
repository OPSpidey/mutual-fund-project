# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project analyzes the Indian Mutual Fund industry using historical NAV data, fund performance metrics, SIP inflows, investor behavior, and portfolio analytics. The objective is to build a complete data analytics pipeline and interactive dashboard for investment insights.

## Objectives

* Build ETL pipeline for mutual fund datasets
* Perform Exploratory Data Analysis (EDA)
* Compute risk and performance metrics
* Develop advanced analytics models
* Build Power BI dashboard
* Generate actionable investment insights

## Dataset Description

### 01_fund_master

Fund metadata including AMFI code, category, fund house, benchmark and expense ratio.

### 02_nav_history_clean

Historical NAV records from 2022–2025.

### 03_aum_by_fund_house

Fund house assets under management.

### 04_monthly_sip_inflows

Monthly SIP statistics.

### 05_category_inflows

Category-wise inflow data.

### 06_industry_folio_count

Industry folio counts.

### 07_performance_clean

Fund performance metrics and rankings.

### 08_transactions_clean

Synthetic investor transaction dataset.

## Setup Instructions

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run ETL Pipeline

```bash
python scripts/run_pipeline.py
```

## Run Advanced Analytics

Open:

```text
notebooks/05_advanced_analytics.ipynb
```

and execute all cells.

## Dashboard

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

## Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* Power BI Dashboard
* Advanced Analytics Notebook
* GitHub Repository

## Author

Yaswanth Kumar
IIT (BHU) Varanasi
