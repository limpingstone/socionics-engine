#!/usr/bin/env python3
#
# function_analysis.py - By Steven Chen Hao Nyeo 
# The script containing the helper methods for identifying the personality roles in the type square from the cognitive functions
# Created: January 4, 2019

from cognitive_function import *

class Function: 
	
	# The function that returns the corresponding cognitive function (T - F / N - S)
	def get_opposite (function): 
		if (function.label + function.sublabel == "Ti"):
			return Fi
		elif (function.label + function.sublabel == "Fi"): 
			return Ti
		elif (function.label + function.sublabel == "Ni"):
			return Si
		elif (function.label + function.sublabel == "Si"):
			return Ni
		elif (function.label + function.sublabel == "Te"):
			return Fe
		elif (function.label + function.sublabel == "Fe"):
			return Te
		elif (function.label + function.sublabel == "Ne"):
			return Se
		elif (function.label + function.sublabel == "Se"):
			return Ne
		
	# The helper method that changes the sublabel from introverted to extroverted or vice versa (i - e) 
	def get_opposite_orientation (function): 
		if (function.label + function.sublabel == "Ti"):
			return Te
		elif (function.label + function.sublabel == "Fi"): 
			return Fe
		elif (function.label + function.sublabel == "Ni"):
			return Ne
		elif (function.label + function.sublabel == "Si"):
			return Se
		elif (function.label + function.sublabel == "Te"):
			return Ti
		elif (function.label + function.sublabel == "Fe"):
			return Fi
		elif (function.label + function.sublabel == "Ne"):
			return Ni
		elif (function.label + function.sublabel == "Se"):
			return Si
		
	# The helper method that reverse the order of the dominant and auxiliary cognitive functions 
	def reverse_order (*array):
		
		reversed_array = []
		for function in array: 	
			reversed_array.append(function)
		
		temp = reversed_array[0]
		reversed_array[0] = reversed_array[1]
		reversed_array[1] = temp
		return reversed_array
		