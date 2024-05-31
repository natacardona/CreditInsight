from data.make_datasets import get_trainnig_model_dataframe, merge_dataframes
from models.train_model import train_model
from visualization.visualize import plot_arrears_by_client, plot_arrears_days_distribution, plot_arrears_time_series, plot_loan_activity_heatmap
def main():

    final_merged_df = merge_dataframes()
    
    plot_arrears_days_distribution(final_merged_df)
    
    plot_loan_activity_heatmap(final_merged_df)
    
    plot_arrears_by_client(final_merged_df)
    
    plot_arrears_time_series(merge_dataframes())
    
    traing_modeldf = get_trainnig_model_dataframe(final_merged_df)

    train_model(traing_modeldf)
            
if __name__ == "__main__":
    main() 