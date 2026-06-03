CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER
);

CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date_id INTEGER,
    nav REAL
);

CREATE TABLE fact_transactions (
    amfi_code INTEGER,
    date_id INTEGER,
    amount_inr REAL
);

CREATE TABLE fact_performance (
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL
);

CREATE TABLE fact_aum (
    fund_house TEXT,
    aum_crore REAL,
    date_id INTEGER
);