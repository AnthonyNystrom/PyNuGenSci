#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import *

class RootFinder(object):
	def __init__(self, f, niter, acc):
		""" <summary>Constructor.</summary>
		 <param name="f">A continuous function.</param>
		"""
		self._m_InvalidRange = "Invalid range while finding root"
		self._m_AccuracyNotReached = "The accuracy couldn't be reached with the specified number of iterations"
		self._m_RootNotFound = "The algorithm ended without root in the range"
		self._m_RootNotBracketed = "The algorithm could not start because the root seemed not to be bracketed"
		self._m_InadequatedAlgorithm = "This algorithm is not able to solve this equation"
		self._double_Accuracy = 9.99200722162641E-16
		self._m_NbIterDefaultMax = 30
		self._m_DefaultAccuracy = 1.0E-04
		self._m_BracketingFactor = 1.6
		self._m_f = f
		self._m_NbIterMax = niter
		self._m_Accuracy = acc

	def __init__(self, f, niter, acc):
		self._m_InvalidRange = "Invalid range while finding root"
		self._m_AccuracyNotReached = "The accuracy couldn't be reached with the specified number of iterations"
		self._m_RootNotFound = "The algorithm ended without root in the range"
		self._m_RootNotBracketed = "The algorithm could not start because the root seemed not to be bracketed"
		self._m_InadequatedAlgorithm = "This algorithm is not able to solve this equation"
		self._double_Accuracy = 9.99200722162641E-16
		self._m_NbIterDefaultMax = 30
		self._m_DefaultAccuracy = 1.0E-04
		self._m_BracketingFactor = 1.6
		self._m_f = f
		self._m_NbIterMax = niter
		self._m_Accuracy = acc

	def get_BracketingFactor(self):
		return self._m_BracketingFactor

	def set_BracketingFactor(self, value):
		if value <= 0.0:
			raise ArgumentOutOfRangeException()
		self._m_BracketingFactor = value

	BracketingFactor = property(fget=get_BracketingFactor, fset=set_BracketingFactor)

	def set_Iterations(self, value):
		if value <= 0:
			raise ArgumentOutOfRangeException()
		self._m_NbIterMax = value

	Iterations = property(fset=set_Iterations)

	def get_Accuracy(self):
		return self._m_Accuracy

	def set_Accuracy(self, value):
		self._m_Accuracy = value

	Accuracy = property(fget=get_Accuracy, fset=set_Accuracy)

	def SearchBracketsOutward(self, xmin, xmax, factor):
		""" <summary>Detect a range containing at least one root.</summary>
		 <param name="xmin">Lower value of the range.</param>
		 <param name="xmax">Upper value of the range</param>
		 <param name="factor">The growing factor of research. Usually 1.6.</param>
		 <returns>True if the bracketing operation succeeded, else otherwise.</returns>
		 <remarks>This iterative methods stops when two values with opposite signs are found.</remarks>
		"""
		# Check the range
		if xmin >= xmax:
			raise RootFinderException(self._m_InvalidRange, 0, Range(xmin, xmax), 0.0)
		fmin = self.m_f(xmin)
		fmax = self.m_f(xmax)
		iiter = 0
		while iiter += 1 < self._m_NbIterMax:
			if self.Sign(fmin) != self.Sign(fmax):
				return (True)
			if Math.Abs(fmin) < Math.Abs(fmax):
				fmin = self.m_f(xmin += factor * (xmin - xmax))
			else:
				fmax = self.m_f(xmax += factor * (xmax - xmin))
		raise RootFinderException(self._m_RootNotFound, iiter, Range(fmin, fmax), 0.0)

	def Solve(self, x1, x2, bracket):
		""" <summary>Prototype algorithm for solving the equation f(x)=0.</summary>
		 <param name="x1">The low value of the range where the root is supposed to be.</param>
		 <param name="x2">The high value of the range where the root is supposed to be.</param>
		 <param name="bracket">Determines whether a bracketing operation is required.</param>
		 <returns>Returns the root with the specified accuracy.</returns>
		"""
		if bracket:
			self.SearchBracketsOutward(, , self._m_BracketingFactor)
		self._m_xmin = x1
		self._m_xmax = x2
		return self.Find()

	def Solve(self, x1, x2, y, bracket):
		""" <summary>Prototype algorithm for solving the equation f(x)=y.</summary>
		 <param name="x1">The low value of the range where the root is supposed to be.</param>
		 <param name="x2">The high value of the range where the root is supposed to be.</param>
		 <param name="y"></param>
		 <param name="bracket">Determines whether a bracketing operation is required.</param>
		 <returns>Returns the root with the specified accuracy.</returns>
		"""
		self._m_Of = self._m_f
		self._m_f = UnaryFunctions.Substract(self._m_Of, UnaryFunctions.Constant(y))
		x = self.Solve(x1, x2, bracket)
		self._m_f = self._m_Of
		self._m_Of = None
		return x

	def Find(self):
		pass

	def Swap(self, x, y):
		t = x
		x = y
		y = t

	def Sign(self, a, b):
		""" <summary>Helper method useful for preventing rounding errors.</summary>
		 <returns>a*sign(b)</returns>
		"""
		return (a if a >= 0 else -a) if b >= 0 else (-a if a >= 0 else a)

	def Sign(x):
		return 1.0 if x > 0 else -1.0

	Sign = staticmethod(Sign)
