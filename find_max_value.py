def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    x = list(data.values())
    maxi=0
    for i in x:
        if i > maxi:
            maxi = i
    return maxi
nur={
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }
print(find_max_value(nur))