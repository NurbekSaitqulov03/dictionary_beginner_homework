def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    x = 0
    y = 0
    for i in data:
        for w in i.values():
            if job == w:
                x+=1 
    return x
cholo = [
  {
    'name': 'John',
    'job': 'Barber'
  }, 
  {
    'name': 'Mary',
    'job': 'Developer'
  },
  {
    'name': 'Ann', 
    'job': 'Teacher'
  }
  ]
print(count_jobs(cholo, "Student"))