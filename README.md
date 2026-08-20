# AI-Powered E-Commerce Customer Intelligence & Sales Analytics Platform

## Overview
This project analyzes e-commerce data (Brazilian Olist dataset) to provide customer segmentation, product recommendations, and sales analytics through an interactive web dashboard. Built as part of an Industry ML Internship with 3 team members.

## Team Members & Modules
| Member | Module |
|--------|--------|
| Member 1 | Customer Intelligence / Segmentation (RFM + K-Means) |
| Member 2 | Recommendation System (Content-Based/Collaborative Filtering) |
| Member 3 (Ayesha) | Sales Analytics + Web Platform (Dashboard, Backend, Integration) |

## My Contribution (Member 3)
- Sales data analysis: total revenue, best-selling products, monthly trends, customer-wise sales (via Google Colab)
- Built the Flask backend and SQLite database
- Designed an interactive Admin Dashboard using Chart.js
- Integrated Member 1's customer segmentation and Member 2's recommendation output into one unified platform

## Tech Stack
- Python, Pandas, Flask, SQLite
- HTML, CSS, JavaScript, Chart.js
- Google Colab (for EDA and analysis)

## Project Structure
ecommerce_dashboard/
├── app.py
├── setup_database.py
├── requirement.txt
├── data/
│ ├── monthly_sales.csv
│ ├── top_products.csv
│ ├── customer_sales_with_segments.csv
│ ├── recommendations.csv
│ └── ecommerce.db
├── templates/
│ └── dashboard.html
└── static/
└── style.css

## How to Run
```bash
pip install -r requirement.txt
python setup_database.py
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

## Dataset
[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## Features
- Total revenue, average order value, total customers (KPIs)
- Monthly sales trend chart
- Top-selling product categories chart
- Customer segmentation table (New / Regular / High-Value / At-Risk)
- Personalized product recommendations