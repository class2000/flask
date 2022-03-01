import pandas as pd
import plotly.express as px
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
annualChangeForestArea = pd.read_csv('flaskweb/static/annual-change-forest-area.csv')

def plot_net_conv(scope,title):
    fig = px.choropleth(
        annualChangeForestArea,
        locations ="Code",
        color ="Net forest conversion",
        hover_name ="Entity",
        scope=scope,
        color_continuous_scale='RdYlGn',
        animation_frame ="Year")
    
    fig.update_layout(title_text=title,
        font_family="Rockwell",
        title_font_size=20,
        coloraxis_colorbar=dict(
            title='Net Forest Conversion'))
    
    fig.show()

