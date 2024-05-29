import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(df):
    """
    Generate plots to explore the data.

    Parameters:
    df (pd.DataFrame): The data frame to plot.

    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df['max_arrears_6m'], kde=True)
    plt.title('Histogram of Max Arrears Over 6 Months')
    plt.show()
