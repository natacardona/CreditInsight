from data.make_datasets import get_trainnig_model_dataframe, merge_dataframes
from models.train_model import train_model
from visualization.visualize import display_basic_information, display_statistical_summaries, plot_arrears_by_client, plot_arrears_days_distribution, plot_arrears_time_series, plot_loan_activity_heatmap

def main():

    final_merged_df = merge_dataframes()
    
    static_merged_df = merge_dataframes()
    
    print("----------------------------------------------EDA------------------------------------------------------------")
    
    display_basic_information(final_merged_df)
    display_statistical_summaries(final_merged_df)
    
    print("----------------------------------------------------------------------------------------------------------")
    
    plot_arrears_days_distribution(final_merged_df)
    
    plot_loan_activity_heatmap(final_merged_df)
    
    plot_arrears_by_client(final_merged_df)
    
    plot_arrears_time_series(static_merged_df)
    
    print("---------------------------------------- ML MODEL ---------------------------------------------------")
    
    traing_modeldf = get_trainnig_model_dataframe(final_merged_df)

    train_model(traing_modeldf)
    
    print("----------------------------------------------------------------------------------------------------------")
            
if __name__ == "__main__":
    main() 