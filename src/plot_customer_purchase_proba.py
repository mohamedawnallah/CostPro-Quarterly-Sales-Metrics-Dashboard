import numpy as np
import plotly.express as px

# Visualize the Binomial distribution for Cumulative Distribution Functions
def plot_customer_purchase_proba(binomial_dist):
    x = np.arange(0, 100, 5)
    y = binomial_dist.cdf(x)

    fig = px.bar(x=x, y=y)
    fig.update_xaxes(title_text='Number of Successes (sales > 1,000)')
    fig.update_yaxes(title_text='Probability (CDF)')
    fig.update_layout(title=f'Binomial Distribution for Customer Purchase Probability')
    return fig