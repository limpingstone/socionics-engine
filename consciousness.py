#!/usr/bin/env python3
#
# consciousness.py - By Steven Chen Hao Nyeo 
# The class containing functions that generate order of consciousness
# Created: January 1, 2019

class Consciousness: 
	def generate_order (entity):
		
		conscious_order = []
		
		# Rearrange the order of value into strength
		conscious_order.append(entity.values[0])
		conscious_order.append(entity.values[1])
		conscious_order.append(entity.values[7])
		conscious_order.append(entity.values[6])
		conscious_order.append(entity.values[3])
		conscious_order.append(entity.values[2])
		conscious_order.append(entity.values[4])
		conscious_order.append(entity.values[5])
		
		return conscious_order
	
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
			print(conscious.label, end=' ')
		print() # New line for last element
			