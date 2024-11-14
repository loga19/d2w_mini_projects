def mergesort(array, byfunc=None):  # Wenmiao's code
    # Call the recursive function
    p = 0   # first index
    r = len(array) - 1   # last index
    mergesort_recursive(array, p, r, byfunc)

def mergesort_recursive(array, p, r, byfunc):
    if p < r:   #if there is more than 1 item in the sub array
        q = (p + r) // 2  # middle index
        mergesort_recursive(array, p, q, byfunc)  # merge sort the first half
        mergesort_recursive(array, q + 1, r, byfunc)  # merge sort the second half
        merge(array, p, q, r, byfunc)  # merge two sorted arrays

def merge(array, p, q, r, byfunc):
    left_array = array[p:q + 1]   # slice from p to q
    right_array = array[q + 1:r + 1]   # slice from q+1 to r
    
    # initialize indexes and size
    left_index = 0
    right_index = 0
    main_index = p

    left_array_size = len (left_array)
    right_array_size = len (right_array)

    # while compared items are within the range of the arrays
    while left_index < left_array_size and right_index < right_array_size:
        # if byfunc is provided
        if byfunc:
            # if left < right, put left item to main array
            if byfunc(left_array[left_index]) <= byfunc(right_array[right_index]):
                array[main_index] = left_array[left_index]
                left_index += 1  # move to the next item in left array
            else:
                array[main_index] = right_array[right_index]
                right_index += 1
            main_index += 1  # move to the next place in main array

        # if byfunc is not provided
        else:
            # if left < right, put left item to main array
            if left_array[left_index] <= right_array[right_index]:
                array[main_index] = left_array[left_index]
                left_index += 1  # move to the next item in left array
            else:
                array[main_index] = right_array[right_index]
                right_index += 1
            main_index += 1  # move to the next place in main array
    
    # if right array has no more item to compare:
    while left_index < left_array_size:
        array[main_index] = left_array[left_index]
        left_index += 1
        main_index += 1
    
    # if left array has no more item to compare:
    while right_index < right_array_size:
        array[main_index] = right_array[right_index]
        right_index += 1
        main_index += 1


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

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()

    for token in tokens:
            if token.isdigit():  # If the token is an operand (number)
                operand_stack.push(int(token))  # Push as integer
            elif token == '(':
                operator_stack.push(token)
            elif token == ')':
                # Process until we find '('
                while not operator_stack.is_empty and operator_stack.peek() != '(':
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.pop()  # Discard the '('
            elif token in '+-':
                # Process all operators on the top of the stack with higher or equal precedence
                while (not operator_stack.is_empty and operator_stack.peek() not in '()'):
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(token)
            elif token in '*/':
                # Process all '*' or '/' operators on the top of the stack
                while (not operator_stack.is_empty and operator_stack.peek() in '*/'):
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(token)

    # Phase 2: Process all remaining operators
    while not operator_stack.is_empty:
        self.process_operator(operand_stack, operator_stack)

    # Final result should be at the top of operand stack
    return operand_stack.pop()




def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





