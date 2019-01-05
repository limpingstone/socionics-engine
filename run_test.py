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

# Print the personality type of identity
print("Identity: " + 
      Translator.translate_orientation(e) + 
      Translator.translate_observing(e) + 
      Translator.translate_decision_making(e) + 
      Translator.translate_perception(e))

# Print the personality type of duality
duality = [e.values[0].opposite().opposite_orientation(), e.values[1].opposite().opposite_orientation()]
e_duality = Entity(duality)
print("Duality: " + 
      Translator.translate_orientation(e_duality) + 
      Translator.translate_observing(e_duality) + 
      Translator.translate_decision_making(e_duality) + 
      Translator.translate_perception(e_duality))

# Print the personality type of semi-duality
semi_duality = [e.values[0].opposite().opposite_orientation(), e.values[1].opposite()]
print(str(dom.label + dom.sublabel) + ", " + str(aux.label + aux.sublabel))
e_semi_duality = Entity(semi_duality)
print("Semi-duality: " + 
      Translator.translate_orientation(e_semi_duality) + 
      Translator.translate_observing(e_semi_duality) + 
      Translator.translate_decision_making(e_semi_duality) + 
      Translator.translate_perception(e_semi_duality))


# Print the personality type of mirror
mirror = Function.reverse_order(e.values)
e_mirror = Entity(mirror)
print("Mirror: " + 
      Translator.translate_orientation(e_mirror) + 
      Translator.translate_observing(e_mirror) + 
      Translator.translate_decision_making(e_mirror) + 
      Translator.translate_perception(e_mirror))