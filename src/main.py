from data.make_datasets import clean_data, load_data
from features.features import create_features
from models.model import train_predict
from visualization.explore_data import plot_data
from visualization.visualize import display_basic_information

def main():
    # Load data
    arrears_adj = load_data('https://drive.google.com/uc?export=download&id=1Pcl-Jpvu1Ixtl-rDHY2o8Vdy63g4aEC9')
  
    eeff = load_data('https://drive.google.com/uc?export=download&id=1fTo2b_ReZ8eVzm76kQIlOy62teTQsxVT')
    
    hist_loans = load_data('https://drive.google.com/uc?export=download&id=1m8H_sTubphMaU0CH625LrPHXYNHAMN96')
    #change columns upper to lower case
    arrears_adj.columns = [col.lower() for col in arrears_adj.columns]

    display_basic_information(arrears_adj,eeff,hist_loans)
    
    df = create_features(arrears_adj)
    

    
    """  
    # Explore data
    plot_data(df)
    
    # Train and evaluate model
    results = train_predict(df, 'arrears_days')
    print(results)
 
    """  
if __name__ == "__main__":
    main()
