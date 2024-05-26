from typing import Union
import numpy as np


def transpose2d(input_matrix: list[list[float]]) -> list[list[float]]:
    """
    Transpose a 2D list of floats (matrix).

    Parameters:
    ----------
    input_matrix : List[List[float]]
        A 2D list of floats representing the input matrix to be transposed.

    Returns:
    -------
    List[List[float]]
        A 2D list of floats representing the transposed matrix.

    Raises:
    ------
    ValueError
        If `input_matrix` is not a 2D list of lists.
        If the rows in the input matrix do not all have the same number of columns.

    Example:
    -------
    >>> matrix = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    >>> transpose2d(matrix)
    [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]
    """
    if not isinstance(input_matrix, list) or not all(
        isinstance(row, list) for row in input_matrix
    ):
        raise ValueError("Input must be a 2D list of lists")

    if len(input_matrix) == 0:
        return []

    num_cols = len(input_matrix[0])
    if any(len(row) != num_cols for row in input_matrix):
        raise ValueError(
            "All rows in the input matrix must have the same number of columns"
        )

    return [[row[i] for row in input_matrix] for i in range(num_cols)]
