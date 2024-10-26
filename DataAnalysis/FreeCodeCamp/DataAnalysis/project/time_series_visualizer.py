import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("/Users/luneto10/Documents/Study/DataAnalysis/FreeCodeCamp/data/fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
top_value = df['value'].quantile(0.975)
bottom_value = df['value'].quantile(0.025)
df = df[(df['value'] > bottom_value) & (df['value'] < top_value)]


def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots(figsize=(18,6))
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    axes.plot(df.index, df['value'], color="red")
    axes.set_xlabel("Date")
    axes.set_ylabel("Page Views")
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar.reindex(month_order, axis="columns")

    # Draw bar plot

    fig = df_bar.plot.bar(figsize=(18,6), width=0.2, legend = True, ylabel='Average Page Views', xlabel='Years').figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['month_number'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_number')

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18,6))

    axes[0] = sns.boxplot(x=df_box['year'], y=df_box['value'], ax=axes[0])
    axes[1] = sns.boxplot(x=df_box['month'], y=df_box['value'], ax=axes[1])

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_ylabel("Page Views")
    axes[0].set_xlabel("Year")

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_ylabel("Page Views")
    axes[1].set_xlabel("Month")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
