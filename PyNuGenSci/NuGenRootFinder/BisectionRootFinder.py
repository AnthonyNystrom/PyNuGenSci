#!/usr/bin/env python
# -*- coding: utf-8 -*-

from System import *

class BisectionRootFinder(RootFinder):
	def __init__(self, f, niter, pres):
		pass
	def __init__(self, f, niter, pres):
		pass
	def Find(self):
		f = self.m_f(m_xmin)
		fmid = self.m_f(m_xmax)
		if m_xmin >= m_xmax or self.Sign(f) == self.Sign(fmid):
			raise RootFinderException(m_InvalidRange, 0, Range(m_xmin, m_xmax), 0.0)
		if f < 0.0:
			dx = m_xmax - m_xmin
			x = m_xmin
		else:
			dx = m_xmin - m_xmax
			x = m_xmax
		iiter = 0
		while iiter += 1 < m_NbIterMax:
			fmid = self.m_f(xmid = x + (dx *= 0.5))
			if fmid <= 0.0:
				x = xmid
			if Math.Abs(dx) < m_Accuracy or fmid == 0.0:
				return (x)
		# L'algorithme a dépassé le nombre d'itérations autorisé
		raise RootFinderException(m_AccuracyNotReached, iiter, Range(Math.Min(xmid, x), Math.Max(xmid, x)), Math.Abs(dx))
