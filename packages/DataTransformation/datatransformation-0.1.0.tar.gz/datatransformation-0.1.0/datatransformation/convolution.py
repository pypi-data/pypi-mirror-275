import numpy as np


def convolution2d(
    input_matrix: np.ndarray, kernel: np.ndarray, stride: int = 1
) -> np.ndarray:
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
    if not isinstance(input_matrix, np.ndarray) or input_matrix.ndim != 2:
        raise ValueError("input_matrix must be a 2D numpy array.")
    if not isinstance(kernel, np.ndarray) or kernel.ndim != 2:
        raise ValueError("kernel must be a 2D numpy array.")
    if not isinstance(stride, int) or stride <= 0:
        raise ValueError("stride must be a positive integer.")

    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate the dimensions of the output matrix
    output_height = (input_height - kernel_height) // stride + 1
    output_width = (input_width - kernel_width) // stride + 1

    # Initialize the output matrix with zeros
    output_matrix = np.zeros((output_height, output_width))

    # Perform the convolution operation (cross-correlation)
    for i in range(0, output_height):
        for j in range(0, output_width):
            region = input_matrix[
                i * stride : i * stride + kernel_height,
                j * stride : j * stride + kernel_width,
            ]
            output_matrix[i, j] = np.sum(region * kernel)

    return output_matrix
