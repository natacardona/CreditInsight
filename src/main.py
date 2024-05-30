from data.make_datasets import merge_dataframes
from visualization.visualize import display_basic_information, display_data_visualization, display_statistical_summaries

def main():

    final_merged_df = merge_dataframes()

    display_basic_information(final_merged_df)
    
    display_statistical_summaries(final_merged_df)
    
    display_data_visualization(final_merged_df)
        
if __name__ == "__main__":
    main()