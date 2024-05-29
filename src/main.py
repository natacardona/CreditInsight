from data.make_datasets import load_data

def main():
    # Load data
    arrears_days_month_end = load_data('https://drive.google.com/uc?export=download&id=1Pcl-Jpvu1Ixtl-rDHY2o8Vdy63g4aEC9')
  
    eeff = load_data('https://drive.google.com/uc?export=download&id=1fTo2b_ReZ8eVzm76kQIlOy62teTQsxVT')
    
    hist_loans = load_data('https://drive.google.com/uc?export=download&id=1m8H_sTubphMaU0CH625LrPHXYNHAMN96')
  
    eeff.info
if __name__ == "__main__":
    main()
