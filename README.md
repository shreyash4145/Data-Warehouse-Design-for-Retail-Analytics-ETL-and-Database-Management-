# Retail Data Warehouse Design for Retail Analytics

This project is a data warehouse solution for retail analytics, designed to support BI and analytics using PostgreSQL, Power BI, and ETL workflows.

## Features
- **ETL Workflows**: Extract, transform, and load retail transaction data into a PostgreSQL database.
- **SQL Queries**: Optimized SQL queries for complex analytics and reporting.
- **Power BI Dashboards**: Interactive dashboards for sales and customer analytics.

## Project Structure
📂 retail-data-warehouse/
│── 📂 etl/ # ETL scripts for data transformation
│── 📂 sql/ # SQL queries for analytics
│── 📂 reports/ # Power BI dashboards
│── README.md
│── requirements.txt
│── LICENSE


## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up PostgreSQL and create a database named retail_warehouse

3. Run the ETL workflows:
   ```bash
   python -m etl.extract
   python -m etl.transform
   python -m etl.load
   ```

4. Use the SQL queries in the `sql/` directory for analytics.

5. Open the Power BI dashboards in the `reports/` directory.
