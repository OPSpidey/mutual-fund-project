# Data Dictionary

## 01_fund_master.csv

Source: Fund Master Dataset

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | String | Asset Management Company (AMC) |
| scheme_name | String | Mutual fund scheme name |
| category | String | Fund category (Equity/Debt) |
| sub_category | String | Fund sub-category |
| plan | String | Direct or Regular plan |
| launch_date | Date | Scheme launch date |
| benchmark | String | Benchmark index |
| expense_ratio_pct | Float | Expense ratio percentage |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP investment amount |
| min_lumpsum_amount | Integer | Minimum lump sum investment |
| fund_manager | String | Fund manager name |
| risk_category | String | Risk classification |
| sebi_category_code | String | SEBI category code |

---

## 02_nav_history.csv

Source: Historical NAV Data

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | Scheme code |
| date | Date | NAV reporting date |
| nav | Float | Net Asset Value |

---

## 03_aum_by_fund_house.csv

Source: AUM Statistics

| Column | Data Type | Description |
|----------|----------|-------------|
| date | Date | Reporting date |
| fund_house | String | AMC name |
| aum_lakh_crore | Float | Assets under management (lakh crore) |
| aum_crore | Integer | Assets under management (crore) |
| num_schemes | Integer | Number of schemes managed |

---

## 04_monthly_sip_inflows.csv

Source: SIP Industry Data

| Column | Data Type | Description |
|----------|----------|-------------|
| month | Date | Reporting month |
| sip_inflow_crore | Integer | Monthly SIP inflow amount |
| active_sip_accounts_crore | Float | Active SIP accounts |
| new_sip_accounts_lakh | Float | New SIP accounts added |
| sip_aum_lakh_crore | Float | SIP assets under management |
| yoy_growth_pct | Float | Year-over-year growth percentage |

---

## 05_category_inflows.csv

Source: Category-wise Fund Flows

| Column | Data Type | Description |
|----------|----------|-------------|
| month | Date | Reporting month |
| category | String | Fund category |
| net_inflow_crore | Float | Net inflow amount |

---

## 06_industry_folio_count.csv

Source: Industry Folio Statistics

| Column | Data Type | Description |
|----------|----------|-------------|
| month | Date | Reporting month |
| total_folios_crore | Float | Total folios |
| equity_folios_crore | Float | Equity folios |
| debt_folios_crore | Float | Debt folios |
| hybrid_folios_crore | Float | Hybrid folios |
| others_folios_crore | Float | Other category folios |

---

## 07_scheme_performance.csv

Source: Scheme Performance Metrics

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | Scheme code |
| scheme_name | String | Scheme name |
| fund_house | String | AMC name |
| category | String | Fund category |
| plan | String | Plan type |
| return_1yr_pct | Float | One-year return (%) |
| return_3yr_pct | Float | Three-year return (%) |
| return_5yr_pct | Float | Five-year return (%) |
| benchmark_3yr_pct | Float | Benchmark return (%) |
| alpha | Float | Alpha measure |
| beta | Float | Beta measure |
| sharpe_ratio | Float | Sharpe ratio |
| sortino_ratio | Float | Sortino ratio |
| std_dev_ann_pct | Float | Annualized standard deviation |
| max_drawdown_pct | Float | Maximum drawdown (%) |
| aum_crore | Integer | Assets under management |
| expense_ratio_pct | Float | Expense ratio (%) |
| morningstar_rating | Integer | Morningstar rating |
| risk_grade | String | Risk grade |

---

## 08_investor_transactions.csv

Source: Investor Transaction Records

| Column | Data Type | Description |
|----------|----------|-------------|
| investor_id | String | Unique investor identifier |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Scheme code |
| transaction_type | String | SIP, Lumpsum, or Redemption |
| amount_inr | Integer | Transaction amount |
| state | String | Investor state |
| city | String | Investor city |
| city_tier | String | Tier classification |
| age_group | String | Investor age bracket |
| gender | String | Investor gender |
| annual_income_lakh | Float | Annual income in lakhs |
| payment_mode | String | Payment method |
| kyc_status | String | KYC verification status |

---

## 09_portfolio_holdings.csv

Source: Portfolio Holdings Data

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | Scheme code |
| stock_symbol | String | Stock ticker symbol |
| stock_name | String | Company name |
| sector | String | Industry sector |
| weight_pct | Float | Portfolio allocation percentage |
| market_value_cr | Float | Market value in crore |
| current_price_inr | Float | Current stock price |
| portfolio_date | Date | Portfolio reporting date |

---

## 10_benchmark_indices.csv

Source: Benchmark Index History

| Column | Data Type | Description |
|----------|----------|-------------|
| date | Date | Trading date |
| index_name | String | Benchmark index name |
| close_value | Float | Index closing value |

---

# Business Definitions

| Term | Definition |
|--------|------------|
| NAV | Net Asset Value of a mutual fund unit |
| AUM | Assets Under Management |
| SIP | Systematic Investment Plan |
| Expense Ratio | Annual fund operating expenses as a percentage of AUM |
| Alpha | Excess return over benchmark |
| Beta | Sensitivity of fund returns relative to market |
| Sharpe Ratio | Risk-adjusted return metric |
| Sortino Ratio | Downside-risk-adjusted return metric |
| AMFI Code | Unique identifier assigned to a mutual fund scheme |
| Benchmark Index | Reference market index used for performance comparison |