from org.transcrypt.stubs.browser import *
import random


def gen_random_int(number: int, seed: int) -> list[int]: #Wenmiao's code
    result = list(range(number))
    random.seed(seed)
    random.shuffle (result)
    
    return result

def generate(): #Wenmiao's code
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	
	array = gen_random_int(number, seed)
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str = ""
	n = len(array)
	for i, element in enumerate(array):
		array_str = array_str + str(element)
		#trace the index of the last element in the list.
		#As long as it is not the last element, add comma.
		#else, add full stop.
		if i < n-1:
			array_str = array_str + ","
		else:
			array_str = array_str + "."


		

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


def str_to_int(long_str: str) -> list[int]: # annie's code
	str_ls: list[str] = long_str.split(",") # split the string with ","
	int_ls: list[int] = [] # to be filled later
	for str_ele in str_ls: # str_ele are individual string numbers
		if str_ele != ".": # because "generate" has '.' and "number" may not (html id)
			make_int = int(str_ele)
			int_ls.append(make_int) # create the int list
		return int_ls

def array_to_str(int_ls: list[int]) -> str: # annie's code
	final_str: str = '' # to be filled later
	length_of_array = len(int_ls)
	for i in range(length_of_array-1): # i are indexes (integers)
		final_str += str(int_ls[i]) + ','
	final_str += str(int_ls[-1]) # since final term shouldn't have "," behind
	return final_str

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
	gotten_str = document.getElementById("generate").innerHTML
	
	gotten_str_to_array : list[int] = str_to_int(gotten_str) # returns list[int]

	sort1(gotten_str_to_array) # returns nothing, just sorts list

	array_str: str = array_to_str(gotten_str_to_array)

	document.getElementById("sorted").innerHTML = array_str

def sort2(array: list[int]) -> None: # varsh's code
	n = len(array)
	for big_idx in range(1,n):
		small_idx = big_idx
		temp = array[small_idx]
		while (small_idx > 0) and array[small_idx - 1] > temp:
			array[small_idx] = array[small_idx -1]
			small_idx -= 1
		array[small_idx] = temp 

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
	print(value)
	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# written code here - varsh
	value_array : list[int] = value.split(',')
	sort2(value_array)
	array_str: str = ",".join(value_array)
	document.getElementById("sorted").innerHTML = array_str


