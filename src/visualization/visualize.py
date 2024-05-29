# Display basic information and the first few rows of the datasets
def display_basic_information(arrears_adj,eeff,hist_loans):

    print(arrears_adj.info())
    print(arrears_adj.head())

    print(eeff.info())
    print(eeff.head())

    print(hist_loans.info())
    print(hist_loans.head())