
from flask import Flask, render_template, jsonify
import sqlite3
import pandas as pd
import json

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect('data/ecommerce.db')
    monthly_sales = pd.read_sql('SELECT * FROM monthly_sales', conn)
    top_products = pd.read_sql('SELECT * FROM top_products', conn)
    customer_data = pd.read_sql('SELECT * FROM customer_data', conn)
    conn.close()
    return monthly_sales, top_products, customer_data


@app.route('/')
def dashboard():
    monthly_sales, top_products, customer_data = get_data()

    total_revenue = round(customer_data['total_spend'].sum(), 2)
    total_customers = customer_data['customer_unique_id'].nunique()
    avg_order_value = round(customer_data['total_spend'].mean(), 2)

    segment_counts = customer_data['Customer_Category'].value_counts().to_dict()
    segment_revenue = customer_data.groupby('Customer_Category')['total_spend'].sum().round(2).to_dict()

    monthly_labels = monthly_sales['month'].astype(str).tolist()
    monthly_values = monthly_sales['revenue'].tolist()

    top_product_labels = top_products['category'].tolist()
    top_product_values = top_products['revenue'].tolist()

    dummy_recommendations = [
        {"product": "Bed & Bath Linen", "reason": "Popular in your segment"},
        {"product": "Health & Beauty", "reason": "Frequently bought together"},
        {"product": "Sports & Leisure", "reason": "Trending this month"},
        {"product": "Electronics", "reason": "Based on similar customers"},
    ]

    return render_template(
        'dashboard.html',
        total_revenue=total_revenue,
        total_customers=total_customers,
        avg_order_value=avg_order_value,
        segment_counts=segment_counts,
        segment_revenue=segment_revenue,
        monthly_labels=json.dumps(monthly_labels),
        monthly_values=json.dumps(monthly_values),
        top_product_labels=json.dumps(top_product_labels),
        top_product_values=json.dumps(top_product_values),
        recommendations=dummy_recommendations,
    )


if __name__ == '__main__':
    app.run(debug=True)