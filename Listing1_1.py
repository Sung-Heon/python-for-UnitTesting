def IsStringLong(input : str):
  if len(input) > 5:
    return True
  return False


def Test():
  result = IsStringLong("abc")
  assert False == result
