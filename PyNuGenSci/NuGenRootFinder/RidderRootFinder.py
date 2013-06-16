#!/usr/bin/env python
# -*- coding: utf-8 -*-

from System import *

class RidderRootFinder(RootFinder):
	def __init__(self, f, niter, pres):
		pass
	def __init__(self, f, niter, pres):
		pass
	def Find(self):
		# Vérifications d'usage
		if m_xmin >= m_xmax:
			raise RootFinderException(m_InvalidRange, 0, Range(m_xmin, m_xmax), 0.0) # Mauvaise plage de recherche
		ans = -1.11e30
		xh = m_xmax
		xl = m_xmin
		fl = self.m_f(m_xmin)
		fh = self.m_f(m_xmax)
		iiter = 0
		if self.Sign(fl) != self.Sign(fh):
			while iiter < m_NbIterMax:
				# Compute the mid point
				xm = 0.5 * (xl + xh)
				fm = self.m_f(xm)
				s = Math.Sqrt(fm * fm - fl * fh)
				if s == 0.0:
					return (ans)
				# Updating formula
				xnew = xm + (xm - xl) * ((1.0 if fl >= fh else -1.0) * fm / s)
				# Maybe the new value is the good one
				if Math.Abs(xnew - ans) <= m_Accuracy:
					return (ans)
				# Store this new point
				ans = xnew
				fnew = self.m_f(ans)
				if self.Sign(fm, fnew) != fm:
					xl = xm
					fl = fm
					xh = ans
					fh = fnew
				elif self.Sign(fl, fnew) != fl:
					xh = ans
					fh = fnew
				elif self.Sign(fh, fnew) != fh:
					xl = ans
					fl = fnew
				else:
					raise Exception()
				if Math.Abs(xh - xl) <= m_Accuracy:
					return (ans)
				iiter += 1
			raise RootFinderException(m_AccuracyNotReached, iiter, Range(m_xmin, m_xmax), Math.Abs(xh - xl))
		else: # nombre d'itérations autorisé dépassé
			if fl == 0.0:
				return (m_xmin)
			if fh == 0.0:
				return (m_xmax)
		raise RootFinderException(m_AccuracyNotReached, iiter, Range(m_xmin, m_xmax), Math.Abs(xh - xl))
