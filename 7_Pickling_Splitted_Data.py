import pickle


def dump_pickle(fname, data):
    """ 

    Save loaded data for easy use

    Parameters
    ----------
    fname : raw string
    The string of file name with extension

    data : pandas DataFrame
    The dataset of the project

    """
    pick_in = open(fname, 'wb')
    pickle.dump(data, pick_in)
    pick_in.close()


def load_pickle(fname):
    """

    Load saved data for modelling

    Parameters
    ----------
    fname : raw string
    The string of pre-saved file name with extension

    Returns
    --------
    DataFrame
    The preprocessed dataset of the project

    """
    pick_out = open(fname, 'rb')
    data = pickle.load(pick_out)
    pick_out.close()
    return data
