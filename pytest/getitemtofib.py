#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
class Fib():
    def __getitem__(self,n):
        if isinstance(n,int):
            a, b = 1, 1
            for  x in range(n):
                a, b = a, a + b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
#
