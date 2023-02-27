import numpy as np


def identity_matrix(dim1, dim2):
    """
    :param dim1:
    :param dim2:
    :return: identity matrix
    >>> identity_matrix(2,2)
    array([[1., 0.],
           [0., 1.]])
    >>> identity_matrix(3,3)
    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])
    """
    return np.eye(dim1, dim2)
