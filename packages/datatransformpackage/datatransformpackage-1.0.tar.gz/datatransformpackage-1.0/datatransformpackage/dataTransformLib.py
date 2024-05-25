import numpy as np
from typing import List, Union

#transpose
from typing import List, Union

def read_matrix_from_file(file_path: str) -> List[List[float]]:
    """
    Reads a matrix from a file where each line represents a row of the matrix
    and elements in the row are separated by spaces.

    Args:
        file_path (str): Path to the file containing the matrix data.

    Returns:
        List[List[float]]: 2D list representing the matrix.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If there is an issue with parsing floats from the file.
    """
    matrix = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                row = list(map(float, line.split()))
                matrix.append(row)
    except FileNotFoundError as e:
        print(f"Error: The file '{file_path}' was not found.")
        raise e
    except ValueError as e:
        print(f"Error: Could not convert data to float in file '{file_path}'.")
        raise e
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        raise e
    return matrix

def transpose2d(input_matrix: Union[List[List[float]], str]) -> List[List[float]]:
    """
    Transposes a 2D matrix.

    Args:
        input_matrix (Union[List[List[float]], str]): 2D list representing the matrix
            or a string representing the file path to the matrix data.

    Returns:
        List[List[float]]: Transposed 2D list.

    Raises:
        TypeError: If input_matrix is not a list of lists or a string.
        ValueError: If input_matrix is not a valid 2D list.
        AttributeError: If input_matrix is a list but does not have correct structure.
    """
    try:
        if isinstance(input_matrix, str):
            matrix = read_matrix_from_file(input_matrix)
        elif isinstance(input_matrix, list):
            if not all(isinstance(row, list) for row in input_matrix):
                raise ValueError("Input matrix must be a list of lists.")
            matrix = input_matrix
        else:
            raise TypeError("Input must be a list of lists or a file path (string).")
        
        # Ensure the input matrix is not empty
        if not matrix or not matrix[0]:
            return []

        # Transpose the matrix using list comprehension
        transposed_matrix = [
            [matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))
        ]
    
    except TypeError as e:
        print(f"TypeError: {e}")
        raise e
    except ValueError as e:
        print(f"ValueError: {e}")
        raise e
    except AttributeError as e:
        print(f"AttributeError: {e}")
        raise e
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise e

    return transposed_matrix



#Time Series windows
def window1d(input_array: Union[List[float], np.ndarray], size: int, shift: int = 1, stride: int = 1) -> List[Union[List[float], np.ndarray]]:
    """
    Generate overlapping windows from a 1D input array.

    Args:
        input_array (Union[List[float], np.ndarray]): Input array of real numbers.
        size (int): Size (length) of each window.
        shift (int, optional): Step size between the start of consecutive windows. Default is 1.
        stride (int, optional): Step size within each window. Default is 1.

    Returns:
        List[Union[List[float], np.ndarray]]: List of windows as lists or 1D Numpy arrays.
    """
    
    if not isinstance(input_array, (list, np.ndarray)):
        raise TypeError("input_array must be a list or numpy array")
    
    if not all(isinstance(x, (int, float)) for x in input_array):
        raise ValueError("input_array must contain only real numbers")
    
    if not (isinstance(size, int) and size > 0):
        raise ValueError("size must be a positive integer")
    
    if not (isinstance(shift, int) and shift > 0):
        raise ValueError("shift must be a positive integer")
    
    if not (isinstance(stride, int) and stride > 0):
        raise ValueError("stride must be a positive integer")
    
    input_length = len(input_array)
    windows = []

    for start in range(0, input_length - size + 1, shift):
        window = input_array[start:start + size:stride]
        windows.append(window if isinstance(input_array, list) else np.array(window))

    return windows



#Cross Correlation
def convolution2d(input_matrix: np.ndarray, kernel: np.ndarray, stride: int = 1) -> np.ndarray:
    # Ensure input and kernel are 2D arrays
    if input_matrix.ndim != 2 or kernel.ndim != 2:
        raise ValueError("Both input_matrix and kernel must be 2D arrays")
    
    # Get dimensions of input matrix and kernel
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape
    
    # Calculate the dimensions of the output matrix
    output_height = (input_height - kernel_height) // stride + 1
    output_width = (input_width - kernel_width) // stride + 1
    
    # Initialize the output matrix with zeros
    output_matrix = np.zeros((output_height, output_width))
    
    # Perform the convolution operation
    for i in range(0, output_height):
        for j in range(0, output_width):
            # Calculate the starting points of the current "slice" of the input matrix
            start_i = i * stride
            start_j = j * stride
            # Extract the slice from the input matrix
            input_slice = input_matrix[start_i:start_i + kernel_height, start_j:start_j + kernel_width]
            # Compute the dot product and assign it to the output matrix
            output_matrix[i, j] = np.sum(input_slice * kernel)
    
    return output_matrix