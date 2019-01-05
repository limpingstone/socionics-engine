#!/usr/bin/env python3
#
# function_analysis.py - By Steven Chen Hao Nyeo 
# The script containing the helper methods for identifying the personality roles in the type square from the cognitive functions
# Created: January 4, 2019

from cognitive_function import *

class Function: 
		
	# The helper method that reverse the order of the dominant and auxiliary cognitive functions 
	def reverse_order (array):
		
		reversed_array = []
		for function in array: 	
			reversed_array.append(function)
		
		temp = reversed_array[0]
		reversed_array[0] = reversed_array[1]
		reversed_array[1] = temp
		return reversed_array
		