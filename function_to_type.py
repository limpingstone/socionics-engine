#!/usr/bin/env python3
#
# function_to_type.py - By Steven Chen Hao Nyeo 
# The script that contains the algorithm for translating the cognitive functions to the personality types in the socionics type square 
# Created: January 2, 2019

class Translator: 
	
	# Orientation (E / I) - first column of the personality type 
	# Dependent on the sublabel of the dominant function
	def translate_orientation (entity):
		if (entity.values[0].sublabel == 'e'):
			return "E" 
		else: 
			return "I"
	
	# Observing (N / S) - second column of the personality type 
	# If dominant function is N or S -> write the label of the dominant function to the column 
	# If dominant function is T or F -> write the label of the auxiliary function to the column 
	def translate_observing (entity):
		if (Translator.translate_perception (entity) == 'j'):
			return entity.values[1].label
		else: 
			return entity.values[0].label
	
	# Decision Making (T / F) - third column of the personality type 
	# If dominant function is T or F -> write the label of the dominant function to the column 
	# If dominant function is N or S -> write the label of the auxiliary function to the column 
	def translate_decision_making (entity):
		if (Translator.translate_perception (entity) == 'j'):
			return entity.values[0].label
		else: 
			return entity.values[1].label
		
	# Perception (j / p) - last column of the personality type
	# Dependent on the label of the dominant function 
	# If dominant function is T or F -> judging (j)
	# If dominant function is N or S -> perceiving (p)
	def translate_perception (entity):
		if (entity.values[0].label == 'T' or entity.values[0].label == 'F'):
			return "j" 
		else: 
			return "p"
		