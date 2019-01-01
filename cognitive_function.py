#!/usr/bin/env python3
#
# cognitive_function.py - By Steven Chen Hao Nyeo 
# The script that creates the eight cognitive functions in socionics
# Created: January 1, 2019

class CognitiveFunction: 
	def __init__ (self, label, description):
		self.label = label
		self.description = description
		
Ni = CognitiveFunction("Introveted Intuition", "")	
Ne = CognitiveFunction("Extroverted Intuition", "")
Ti = CognitiveFunction("Introveted Thinking", "")
Te = CognitiveFunction("Extroverted Thinking", "")
Si = CognitiveFunction("Introveted Sensing", "")
Se = CognitiveFunction("Extroverted Sensing", "")
Fi = CognitiveFunction("Introveted Ethics", "")
Fe = CognitiveFunction("Extroverted Ethics", "")

