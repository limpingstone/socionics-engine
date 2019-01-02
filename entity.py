#!/usr/bin/env python3
#
# entity.py - By Steven Chen Hao Nyeo 
# The class that creates an individual object storing the order of value of the cognitive functions
# Created: January 1, 2019

class Entity: 
	def __init__ (self, *functions): 
		self.values = []
		for function in functions: 
			self.values.append(function)
		# for value in values:
		# 	print(value.label)