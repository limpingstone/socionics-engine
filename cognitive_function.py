#!/usr/bin/env python3
#
# cognitive_function.py - By Steven Chen Hao Nyeo 
# The script that creates the eight cognitive functions in socionics
# Created: January 1, 2019

# Label - F or T or N or S 
# Sublabel - i or e
class CognitiveFunction: 
	def __init__ (self, label, name, description):
		self.label = label[0]
		self.sublabel = label[1]
		self.name = name
		self.description = description
		
	# The function that returns the corresponding cognitive function (T - F / N - S)
	def opposite_orientation (self): 
		if (self.label + self.sublabel == "Ti"):
			return Fi
		elif (self.label + self.sublabel == "Fi"): 
			return Ti
		elif (self.label + self.sublabel == "Ni"):
			return Si
		elif (self.label + self.sublabel == "Si"):
			return Ni
		elif (self.label + self.sublabel == "Te"):
			return Fe
		elif (self.label + self.sublabel == "Fe"):
			return Te
		elif (self.label + self.sublabel == "Ne"):
			return Se
		elif (self.label + self.sublabel == "Se"):
			return Ne
		
	# The helper method that changes the sublabel from introverted to extroverted or vice versa (i - e)
	def opposite (self): 
		if (self.label + self.sublabel == "Ti"):
			return Te
		elif (self.label + self.sublabel == "Fi"): 
			return Fe
		elif (self.label + self.sublabel == "Ni"):
			return Ne
		elif (self.label + self.sublabel == "Si"):
			return Se
		elif (self.label + self.sublabel == "Te"):
			return Ti
		elif (self.label + self.sublabel == "Fe"):
			return Fi
		elif (self.label + self.sublabel == "Ne"):
			return Ni
		elif (self.label + self.sublabel == "Se"):
			return Si
		
Ni = CognitiveFunction("Ni", "Introveted Intuition", "development over time, historicity, cause and effect, consequences, repetition, archetypal themes and examples, looking for causes in history or the past, past-future forecasting of event dynamics, rhythm, delay or act-now, past-turned imagination ")	

Ne = CognitiveFunction("Ne", "Extroverted Intuition", "potential, permutation, isomorphism, semblance, essence, uncertainty, the unknown, opening up new \"windows\" and bringing up new possibilities in conversation, seeing opportunities, chance, being the first, refreshing informational suddenness, diversity of interests and involvements")

Ti = CognitiveFunction("Ti", "Introveted Thinking", "structure, analysis, coherence, consistency, cogency, accordance, match, commensurability, understanding, order, or the lack of thereof")

Te = CognitiveFunction("Te", "Extroverted Thinking", "efficiency, method, mechanism, knowledge, work, reason in motion, direction of activity into its most logical course of action, \"logic of actions\", utilitarianism, expediency, benefit ")

Si = CognitiveFunction("Si", "Introveted Sensing", "homeostasis, continuity, smoothness, flow, satisfaction, aesthetics, quality of life, pleasure, relaxation, convenience, quality ")

Se = CognitiveFunction("Se", "Extroverted Sensing", "sensing of immediate static qualities of objects, sensing of immediate reality, external appearance, texture, form, static objects, impact, direct physical effect, span, extent, scope ")

Fi = CognitiveFunction("Fi", "Introveted Ethics", "internal harmony, resonance or dissonance of personal sentiments, sympathy, pity, compassion, support, condemnation, judgement, positive and negative emotional space ")

Fe = CognitiveFunction("Fe", "Extroverted Ethics", "emotional atmosphere, romanticism, cooperation, treatment, qualitative judgement of behavior, sympathy, ethical estimations of observable actions, \"ethics of actions\" ")

