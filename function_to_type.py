#!/usr/bin/env python3
#
# function_to_type.py - By Steven Chen Hao Nyeo 
# The script that contains the algorithm for translating the cognitive functions to the personality types in the socionics type square 
# Created: January 2, 2019

class Translator: 
	def translate_orientation (entity):
		if (entity.values[0].sublabel == 'e'):
			return "E" 
		else: 
			return "I"
		
	def translate_observing (entity):
		if (Translator.translate_perception (entity) == 'j'):
			return entity.values[1].label
		else: 
			return entity.values[0].label
		
	def translate_decision_making (entity):
		if (Translator.translate_perception (entity) == 'j'):
			return entity.values[0].label
		else: 
			return entity.values[1].label
		
	def translate_perception (entity):
		if (entity.values[0].label == 'T' or entity.values[0].label == 'F'):
			return "j" 
		else: 
			return "p"
		