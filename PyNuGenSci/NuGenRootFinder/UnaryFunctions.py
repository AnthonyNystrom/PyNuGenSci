#!/usr/bin/env python
# -*- coding: utf-8 -*-

from System import *

class IUnaryFunction(object):
	def Eval(self, x):
		pass

class UnaryFunctions(object):
	def Identity():
		return UnaryFunction()

	Identity = staticmethod(Identity)

	def Constant(a):
		return UnaryFunction()

	Constant = staticmethod(Constant)

	def Add(f1, f2):
		return UnaryFunction()

	Add = staticmethod(Add)

	def Multiply(f, lambda):
		return UnaryFunction()

	Multiply = staticmethod(Multiply)

	def Minus(f):
		return UnaryFunction()

	Minus = staticmethod(Minus)

	def Substract(f1, f2):
		return UnaryFunction()

	Substract = staticmethod(Substract)

	def Compound(f1, f2):
		return UnaryFunction()

	Compound = staticmethod(Compound)
