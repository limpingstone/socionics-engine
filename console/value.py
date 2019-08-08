#!/usr/bin/env python3
#
# value.py - By Steven Chen Hao Nyeo 
# The class containing functions that generate order of value
# Created: January 1, 2019

class Value: 
	# The helper method that generates the order of value 
	# The function directly returns the array as default
	def generate_order (entity):
		return entity.values
		
		# for value in entity.values:
		# 	print(value.label, end=', ')
		# print() # New line for last element
		
	# The function that generates the chart showing the order of value
	def generate_chart (entity):
		print("| 8  # ")
		print("| 7  #  # ")
		print("| 6  #  #  # ")
		print("| 5  #  #  #  # ")
		print("| 4  #  #  #  #  # ")
		print("| 3  #  #  #  #  #  # ")
		print("| 2  #  #  #  #  #  #  # ")
		print("| 1  #  #  #  #  #  #  #  # ")
		print(" --------------------------\n    ", end='')
		for value in Value.generate_order (entity):
			print(value.label + value.sublabel, end=' ')
		print() # New line for last element
			