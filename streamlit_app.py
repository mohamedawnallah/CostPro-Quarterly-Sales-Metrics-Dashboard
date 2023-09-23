import pandas as pd
import plotly.express as px
import streamlit as st
from src.filter_by_year_and_quarter import *
from src.total_sales import *
from src.mean_customers_per_day import *
from src.median_order_value import *
from src.most_popular_product import *
from src.most_profitable_product import *
from src.customer_retention_rate import *
from src.order_value_variability import *

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

# Filter the data for the previous quarter needed for customer retention
previous_quarter = quarter - 1 if quarter > 1 else 4
previous_year = year if quarter > 1 else year - 1
filtered_df_previous_quarter = df[(df['Year'] == previous_year) & (df['Quarter'] == previous_quarter)]

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
customer_retention_rate_result = customer_retention_rate(filtered_df, filtered_df_previous_quarter)
if not customer_retention_rate_result:
    customer_retention_rate_result = f"No retention rate for Q{quarter} {year}."
else:
    customer_retention_rate_result = f"{customer_retention_rate_result}%"
st.metric(f"Q{quarter} Customer retention rate", customer_retention_rate_result, delta=None, delta_color="normal", help=None, label_visibility="visible")

# YOUR CUSTOM METRIC HERE

# VISUALIZE THE DATA
# Create a scatterplot of unit prices for the selected quarter
st.subheader(f"Q{quarter} Unit Price Distribution")
fig = px.scatter(filtered_df, x="UnitPrice", color="UnitPrice")
st.plotly_chart(fig)

# YOUR CUSTOM VIZ HERE
