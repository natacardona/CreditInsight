import matplotlib.pyplot as plt
import seaborn as sns

# Display basic information and the first few rows of the datasets
def display_basic_information(df):

    print(df.info())
    print(df.head())


# Statistical Summary  (Generate statistical summaries to understand distributions, means, medians, etc. )
def display_statistical_summaries(df):
    print(df.describe())

#  Visualize data to identify patterns, trends, and anomalies.   
def display_data_visualization(df):
    # Histograms for numeric data
    df['ARREARS_DAYS'].hist(bins=50)
    plt.title('Distribution of Arrears Days')
    plt.show()