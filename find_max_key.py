def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    x = list(data.keys())
    y = 0
    maxi=0
    for i in x:
        if i > maxi:
            maxi = i
    return maxi
nur = {
    1.4 :'a', 
    7.8 :'b', 
    4 : 'c'
  }
print(find_max_key(nur))