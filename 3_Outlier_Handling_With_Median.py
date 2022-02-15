import pandas as pd


def outlier_handling_median(data):
    """  
    Handle the outliers by replacing them with median 

    Parameters
    ----------
    data : pandas DataFrame
    The dataset of the project

    """
    for col_name in data.columns[:-1]:
        q1 = data[col_name].quantile(0.25)
        q3 = data[col_name].quantile(0.75)
        iqr = q3 - q1

        low = q1-1.5*iqr
        high = q3+1.5*iqr

        data.loc[(data[col_name] < low) | (data[col_name] > high),
                 col_name] = data[col_name].median()
