def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    a = data[0]
    b = list(a.values())
    m = b[0]
    n = b[-1]
    k = 0
    for i in data[1:]:
        k = list(i.values())
        if n > k[-1]:
            n = k[-1]
            m = k[0]
    return m
c = [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  },
  {
    'name': 'Ban', 
    'age': 29
  }
]
print(get_min_age_user_name(c))