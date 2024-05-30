from data.make_datasets import get_trainnig_model_dataframe, merge_dataframes,yearly_count_dataframe
from features.features import create_features
from visualization.visualize import arrears_count_per_year, display_basic_information, display_data_visualization, display_statistical_summaries,log_data, plot_correlation
def main():

    final_merged_df = merge_dataframes()
    
    plot_correlation(final_merged_df)

    display_basic_information(final_merged_df)
    
    display_statistical_summaries(final_merged_df)
    
    #display_data_visualization(final_merged_df)

    df = create_features(final_merged_df)
    
    display_statistical_summaries(df)
    
    log_data(df)
    
    display_data_visualization(final_merged_df)      
    
    arrears_count_per_year(yearly_count_dataframe(final_merged_df))
    
    traing_modeldf = get_trainnig_model_dataframe(final_merged_df)


        
if __name__ == "__main__":
    main() 