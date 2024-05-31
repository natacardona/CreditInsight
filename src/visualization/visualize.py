from matplotlib import ticker
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import pandas as pd  # Make sure to import pandas
import seaborn as sns
import matplotlib.pyplot as plt

# Display basic information and the first few rows of the datasets
def display_basic_information(df):

    print(df.info())
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    print(df.head())
    print("---------------------------------------------------------------------------------------------------------------------------------------------")


# Statistical Summary  (Generate statistical summaries to understand distributions, means, medians, etc. )
def display_statistical_summaries(df):
    print(df.describe())
    print("---------------------------------------------------------------------------------------------------------------------------------------------")

def plot_arrears_days_distribution(df):
    # Define the bins for the histogram
    bin_edges = np.linspace(0, 100, 51)  # Creates 50 bins between 0 and 100

    plt.figure(figsize=(10, 6))
    # Histogram plotting with rwidth for padding between bars
    n, bins, patches = plt.hist(df['ARREARS_DAYS'], bins=bin_edges, color='#4D4CFC', alpha=0.7, rwidth=0.85, label='Arrears Days')

    # Adding text for bin ranges in the legend
    bin_labels = [f'{bins[i]:.1f} - {bins[i+1]:.1f}' for i in range(len(bins)-1)]
    for patch, label in zip(patches, bin_labels):
        patch.set_label(label)
        break

    # Only add unique labels to the legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Removing duplicates
    plt.legend(by_label.values(), by_label.keys(), title="Bins", loc='upper right')

    plt.yscale('log')  # Apply logarithmic scale
    plt.title('Distribution of Arrears Days (Log Scale)')
    plt.xlabel('Arrears Days')
    plt.ylabel('Log Frequency')
    plt.grid(True)
    plt.show()

def plot_loan_activity_heatmap(df):
    current_year = pd.to_datetime('now').year
    start_year = current_year - 3
    df_filtered = df[df['ACTIVATION_DATE'].dt.year >= start_year]

    # Add 'Year' and 'Quarter' columns
    df_filtered['Year'] = df_filtered['ACTIVATION_DATE'].dt.year
    df_filtered['Quarter'] = df_filtered['ACTIVATION_DATE'].dt.to_period('Q').astype(str)  # Convert to string for easier pivoting

    # Group by year and quarter, count the number of loans
    quarterly_loans = df_filtered.groupby(['Year', 'Quarter']).size().reset_index(name='Loan Count')

    # Pivot the data for heatmap display
    heatmap_data = quarterly_loans.pivot(index='Quarter', columns='Year', values='Loan Count')
    
    cmap = LinearSegmentedColormap.from_list("custom_blue", ["white", "#4D4CFC"], N=100)

    # Create the heatmap
    plt.figure(figsize=(10, 6))
    ax = sns.heatmap(heatmap_data, annot=True, cmap=cmap, fmt='g')
    ax.grid(True, which='both', color='gray', linewidth=0.5, linestyle='-')
    plt.title('Quarterly Activation of Loans for the Last 3 Years')
    plt.xlabel('Year')
    plt.ylabel('Quarter')
    plt.show()
    
def plot_arrears_by_client(df):
    # Sampling a subset of clients for clarity in visualization
    sample_clients = df['CLIENT_ID'].drop_duplicates().sample(n=20, random_state=42)
    filtered_df = df[df['CLIENT_ID'].isin(sample_clients)]

    plt.figure(figsize=(12, 8))
    sns.boxplot(x='CLIENT_ID', y='ARREARS_DAYS', data=filtered_df, color="#4D4CFC")
    plt.xticks(rotation=90)
    plt.title('Arrears Days by Client ID')
    plt.xlabel('Client ID')
    plt.ylabel('Arrears Days')
    plt.show()
    
def plot_arrears_time_series(df):
    df['ARREARS_DATE'] = pd.to_datetime(df['ARREARS_DATE'])
    df.set_index('ARREARS_DATE', inplace=True)

    # Now you can safely resample and plot
    df['ARREARS_DAYS'].resample('M').sum().plot(figsize=(10, 6), linewidth=2, color='#4D4CFC')
    plt.title('Time Series of Total Arrears Days Per Month')
    plt.xlabel('Date')
    plt.ylabel('Total Arrears Days')
    plt.grid(True)
    plt.show()