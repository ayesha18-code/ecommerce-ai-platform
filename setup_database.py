import sqlite3
import pandas as pd

# CSV files load karo
monthly_sales = pd.read_csv('data/monthly_sales.csv')
top_products = pd.read_csv('data/top_products.csv')
customer_data = pd.read_csv('data/customer_sales_with_segments.csv')

monthly_sales.columns = ['month', 'revenue']
top_products.columns = ['category', 'revenue']

# Database banao aur data daalo
conn = sqlite3.connect('data/ecommerce.db')

monthly_sales.to_sql('monthly_sales', conn, if_exists='replace', index=False)
top_products.to_sql('top_products', conn, if_exists='replace', index=False)
customer_data.to_sql('customer_data', conn, if_exists='replace', index=False)

conn.close()
print("Database created successfully: data/ecommerce.db")