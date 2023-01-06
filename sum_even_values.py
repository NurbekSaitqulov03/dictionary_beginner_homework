def sum_even_values(data: dict) -> int:
    '''
    Return the sum of all even values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all even values in the dictionary
    '''
    x = list(data.values())
    y = 0
    for i in x:
        if i%2==0:
            y+=i
    return y
ak = {
    1: 22, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  }
print(sum_even_values(ak))