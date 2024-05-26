Sure! Here is an updated version of the `README.md` file that includes the project structure:

```markdown
# Data Transformation Library

This Python library provides functions commonly used for transforming data in machine learning models. The library is designed to be lightweight, efficient, and easy to use.

## Functions

### 1. Transpose

The `transpose2d` function switches the axes of a 2D tensor (matrix). This operation is frequently used in data science workflows for various data manipulation tasks.

#### Signature:
```python
def transpose2d(input_matrix: list[list[float]]) -> list[list[float]]:
    ...
```

#### Usage:
```python
input_matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
output_matrix = transpose2d(input_matrix)
```

### 2. Time Series Windowing

The `window1d` function creates a sliding window over a 1D array of data. This is particularly useful for time series analysis and modeling tasks, allowing data to be split into overlapping or non-overlapping windows for processing.

#### Signature:
```python
def window1d(input_array: list | np.ndarray, size: int, shift: int = 1, stride: int = 1) -> list[list | np.ndarray]:
    ...
```

#### Usage:
```python
input_array = [1, 2, 3, 4, 5, 6]
window_size = 3
window_shift = 1
window_stride = 1
windows = window1d(input_array, window_size, window_shift, window_stride)
```

### 3. Cross-Correlation

The `convolution2d` function performs cross-correlation between a 2D input matrix and a kernel matrix. Although often referred to as convolution, in deep learning, it is essentially cross-correlation. This function is commonly used in convolutional neural networks (CNNs) for feature extraction.

#### Signature:
```python
def convolution2d(input_matrix: np.ndarray, kernel: np.ndarray, stride: int = 1) -> np.ndarray:
    ...
```

#### Usage:
```python
input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
kernel = np.array([[1, 0], [0, -1]])
stride = 1
output_matrix = convolution2d(input_matrix, kernel, stride)
```

## Project Structure

```
DataTransformation_library/
│
├── DataTransformation/
│   ├── __init__.py
│   ├── transpose.py
│   ├── window.py
│   └── convolution.py
│
├── tests/
│   ├── __init__.py
│   ├── test_transpose.py
│   ├── test_window.py
│   └── test_convolution.py
│
├── README.md
├── LICENSE
├── pyproject.toml
└── poetry.lock
```

## Installation

You can install the library via pip:

```
pip install DataTransformation-library
```

## Dependencies

- Python (>=3.6)
- NumPy (>=1.26.4)



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

