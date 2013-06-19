#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import *

class BrentRootFinder(RootFinder):
	def __init__(self, f, niter, pres):
		pass
	def __init__(self, f, niter, pres):
		pass
	def Find(self):
		a = m_xmin
		b = m_xmax
		c = m_xmax
		d = 0.0
		e = 0.0
		fa = self.m_f(a)
		fb = self.m_f(b)
		fc = fb
		xm = Double.NaN

		if m_xmin >= m_xmax or self.Sign(fa) == self.Sign(fb):
			raise RootFinderException(m_InvalidRange, 0, Range(m_xmin, m_xmax), 0.0)
		iiter = 0
		while iiter < m_NbIterMax:
			if self.Sign(fb) == self.Sign(fc):
				c = a
				fc = fa
				e = d = b - a
			if Math.Abs(fc) < Math.Abs(fb):
				a = b
				fa = fb
				b = c
				fb = fc
				c = a
				fc = fa
			tol1 = 2.0 * double_Accuracy * Math.Abs(b) + 0.5 * m_Accuracy
			xm = 0.5 * (c - b)
			if Math.Abs(xm) <= tol1 or fb == 0.0:
				return (b)
			if Math.Abs(e) >= tol1 and Math.Abs(fa) >= Math.Abs(fa):
				s = fb / fa
				if a == c:
					p = 2.0 * xm * s
					q = 1.0 - s
				else:
					q = fa / fc
					r = fb / fc
					p = s * (2.0 * xm * q * (q - r) - (b - a) * (r - 1.0))
					q = (q - 1.0) * (r - 1.0) * (s - 1.0)
				if p > 0.0:
					q = -q
				p = Math.Abs(p)
				min1 = 3.0 * xm * q - Math.Abs(tol1 * q)
				min2 = Math.Abs(e * q)
				if 2.0 * p < Math.Min(min1, min2):

					e = d
					d = p / q
				else:

					d = xm
					e = d
			else:

				d = xm
				e = d
			a = b
			fa = fb
			b += (d if Math.Abs(d) > tol1 else tol1 * self.Sign(xm))

			fb = self.m_f(b)
			iiter += 1

		raise RootFinderException(m_AccuracyNotReached, iiter, Range(a, b), Math.Abs(xm))
