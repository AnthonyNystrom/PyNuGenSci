#!/usr/bin/env python
# -*- coding: utf-8 -*-

from System import *

class SecantRootFinder(RootFinder):
	def __init__(self, f, niter, accuracy):
		pass
	def __init__(self, f, niter, accuracy):
		pass
	def Find(self):
		x1 = m_xmin
		x2 = m_xmax
		fl = self.m_f(x1)
		f = self.m_f(x2)
		if Math.Abs(fl) < Math.Abs(f):
			rts = x1
			xl = x2
			self.Swap(, )
		else:
			xl = x1
			rts = x2
		iiter = 0
		while iiter < m_NbIterMax:
			if f == fl:
				raise RootFinderException(m_InadequatedAlgorithm, iiter, Range(x1, x2), Math.Abs(x1 - x2))
			dx = (xl - rts) * f / (f - fl)
			xl = rts
			fl = f
			rts += dx
			f = self.m_f(rts)
			if Math.Abs(dx) < m_Accuracy or f == 0.0:
				return rts
			iiter += 1
		raise RootFinderException(m_RootNotFound, iiter, Range(xl, x2), m_Accuracy)
