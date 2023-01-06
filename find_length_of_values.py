def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    x = list(data.values())
    y = 0
    for i in x:
        y+=len(i)
    return y
aba = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }
print(find_length_of_values(aba))