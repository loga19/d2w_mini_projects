

def mergesort(array, byfunc=None):
  pass

class Stack:
  def __init__(self, first=None):
    self.stackls = list()

  def push(self, thingy):
    self.stackls.append(thingy)

  def pop(self):
    if not self.is_empty:
      return self.stackls.pop()
    return None

  def peek(self):
    if not self.is_empty:
      return self.stackls[-1]
  pass

  @property
  def is_empty(self):
    return len(self.stackls) == 0

  @property
  def size(self):
    return len(self.stackls)

class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





