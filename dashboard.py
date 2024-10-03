import streamlit as st
import pandas as pd

# Load data from CSV file
df = pd.read_csv('products_dataset.csv')

# Dashboard title
st.title('Product Dashboard')

# Display basic information
st.write("Total Products:", len(df))
st.write("Total Product Categories:", df['product_category_name'].nunique())
st.write("Average Product Weight (g):", df['product_weight_g'].mean())

# Display statistics by product category
st.subheader('Statistics by Product Category')
category_stats = df.groupby('product_category_name').agg({
    'product_id': 'count',
    'product_weight_g': 'mean',
    'product_photos_qty': 'mean'
}).rename(columns={
    'product_id': 'Total Products',
    'product_weight_g': 'Average Weight (g)',
    'product_photos_qty': 'Average Number of Photos'
}).reset_index()

st.write(category_stats)

# Visualization of average product weight per category
st.subheader('Average Product Weight by Category')
st.bar_chart(category_stats.set_index('product_category_name')['Average Weight (g)'])

# Visualization of total products per category
st.subheader('Total Products by Category')
st.bar_chart(category_stats.set_index('product_category_name')['Total Products'])

