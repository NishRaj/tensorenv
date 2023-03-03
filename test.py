# import tensorflow
# import keras
import numpy as np

matrix_1 = np.random.randint(1, 10, (2, 3, 4))
print(matrix_1)
print(matrix_1.flatten('C'))
# print(np.split(matrix_1, axis=0))

# print(np.resize(matrix_1, (2, 30)))
print(np.reshape(matrix_1, (3, 2, 4)))


##### collapse the matrix #############

def collapse_matrix(matrix) -> np.ndarray:
    """
    :param matrix:
    :return: numpy array with one dimension
    >>> collapse_matrix(np.ones((1,2,3)))
    array([1., 1., 1., 1., 1., 1.])
    """
    return matrix.flatten('C')


def reshape_matrix(matrix, new_dimension) -> np.ndarray:

    """
    :param matrix:
    :param new_dimension: new dimension to convert the matrix
    :return: numpy array with new dimension
    >>> reshape_matrix(np.ones((3,4)),(2,6))
    array([[1., 1., 1., 1., 1., 1.],
           [1., 1., 1., 1., 1., 1.]])
    """
    return np.reshape(matrix, new_dimension)


def rotate_matrix(matrix) -> np.ndarray:

    """
    :param matrix: matrix to rotate
    :return: matrix : rotated matrix
    >>> rotate_matrix(np.array([[1, 2, 3], [4, 5, 6]], dtype=int))
    array([[1, 4],
           [2, 5],
           [3, 6]])
    """
    return matrix.T

print(round(43.75))
