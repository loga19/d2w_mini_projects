

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
  valid_char = '0123456789+-*/() '

  def __init__(self, string=""):
    # Assign memory to store expression
    self._expr = ''
    # Call the setter to validate and set the expression
    self.expression = string
    pass

  @property
  def expression(self):
    return self._expr
    pass

  @expression.setter
  def expression(self, new_expr):
    # Check if new_expr contains only valid character
    if all(char in self.valid_char for char in new_expr):
      # Set to new expression if valid
      self._expr = new_expr
    else:
      # Set to empty string if invalid characters found
      self._expr = ""
    pass

  def insert_space(self):
    # Insert space around operators and parenthesis
    spaced_expr = ""
    for char in self._expr:
      if char in "+-*/()":
        spaced_expr += f" {char} "  # Add spaces around operators and parentheses
      else:
        spaced_expr += char
    return spaced_expr  # Return as-is to preserve spaces around consecutive operators
    pass

  def process_operator(self, operand_stack, operator_stack):
    # Pop operator and operands
    operator = operator_stack.pop()
    right_operand = operand_stack.pop()
    left_operand = operand_stack.pop()
    
    # Perform the operation based on the operator
    if operator == '+':
      result = left_operand + right_operand
    elif operator == '-':
      result = left_operand - right_operand
    elif operator == '*':
      result = left_operand * right_operand
    elif operator == '/':
      # Perform integer division
      result = left_operand // right_operand
    
    # Push the result back onto the operand stack
    operand_stack.push(result)
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





