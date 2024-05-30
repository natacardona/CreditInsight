import matplotlib.pyplot as plt
import seaborn as sns

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