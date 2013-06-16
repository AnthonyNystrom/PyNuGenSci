#!/usr/bin/env python
# -*- coding: utf-8 -*-

from System import *

class NewtonRootFinder(RootFinder):
	def __init__(self, f, df, niter, pres):
		self._m_df = df

	def __init__(self, f, df, niter, pres):
		self._m_df = df

	def Find(self):
		dx = 0.0
		h = 1.0e-5
		xacc = 1.0e-5
		if m_xmin >= m_xmax:
			raise ArgumentException("Mauvaise plage de recherche")
		x = 0.5 * (m_xmin + m_xmax)
		iiter = 0
		while iiter < m_NbIterMax:
			dx = self.m_f(x) / self.m_df(x)
			x -= dx
			if self.Sign(m_xmin - x) != self.Sign(x - m_xmax):
				raise RootFinderException(m_InvalidRange, iiter, Range(x, x + dx), Math.Abs(dx))
			if Math.Abs(dx) < xacc:
				return x
			iiter += 1
		# L'algorithme a dépassé le nombre d'itérations autorisé
		raise RootFinderException(m_InvalidRange, iiter, Range(x, x + dx), Math.Abs(dx))
