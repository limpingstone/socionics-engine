#!/usr/bin/env python3
#
# entity.py - By Steven Chen Hao Nyeo 
# The class that creates an individual object storing the order of value of the cognitive functions
# Created: January 1, 2019

from cognitive_function import *

# Rules of generating the list of Jungian cognitive functions: 
# The order of sublabels are either [e, i, e, i, e, i, e, i] or [i, e, i, e, i, e, i, e]
# The order of labels for the shadowing functions (last four) corresponds to the primary functions (first four) 
# The dominant and inferior functions are opposites (either a pair of N / S or T / F)
# The auxiliary and tertiary functions are opposites (either a pair of N / S or T / F)

class Entity: 
	def __init__ (self, *functions): 
		
		self.values = []
		for function in functions: 
			self.values.append(function)
		
		# The auxiliary and tertiary functions - opposites
		if (self.values[1].label == 'S'):
			if (self.values[1].sublabel == 'e'):
				self.values.append(Ni)
			else:
				self.values.append(Ne)
		elif (self.values[1].label == 'N'): 
			if (self.values[1].sublabel == 'e'):
				self.values.append(Si)
			else:
				self.values.append(Se)
		elif (self.values[1].label == 'F'): 
			if (self.values[1].sublabel == 'e'):
				self.values.append(Ti)
			else:
				self.values.append(Te)
		elif (self.values[1].label == 'T'): 
			if (self.values[1].sublabel == 'e'):
				self.values.append(Fi)
			else:
				self.values.append(Fe)
		
		# The dominant and inferior functions - opposites
		if (self.values[0].label == 'S'):
			if (self.values[0].sublabel == 'e'):
				self.values.append(Ni)
			else:
				self.values.append(Ne)
		elif (self.values[0].label == 'N'):
			if (self.values[0].sublabel == 'e'):
				self.values.append(Si)
			else:
				self.values.append(Se)
		elif (self.values[0].label == 'F'):
			if (self.values[0].sublabel == 'e'):
				self.values.append(Ti)
			else:
				self.values.append(Te)
		elif (self.values[0].label == 'T'):
			if (self.values[0].sublabel == 'e'):
				self.values.append(Fi)
			else:
				self.values.append(Fe)
		
		# The remaining ignoring, demonstrative, PoLR and role functions
		# They have the same order of labels as the first four functions, yet the orientation is reversed
		for i in range(4): 
			if (self.values[i].label == 'S'):
				if (self.values[i].sublabel == 'e'):
					self.values.append(Si)
				else:
					self.values.append(Se)
			elif (self.values[i].label == 'N'):
				if (self.values[i].sublabel == 'e'):
					self.values.append(Ni)
				else:
					self.values.append(Ne)
			elif (self.values[i].label == 'F'):
				if (self.values[i].sublabel == 'e'):
					self.values.append(Fi)
				else:
					self.values.append(Fe)
			elif (self.values[i].label == 'T'):
				if (self.values[i].sublabel == 'e'):
					self.values.append(Ti)
				else:
					self.values.append(Te)
		
		# self.values = []
		# for function in functions: 
		# 	self.values.append(function)
		
		# for value in values:
		# 	print(value.label)