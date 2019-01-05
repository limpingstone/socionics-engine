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

e = Entity(Function.reverse_order(Fi, Se))

# Print the personality type of identity
print("Mirror: " + 
      Translator.translate_orientation(e) + 
      Translator.translate_observing(e) + 
      Translator.translate_decision_making(e) + 
      Translator.translate_perception(e))