import scipy.stats as stats


def Hypothesis_testing(col1, col2):
    """ 
    Return the p-value along with the test results that accepts or rejects the hypothesis

    Hypothesis
    ----------
        Ho : No significant difference in the distributions after the missing value imputations OR outlier treatment

        Ha : There is a significant difference in the distributions after the missing value imputations OR outlier treatment

    Parameters
    ----------
        col1 : pandas Series, list
        The series or list of the column data from raw dataset.

        col2: pandas Series, list
        The series or list of the same column data from preprocessed dataset.

    Returns
    --------
    string 
        a string representing the p-value and the result of the hyposthesis

    """
    t, pval = stats.ttest_rel(col1, col2, nan_policy='omit')

    if pval < 0.05:
        return("pval ->" + str(pval) + ' -  reject null hypothesis')
    else:
        return("pval ->" + str(pval) + ' - accept null hypothesis')
