#!/usr/bin/env python
# -*- coding: utf-8 -*-

from System import *
from System.Collections.Generic import *
from System.Text import *

class Range(object):
	def __init__(self, min, max):
		self._Min = min
		self._Max = max

class RootFinderException(Exception):
	def __init__(self, message, iteration, range, accuracy):
		self._m_Iteration = iteration
		self._m_Range = range
		self._m_Accuracy = accuracy

	def get_Iteration(self):
		return self._m_Iteration

	def set_Iteration(self, value):
		self._m_Iteration = value

	Iteration = property(fget=get_Iteration, fset=set_Iteration)

	def get_Range(self):
		return self._m_Range

	def set_Range(self, value):
		self._m_Range = value

	Range = property(fget=get_Range, fset=set_Range)

	def get_Accuracy(self):
		return self._m_Accuracy

	def set_Accuracy(self, value):
		self._m_Accuracy = value

	Accuracy = property(fget=get_Accuracy, fset=set_Accuracy)
