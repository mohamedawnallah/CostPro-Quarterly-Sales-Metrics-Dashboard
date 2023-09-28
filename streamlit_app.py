import pandas as pd
import plotly.express as px
import streamlit as st
from src.filter_by_year_and_quarter import filter_by_year_and_quarter
from src.total_sales import total_sales
from src.mean_customers_per_day import mean_customers_per_day
from src.median_order_value import median_order_value
from src.most_popular_product import most_popular_product
from src.most_profitable_product import most_profitable_product
from src.customer_retention_rate import customer_retention_rate
from src.order_value_variability import order_value_variability
from src.customer_purchase_proba import customer_purchase_proba
from src.customer_arrival_proba import customer_arrival_proba
from src.plot_customer_purchase_proba import plot_customer_purchase_proba
from src.plot_customer_arrival_proba import plot_customer_arrival_proba

# Display title and text
st.title("CostPro Quarterly Sales Metrics")

# Read dataframe
# df = pd.read_csv('./retail_metrics_dashboard/data.csv')
df = pd.read_csv('./data.csv')

# Create a selection widget to choose the quarter
year = st.selectbox("Select quarter:", df["Year"].unique())
quarter = st.selectbox("Select quarter:", df["Quarter"].unique())

# Filter the data for the selected quarter
filtered_df = filter_by_year_and_quarter(df, year, quarter)

customer_purchase_binomial_dist = customer_purchase_proba(filtered_df)
customer_arrival_poisson_dist = customer_arrival_proba(filtered_df)

# SUMMARIZE THE DATA
# Display the total sales for the selected quarter
st.metric(f"Q{quarter} Total sales", f"${total_sales(filtered_df)}", delta=None, delta_color="normal", help=None, label_visibility="visible")

# MEAN
# Display the mean number of customers per day for the selected quarter
st.metric(f"Q{quarter} Mean Number of Customers Per Day", f"{mean_customers_per_day(filtered_df)}", delta=None, delta_color="normal", help=None, label_visibility="visible")

# MEDIAN
# Display the median order value for the selected quarter
st.metric(f"Q{quarter} Median Order Value", f"${median_order_value(filtered_df)}", delta=None, delta_color="normal", help=None, label_visibility="visible")

# STANDARD DEVIATION
# Display the standard deviation of order values for the selected quarter
st.metric(f"Q{quarter} Standard Deviation of Order Values", f"${order_value_variability(filtered_df)}", delta=None, delta_color="normal", help=None, label_visibility="visible")

# MODE
# Calculate the most popular product(mode) in the selected quarter
st.metric(f"Q{quarter} Most Popular Product", f"{most_popular_product(filtered_df)}", delta=None, delta_color="normal", help=None, label_visibility="visible")

# Calculate the most profitable product(mode) in the selected quarter
st.metric(f"Q{quarter} Most Profitable Product", f"{most_profitable_product(filtered_df)}", delta=None, delta_color="normal", help=None, label_visibility="visible")

# CUSTOM METRICS
# Display the customer retention rate for the selected quarter
st.metric(f"Q{quarter} Customer retention rate", customer_retention_rate(filtered_df), delta=None, delta_color="normal", help=None, label_visibility="visible")

# YOUR CUSTOM METRIC HERE

# VISUALIZE THE DATA
# Create a scatterplot of unit prices for the selected quarter
st.subheader(f"Q{quarter} Unit Price Distribution")
unit_price_dist_fig = px.scatter(filtered_df, x="UnitPrice", color="UnitPrice")
st.plotly_chart(unit_price_dist_fig)

# YOUR CUSTOM VIZ HERE
st.subheader(f"Q{quarter} Customer Purchase Probability")
customer_purchase_proba_fig = plot_customer_purchase_proba(customer_purchase_binomial_dist)
st.plotly_chart(customer_purchase_proba_fig)


st.subheader(f"Q{quarter} Customer Arrival Probability")
customer_arrival_proba_fig = plot_customer_arrival_proba(customer_arrival_poisson_dist)
st.plotly_chart(customer_arrival_proba_fig)
