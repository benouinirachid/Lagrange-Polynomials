from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class Lagrange_Polynomial(object):

	def __init__(self, n, X, function, X_actual=None, Y_actual=None):
		self.n = n
		self.X = X
		self.X_actual = X_actual
		self.Y_actual = Y_actual
		self.function = function
		self.generate_f_k()
		self.generate_polynomial()
	

	def generate_f_k(self):
		self.f_k = []
		for xk in self.X:
			self.f_k.append(self.function(xk))


	def L_coeff_function(self, x, k):
		Lk = 1
		for i in xrange(self.n):
			if i == k:
				continue
			numerator = x - self.X[i]
			denominator = self.X[k] - self.X[i]
			Lk *= (numerator / denominator)
		return Lk


	def generate_polynomial(self):
		self.P = []
		for x in self.X_actual:
			Pk = 0
			for k, xk in enumerate(self.X):
				fk = self.f_k[k]
				Lk = self.L_coeff_function(x, k)
				Pk += (fk*Lk)
			self.P.append(Pk)


	def plot(self):
		plt.subplot(211)
		plt.plot(self.X_actual, self.P, 'b--', linewidth=2)
		x_min = min(self.X_actual) - max(self.X_actual) * 0.25
		x_max = max(self.X_actual) * 1.25
		
		if np.abs(max(self.Y_actual)) < 1e-3:
			y_max = np.abs(min(self.Y_actual))*0.075
			y_min = min(self.Y_actual) - np.abs(min(self.Y_actual) * 0.05)
		else:
			y_max = max(self.Y_actual) * 2.25
			y_min = min(self.Y_actual) - max(self.Y_actual) * 0.25

		plt.axis([x_min, x_max, y_min, y_max])

		