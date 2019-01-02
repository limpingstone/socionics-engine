#!/usr/bin/env python3
#
# run_test.py - By Steven Chen Hao Nyeo 
# The testing script for the cognitive function
# Created: January 1, 2019

from cognitive_function import *
from entity import Entity
from value import Value
from strength import Strength

e = Entity(Te, Ni, Se, Fi, Ti, Ne, Si, Fe)

Value.generate_order(e)
Value.generate_chart(e)

Strength.generate_chart(e)