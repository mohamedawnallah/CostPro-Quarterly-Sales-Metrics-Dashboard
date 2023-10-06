import numpy as np
import plotly.express as px

# Visualize the Binomial distribution for Cumulative Distribution Functions
def plot_customer_arrival_proba(poisson_dist):
    x = np.arange(0, 100, 5)
    y = poisson_dist.pmf(x)

    fig = px.bar(x=x, y=y)
    fig.update_xaxes(title_text='Number of Visits to the Store per Day')
    fig.update_yaxes(title_text='Probability (PMF)')
    fig.update_layout(title=f'Poisson Distribution for Customer Arrivals')
    return fig
