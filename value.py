#!/usr/bin/env python3
#
# value.py - By Steven Chen Hao Nyeo 
# The class containing functions that generate order of value
# Created: January 1, 2019

import sys

class Value: 
	def generate_order (entity):
		for value in entity.values:
			print(value.label, end=', ')
		print() # New line for last element
		
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
		for value in entity.values:
			print(value.label, end=' ')
		print() # New line for last element
		
		