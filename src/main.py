from data.make_datasets import merge_dataframes
from features.features import create_features
from visualization.visualize import display_basic_information, display_data_visualization, display_statistical_summaries, log_data

def main():

    final_merged_df = merge_dataframes()

    display_basic_information(final_merged_df)
    
    display_statistical_summaries(final_merged_df)
    
    #display_data_visualization(final_merged_df)

    df = create_features(final_merged_df)
    
    display_statistical_summaries(df)
    
    log_data(df)
            
if __name__ == "__main__":
    main() 