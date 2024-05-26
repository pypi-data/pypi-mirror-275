import numpy as np
from typing import Union, List


def window1d(
    input_array: Union[list, np.ndarray],
    size: int,
    shift: int = 1,
    stride: int = 1,
) -> List[np.ndarray]:
    """
    Generate 1D sliding windows from the input array.

    Parameters:
    ----------
    input_array : Union[list, np.ndarray]
        A 1D list or numpy array from which windows are to be extracted.
    size : int
        The size of each window.
    shift : int, optional
        The shift (step) between the starting points of consecutive windows. Default is 1.
    stride : int, optional
        The stride (step) between elements within a window. Default is 1.

    Returns:
    -------
    List[np.ndarray]
        A list of 1D numpy arrays, each representing a window from the input array.

    Raises:
    ------
    ValueError
        If `size`, `shift`, or `stride` is not a positive integer.
        If `input_array` is not 1D.
    TypeError
        If `input_array` is not a list or a 1D numpy array.

    Example:
    -------
    >>> input_array = [1, 2, 3, 4, 5, 6]
    >>> window1d(input_array, size=3, shift=2, stride=1)
    [array([1, 2, 3]), array([3, 4, 5]), array([5, 6])]
    """
    # Validate parameters
    if not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer.")
    if not isinstance(shift, int) or shift <= 0:
        raise ValueError("shift must be a positive integer.")
    if not isinstance(stride, int) or stride <= 0:
        raise ValueError("stride must be a positive integer.")

    # Ensure input_array is either a list or a 1D numpy array
    if not isinstance(input_array, (list, np.ndarray)):
        raise TypeError("input_array must be a list or a 1D numpy array.")

    # Convert input to numpy array if it is a list
    if isinstance(input_array, list):
        input_array = np.array(input_array)

    # Ensure input_array is 1D
    if input_array.ndim != 1:
        raise ValueError("input_array must be 1D.")

    result = []
    start = 0

    while start + (size - 1) * stride < len(input_array):
        window = input_array[start : start + size * stride : stride]

        # Ensure window length is exactly equal to size
        if len(window) == size:
            result.append(window)

        start += shift

    return result
