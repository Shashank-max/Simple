import numpy as np

def extract_subpart(arr, center, shape, fill=0):
    """
    Extracts a subpart from an array with a fixed shape centered on a given element.
    
    Parameters:
        arr (numpy.ndarray): The input array.
        center (tuple): The coordinates of the center element (row, column).
        shape (tuple): The shape of the subpart to extract (rows, columns).
        fill (int or float, optional): The value used for padding when necessary. Defaults to 0.
    
    Returns:
        numpy.ndarray: The extracted subpart.
    """
    rows, cols = arr.shape
    center_row, center_col = center
    subpart_rows, subpart_cols = shape
    
    start_row = max(center_row - subpart_rows // 2, 0)
    end_row = min(center_row + subpart_rows // 2 + 1, rows)
    start_col = max(center_col - subpart_cols // 2, 0)
    end_col = min(center_col + subpart_cols // 2 + 1, cols)
    
    subpart = np.full(shape, fill)
    subpart_start_row = subpart_rows // 2 - (center_row - start_row)
    subpart_end_row = subpart_start_row + (end_row - start_row)
    subpart_start_col = subpart_cols // 2 - (center_col - start_col)
    subpart_end_col = subpart_start_col + (end_col - start_col)
    
    subpart[subpart_start_row:subpart_end_row, subpart_start_col:subpart_end_col] = arr[start_row:end_row, start_col:end_col]
    
    return subpart

# Example usage:
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]])

center_element = (2, 2)
subpart_shape = (3, 3)
fill_value = 0

result = extract_subpart(arr, center_element, subpart_shape, fill_value)
print(result)