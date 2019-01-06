#!/usr/bin/env python3
#
# run_test.py - By Steven Chen Hao Nyeo 
# The testing script for the cognitive function
# Created: January 1, 2019

from cognitive_function import *
from entity import Entity
from value import Value
from strength import Strength
from consciousness import Consciousness
from function_to_type import Translator
from function_analysis import *

# e = Entity(Te, Ni, Se, Fi, Ti, Ne, Si, Fe)
e = Entity([Fi, Se])

# Generate the charts for value, strength and consciousness
Value.generate_chart(e)
Strength.generate_chart(e)
Consciousness.generate_chart(e)

# Print the personality type according to the dominant and auxiliary functions 
print("Personality: " + 
      Translator.translate_orientation(e) + 
      Translator.translate_observing(e) + 
      Translator.translate_decision_making(e) + 
      Translator.translate_perception(e))

print("------------------------")

def print_personality (string, entity): 
	print(string + 
		Translator.translate_orientation(entity) + 
		Translator.translate_observing(entity) + 
		Translator.translate_decision_making(entity) + 
		Translator.translate_perception(entity))

# Print the personality type of identity
print_personality("Identity: ", e)

# Print the personality type of mirror
mirror = Function.reverse_order(e.values)
e_mirror = Entity(mirror)
print_personality("Mirror: ", e_mirror)

# Print the personality type of semi-duality
semi_duality = [e.values[0].opposite().opposite_orientation(), e.values[1].opposite()]
e_semi_duality = Entity(semi_duality)
print_personality("Semi-duality: ", e_semi_duality)

# Print the personality type of benefactor
benefactor = Function.reverse_order([e.values[0].opposite().opposite_orientation(), e.values[1].opposite()])
e_benefactor = Entity(benefactor)
print_personality("Benefactor: ", e_benefactor)

# Print the personality type of duality
duality = [e.values[0].opposite().opposite_orientation(), e.values[1].opposite().opposite_orientation()]
e_duality = Entity(duality)
print_personality("Duality: ", e_duality)