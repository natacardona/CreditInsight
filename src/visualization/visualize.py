from matplotlib import ticker
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

#  Visualize data to identify patterns, trends, and anomalies.   
def display_data_visualization(df):
    # Histograms for numeric data
    df['ARREARS_DAYS'].hist(bins=50)
    plt.title('Distribution of Arrears Days')
    plt.show()
    
def  log_data(df):
    filtered_df = df[df['ARREARS_DAYS'] > 0]
    
    # Print the filtered DataFrame
    if not filtered_df.empty:
        print(filtered_df)
    else:
        print("No rows with arrears_days greater than 0.")
        
    # Filter rows where ARREARS_DAYS is not equal to max_arrears_6m
    different_rows = df[df['ARREARS_DAYS'] != df['max_arrears_6m']]
    print(different_rows)

    # Optionally, display only the first few rows if there are many
    print(different_rows.head(20))
    
def plot_correlation(df):
    # Define column aliases for better readability
    column_aliases = {
        'CLIENT_ID': 'Client ID',
        'LOAN_CODE': 'Loan Code',
        'ACTIVATION_DATE': 'Activation Date',
        'ARREARS_DAYS': 'Arrears Days',
        'ARREARS_DATE': 'Arrears Date'
    }
    
    # Select and rename the columns of interest
    columns_of_interest = ['CLIENT_ID', 'LOAN_CODE', 'ACTIVATION_DATE', 'ARREARS_DAYS', 'ARREARS_DATE']
    auxdf = df[columns_of_interest].rename(columns=column_aliases)
    
    # Convert all columns to numeric, errors coerce will turn non-convertibles into NaN
    auxdf = auxdf.apply(pd.to_numeric, errors='coerce')
    
    # Calculate the correlation matrix
    plt.figure(figsize=(10, 8))
    try:
        correlation_matrix = auxdf.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Matrix')
        plt.show()
    except ValueError as e:
        print("Error computing the correlation matrix:", e)

    
def arrears_count_per_year(yearly_data):
    plt.figure(figsize=(12, 8))
    ax = plt.subplot(111)  # Add a subplot for detailed customization

    bars = plt.bar(yearly_data['YEAR'], yearly_data['COUNT'], color='skyblue')

    # Adding data labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}', ha='center', va='bottom', fontsize=9, fontweight='bold', color='red')

    # Customize the plot with titles and labels
    plt.title('Annual Count of Arrears', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Count of Arrears', fontsize=14)

    # Improve the y-axis scale readability with a thousands separator
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    # Optional: Add a grid for better readability of the plot
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Improve legibility of the x-axis labels
    plt.xticks(yearly_data['YEAR'], rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    # Tight layout to ensure no clipping of tick labels
    plt.tight_layout()

    plt.show()