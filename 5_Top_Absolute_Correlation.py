import pandas as pd


def get_redundant_pairs(df):
    """ 

    Get diagonal and lower triangular pairs of correlation matrix

    Parameters
    ----------
    df : pandas DataFrame
    The dataset of the project

    Returns
    --------
    list
        The list representing the redundant pairs of data

    """
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop


def get_top_abs_correlations(df, n=20):
    ''' 

    Return the top absolute correlation values 

    Parameters
    ----------
    df : pandas DataFrame
    The dataset of the project

    n : int
    an integer value that defines the number of top correlation values to be displayed (default is '20')

    Returns
    --------
    Series or List
        The Series or list representing the top correlation values

    '''
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]
