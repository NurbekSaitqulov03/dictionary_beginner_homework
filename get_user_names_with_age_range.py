def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    a = []
    x = 0
    for i in data:
        x = list(i.values())
        if x[-1] >= min_age and x[-1] <= max_age:
            a.append(x[0])
    return a
ac = [
  {
    'name': 'Anny', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 30
  }
]
print(get_user_names_with_age_range(ac, 20, 30))