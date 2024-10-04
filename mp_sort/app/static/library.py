from org.transcrypt.stubs.browser import *
from random import *

#python -m transcrypt -b -n library

def gen_random_int(number: int, seed: int) -> list[int]: #Wenmiao's code
    result = random.sample(range(0,100),10)
    random.seed(seed)
    random.shuffle (result)
    
    return result

def generate():	# Wenmiao's code
    number = 10
    seed = 200
    
    # call gen_random_int() with the given number and seed
    # store it to the variable array
    array = gen_random_int(number, seed)
    
    # convert the items into one single string 
    # the number should be separated by a comma
    # and a full stop should end the string.
    array_str = ""
    
    for i, element in enumerate(array):
        #trace the index of the last element in the list.
        #As long as it is not the last element, add comma.
        #else, add full stop.
        if i < (number-1):
            array_str += str(element) + ","
        else:
            array_str += str(element) + '.'
    # pass
    
    # This line is to placed the string into the HTML
    # under div section with the id called "generate"
    document.getElementById("generate").innerHTML = array_str

def sort1(array: list[int]) -> None: # annie's code
	n = len(array)
	swapped = True
	while swapped == True:
		swapped = False
		new_n = n
		for i in range(1,n):
			left = array[i-1]
			right = array[i]
			if left>right:
				array[i-1], array[i] = right, left
				swapped = True
				n = new_n


#def str_to_int(long_str: str) -> list[int]: # annie's code
#	str_ls: list[str] = long_str.split(",") # split the string with ","
#	int_ls: list[int] = [] # to be filled later
#	for str_ele in str_ls: # str_ele are individual string numbers
#		if str_ele != ".": # because "generate" has '.' and "number" may not (html id)
#			make_int = int(str_ele)
#			int_ls.append(make_int) # create the int list
#	return int_ls

#def array_to_str(int_ls: list[int]) -> str: # annie's code
#	final_str: str = '' # to be filled later
#	length_of_array = len(int_ls)
#	for i in range(length_of_array-1): # i are indexes (integers)
#		final_str += str(int_ls[i]) + ','
#	final_str += str(int_ls[-1]) # since final term shouldn't have "," behind
#	return final_str

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''

	# written code here - annie
	string = document.getElementById("generate").innerHTML
	array_str: str = string[:-1] # since last term has a fullstop AND doesn't get separated with the split by ","
	split_str: list[str] = array_str.split(",") # now we split the terms hee hee~
	array: list[int] = [] # to be filled with int and sorted later
	for i in split_str:
		#if i != ".":
		array.append(int(i)) # to make int array
	sort1(array) # should return None but sort array
	final_str = ""
	for i in range(len(array)): # i is an index, not an element
		final_str += str(array[i])
		if i != len(array)-1:
			final_str += ","
		else:
			final_str += "."
	#final_str += str(array[-1])
	document.getElementById("sorted").innerHTML = final_str

def sort2(array: list[int]) -> None: # varsh's code
	n = len(array)
	for big_idx in range(1,n):
		small_idx = big_idx
		temp = array[small_idx]
		while (small_idx > 0) and array[small_idx - 1] > temp:
			array[small_idx] = array[small_idx -1]
			small_idx -= 1
		array[small_idx] = temp 

def safe_eval(expression):
    try:
        return int(expression)									# Use eval to calculate the expression and convert to integer
    except (SyntaxError, ValueError, TypeError):
        window.alert("Please enter only numbers separated by commas.")		# If got error prompt user to enter correct values
        return None

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value
	
	# Throw alert and stop if nothing in the text input
	if value == "":												# If value(from HTML element with ID "numbers") is an empty string (textbox is empty)
		window.alert("Your textbox is empty")					# Prompt user that textbox is empty
		return

	# written code here - varsh
	value = value.replace(" ", "")								# Remove ALL whitespace
	str_array: list[string] = value.split()						# Split string, store into array
	
	
	int_array : list[int] = list(map(safe_eval, str_array))		# Try to convert all elements in array, from string to int datatype

	if None in int_array:										# Handle the case where safe_eval returned None for any element
		return													# Stop further execution if invalid input was detected

	sort2(int_array)											# Sort integer array (in place, no copy) using function sort2 (insertion sort algo) 
	array_str: str = ",".join(map(str, int_array))				# Convert integers back to strings and join with commas
	document.getElementById("sorted").innerHTML = array_str		# Display string onto HTML page at the element with ID "sorted"

