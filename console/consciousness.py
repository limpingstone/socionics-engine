#!/usr/bin/env python3
#
# consciousness.py - By Steven Chen Hao Nyeo 
# The class containing functions that generate order of consciousness
# Created: January 1, 2019

class Consciousness: 
	# The helper method that generates the order of consciousness 
	def generate_order (entity):
		conscious_order = []
		
		# Rearrange the order of value into order of consciousness
		conscious_order.append(entity.values[0])
		conscious_order.append(entity.values[1])
		conscious_order.append(entity.values[7])
		conscious_order.append(entity.values[6])
		conscious_order.append(entity.values[3])
		conscious_order.append(entity.values[2])
		conscious_order.append(entity.values[4])
		conscious_order.append(entity.values[5])
		
		# Return the result for the chart 
		return conscious_order
	
	# The function that generates the chart showing the order of consciousness
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
		for conscious in Consciousness.generate_order (entity):
			print(conscious.label + conscious.sublabel, end=' ')
		print() # New line for last element
			