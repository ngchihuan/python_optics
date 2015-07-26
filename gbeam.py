from __future__ import division # without this, python 2.x will understand 1/2 as 0.0s
import numpy as np
pi=3.145

class gbeam:
	def __init__(self,waist,lamda,R1):
		self.waist=waist
		self.R1=R1#1R is 1/R
		self.lamda=lamda
		self.q1=complex(self.R1,(self.lamda/pi/self.waist**2))
#1/q is denoted as 1q

#q1=R1-(lamda/n/3.145/waist**2)


