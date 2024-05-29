import numpy
from numbers import Number


def transpose2d(input_matrix: list[list[Number]]) -> list:
    """
    Transpose a 2D list of numbers.

    Args:
        input_matrix (list[list[Number]]): 2D list of numbers to be transposed.

    Returns:
        list: Transposed 2D list.

    Examples:
        >>> transpose2d([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        
        >>> transpose2d([
            [1, 2],
            [3, 4],
            [5, 6]
        ])
        [
            [1, 3, 5],
            [2, 4, 6]
        ]
    """
    return [list(row) for row in zip(*input_matrix)]


def window1d(
    input_array: list | numpy.ndarray,
    size: int,
    shift: int = 1,
    stride: int = 1,
) -> list[list | numpy.ndarray]:
    """
    Generate sliding windows over a 1D array.

    Args:
        input_array (list or np.ndarray): Input 1D array of real numbers.
        size (int): Size of the window (length).
        shift (int, optional): Shift (step size) between different windows. Defaults to 1.
        stride (int, optional): Stride (step size) within each window. Defaults to 1.

    Returns:
        list of lists or np.ndarray: List of windows, where each window is a sub-array of the input array.
            If input_array is a list, the output is a list of lists.
            If input_array is a 1D NumPy array, the output is a list of 1D NumPy arrays.

    Raises:
        AssertionError: If input_array is not a list or a 1D NumPy array,
            if size, shift, or stride are not positive integers, or if input_array is an empty list.

    Examples:
        >>> input_array = [1, 2, 3, 4, 5]
        >>> window1d(input_array, size=3, shift=1, stride=1)
        [ [1, 2, 3], [2, 3, 4], [3, 4, 5] ]

        >>> input_array = np.array([1, 2, 3, 4, 5])
        >>> window1d(input_array, size=3, shift=2, stride=1)
        [ [1, 2, 3], [3, 4, 5] ]
    """
    if size > 0:
        raise ValueError("size is expected to be a positive integer")
    if shift > 0:
        raise ValueError("shift is expected to be a positive integer")
    if stride > 0:
        raise ValueError("stride is expected to be a positive integer")

    result = []

    for i in range(0, len(input_array) - (size+1), shift):
        window = input_array[i:i+size:stride]
        if isinstance(input_array, numpy.ndarray):
            window = numpy.ndarray(window)
        result.append(window)

    return result


def convolution2d(input_matrix: numpy.ndarray, kernel: numpy.ndarray, stride : int = 1) -> numpy.ndarray:
    """
    Apply a 2D convolution (cross-correlation) to the input matrix using the specified kernel and stride.
    
    Parameters:
        input_matrix (np.ndarray): A 2D Numpy array of real numbers representing the input matrix.
        kernel (np.ndarray): A 2D Numpy array of real numbers representing the kernel.
        stride (int): An integer representing the stride of the convolution. Default is 1.
    
    Returns:
        np.ndarray: A 2D Numpy array of real numbers representing the result of the convolution.
    
    Raises:
        ValueError: If the input_matrix or kernel are not 2D arrays, or if the stride is not a positive integer.
    
    Example:
        >>> input_matrix = np.array([[1, 2, 3], 
                                     [4, 5, 6], 
                                     [7, 8, 9]])
        >>> kernel = np.array([[1, 0], 
                               [0, -1]])
        >>> stride = 1
        >>> convolution2d(input_matrix, kernel, stride)
        array([[ 1.,  2.],
               [-2., -1.]])
    
        >>> input_matrix = np.array([[1, 2, 3, 0], 
                                     [4, 5, 6, 0], 
                                     [7, 8, 9, 0],
                                     [0, 0, 0, 0]])
        >>> kernel = np.array([[1, 0], 
                               [0, -1]])
        >>> stride = 2
        >>> convolution2d(input_matrix, kernel, stride)
        array([[ 1.,  3.],
               [-1., -9.]])
    """
    if not (isinstance(input_matrix, numpy.ndarray) and isinstance(kernel, numpy.ndarray)):
        raise ValueError("Both input_matrix and kernel must be of type np.ndarray.")

    if input_matrix.ndim != 2 or kernel.ndim != 2:
        raise ValueError("Both input_matrix and kernel must be 2D arrays.")

    if not isinstance(stride, int) or stride <= 0:
        raise ValueError("Stride must be a positive integer.")

    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    output_height = (input_height - kernel_height) // stride + 1
    output_width = (input_width - kernel_width) // stride + 1

    output_matrix = numpy.zeros((output_height, output_width))

    for i in range(0, output_height):
        for j in range(0, output_width):
            region = input_matrix[i*stride:i*stride+kernel_height, j*stride:j*stride+kernel_width]
            output_matrix[i, j] = numpy.sum(region * kernel)

    return output_matrix

