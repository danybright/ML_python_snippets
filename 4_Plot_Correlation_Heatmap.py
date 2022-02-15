import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plt_corr_heatmap(df):
    """ 

    Plot correlation heatmap for given dataframe without redundant values

    Parameters
    ----------
    df : pandas DataFrame
    The dataset of the project 

    """
    corr = df.corr()
    sns.set_context("notebook", font_scale=1.0, rc={"lines.linewidth": 3.5})
    plt.figure(figsize=(20, 10))
    # create a mask so we only see the correlation values once
    mask = np.zeros_like(corr)
    # Return the indices for the upper-triangle of arr.
    mask[np.triu_indices_from(mask, 1)] = True
    a = sns.heatmap(corr, mask=mask, annot=True, fmt='.2f')
    rotx = a.set_xticklabels(a.get_xticklabels(), rotation=90)
    roty = a.set_yticklabels(a.get_yticklabels(), rotation=30)
