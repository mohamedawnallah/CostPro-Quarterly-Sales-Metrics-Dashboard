import numpy as np
import plotly.express as px

# Visualize the Binomial distribution for Cumulative Distribution Functions
def plot_customer_arrival_proba(poisson_dist):
    x = np.arange(0, 150, 5)
    y = poisson_dist.cdf(x)

    fig = px.bar(x=x, y=y)
    fig.update_xaxes(title_text='Number of Customer Arrivals')
    fig.update_yaxes(title_text='Probability (CDF)')
    fig.update_layout(title=f'Poisson Distribution for Customer Arrivals')
    return fig
