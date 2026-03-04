# Retail Sales Data Warehouse

End-to-end **Data Engineering project** that builds a retail analytics data warehouse using **PostgreSQL, Python ETL, SQL transformations, and a Streamlit dashboard**.

This project demonstrates how raw transactional data can be transformed into a structured **star schema** and visualized for business insights.

---

# Project Overview

Retail companies generate large volumes of transactional data such as:

- Customer purchases
- Product information
- Store locations
- Sales transactions

This project simulates a **modern analytics pipeline** that converts raw CSV data into a structured **Data Warehouse** for reporting and dashboarding.

The system performs:

1. Raw data ingestion
2. ETL processing
3. Data modeling using **Star Schema**
4. Fact and dimension table creation
5. Data validation
6. Visualization with Streamlit

---

# Architecture


Raw CSV Files
|
▼
Python ETL Pipeline
|
▼
PostgreSQL Staging Tables
|
▼
Dimension Tables
|
▼
Fact Table
|
▼
Analytics Queries
|
▼
Streamlit Dashboard


---

# Data Pipeline Architecture

### 1 Raw Data
Source CSV files:


data/raw/
customers.csv
products.csv
stores.csv
sales.csv


These files represent operational data exported from transactional systems.

---

### 2 Staging Layer

Raw data is first loaded into **staging tables** inside PostgreSQL.

Purpose of staging layer:

- Preserve raw data
- Perform cleaning
- Handle transformations
- Prepare data for warehouse loading

SQL file:


sql/01_create_staging.sql


Example tables:


stg_customers
stg_products
stg_sales
stg_stores


---

### 3 Data Warehouse Layer

The warehouse follows a **Star Schema** design.

Star schema consists of:

- **Fact Table**
- **Dimension Tables**

This structure is optimized for **analytical queries and BI dashboards**.

---

# Star Schema Design

            dim_customer
                 |
                 |

dim_product --- fact_sales --- dim_store
|
|
dim_date


---

# Dimension Tables

Dimension tables store descriptive attributes.

### dim_customer


customer_id
customer_name
segment
city
state
country


---

### dim_product


product_id
product_name
category
sub_category
brand


---

### dim_store


store_id
store_name
city
state
region


---

### dim_date


date_id
date
day
month
quarter
year


Date dimension enables powerful time-based analytics.

---

# Fact Table

### fact_sales

Contains measurable business events.


sales_id
date_id
customer_id
product_id
store_id
quantity
revenue
profit


Fact tables connect to dimensions using **foreign keys**.

---

# ETL Pipeline

ETL pipeline is implemented using **Python**.

Location:


etl/


Scripts include:

### extract_load_staging.py

Loads CSV data into staging tables.

---

### transform_load_dims.py

Transforms staging data into dimension tables.

---

### load_fact_sales.py

Creates the **fact_sales** table by joining staging data with dimension keys.

---

### run_all.py

Runs the entire ETL pipeline sequentially.


python etl/run_all.py


---

# SQL Layer

SQL scripts define the warehouse structure.


sql/


Files include:


00_create_db.sql
01_create_staging.sql
02_create_dims.sql
03_create_fact.sql
99_validation.sql


---

# Data Validation

Validation queries ensure data integrity.

Examples:


Check row counts
Check null values
Check foreign key consistency
Validate revenue calculations


Validation file:


sql/99_validation.sql


---

# Dashboard (Streamlit)

A **Streamlit dashboard** is built on top of the warehouse.

File:


streamlit_app.py


Dashboard provides:

- Total Revenue
- Total Orders
- Units Sold
- Profit
- Revenue Trend
- Revenue by Category

---

# Example Dashboard Visualizations

### Revenue by Year

![Revenue by Year](images/revenue_year.png)

---

### Revenue and Sales by Quarter

![Revenue by Quarter](images/revenue_quarter.png)

---

# Tech Stack

| Tool | Purpose |
|----|----|
| Python | ETL pipeline |
| PostgreSQL | Data warehouse |
| SQL | Transformations |
| Pandas | Data processing |
| SQLAlchemy | Database connection |
| Streamlit | Dashboard |
| Git | Version control |
| GitHub | Project hosting |

---

# Project Structure


retail-sales/

data/raw/ # Raw CSV data

etl/ # ETL scripts
extract_load_staging.py
transform_load_dims.py
load_fact_sales.py
run_all.py

sql/ # SQL scripts
00_create_db.sql
01_create_staging.sql
02_create_dims.sql
03_create_fact.sql
99_validation.sql

streamlit_app.py # Dashboard

requirements.txt

run_pipeline.bat

README.md


---

# How to Run the Project

### 1 Install dependencies


pip install -r requirements.txt


---

### 2 Setup PostgreSQL database

Run SQL files:


sql/00_create_db.sql
sql/01_create_staging.sql
sql/02_create_dims.sql
sql/03_create_fact.sql


---

### 3 Run ETL Pipeline


run_pipeline.bat


or


python etl/run_all.py


---

### 4 Launch Dashboard


streamlit run streamlit_app.py


Open:


http://localhost:8501


---

# Example Analytics Questions

The warehouse supports queries such as:

- Total revenue by year
- Sales by product category
- Top selling products
- Sales by store location
- Quarterly revenue trends

---

# Future Improvements

Possible enhancements:

- Deploy dashboard to cloud
- Add Airflow orchestration
- Add dbt transformations
- Dockerize the entire pipeline
- Add automated testing
- Add CI/CD with GitHub Actions

---

# Author

Nikhil Teja

Data Engineering Portfolio Project
