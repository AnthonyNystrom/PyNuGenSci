#!/usr/bin/env python
# -*- coding: utf-8 -*-

from System import *
from System.Collections.Generic import *
from System.Text import *

class FalsePositionRootFinder(RootFinder):
	def __init__(self, f, niter, pres):
		pass
	def __init__(self, f, niter, pres):
		pass
	def Find(self):
		x1 = m_xmin
		x2 = m_xmax
		fl = self.m_f(x1)
		fh = self.m_f(x2)
		if fl * fh > 0.0:
			raise RootFinderException(m_RootNotBracketed, 0, Range(x1, x2), 0.0)
		if fl < 0.0:
			xl = x1
			xh = x2
		else:
			xl = x2
			xh = x1
			self.Swap(, )
		dx = xh - xl
		iiter = 0
		while iiter < m_NbIterMax:
			rtf = xl + dx * fl / (fl - fh)
			f = self.m_f(rtf)
			if f < 0.0:
				del = xl - rtf
				xl = rtf
				fl = f
			else:
				del = xh - rtf
				xh = rtf
				fh = f
			dx = xh - xl
			if Math.Abs(del) < m_Accuracy or f == 0.0:
				return rtf
			iiter += 1
		raise RootFinderException(m_RootNotFound, iiter, Range(xl, xh), m_Accuracy)
