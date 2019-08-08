#!/usr/bin/env python3
#
# strength.py - By Steven Chen Hao Nyeo 
# The class containing functions that generate order of strength
# Created: January 1, 2019

class Strength: 
	# The helper method that generates the order of strength 
	def generate_order (entity):
		strengths = []
		
		# Rearrange the order of value into order of strength
		strengths.append(entity.values[0])
		strengths.append(entity.values[5])
		strengths.append(entity.values[1])
		strengths.append(entity.values[4])
		strengths.append(entity.values[2])
		strengths.append(entity.values[7])
		strengths.append(entity.values[3])
		strengths.append(entity.values[6])
		
		# Return the result for the chart 
		return strengths
		
	# The function that generates the chart showing the order of strength
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
		for strength in Strength.generate_order (entity):
			print(strength.label + strength.sublabel, end=' ')
		print() # New line for last element
		