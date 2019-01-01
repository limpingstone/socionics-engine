#!/usr/bin/env python3
#
# entity.py - By Steven Chen Hao Nyeo 
# The class that creates an individual object storing the order of value of the cognitive functions
# Created: January 1, 2019

class Entity: 
	def __init__ (self, *functions): 
		values = []
		for function in functions: 
			values.append(function)
		for value in values:
			print(value.label)