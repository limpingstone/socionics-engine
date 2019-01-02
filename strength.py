#!/usr/bin/env python3
#
# strength.py - By Steven Chen Hao Nyeo 
# The class that generates order of strength
# Created: January 1, 2019

class Strength: 
	def generate_order (entity):
		
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