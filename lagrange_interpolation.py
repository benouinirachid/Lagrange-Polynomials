from __future__ import division
from modules.lagrange_polynomial import Lagrange_Polynomial
from modules.utilities import *
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

		
def main(X_finite, a, b, interval, LP_limit, MSE, plot_time_pause=1.0):
	
	# Actual
	X_actual = np.arange(a, b, interval)
	Y_actual = [function(x) for x in X_actual]

	n = len(X_finite)

	# Instantiate L polynomial
	L = Lagrange_Polynomial(n, X_finite, function, X_actual, Y_actual)

	# Calculate error between actual and lagrange
	MSE.append(calculate_error(L.P, Y_actual))

	
	# Plot
	plot(X_finite, X_actual, Y_actual, L, MSE, n, LP_limit, plot_time_pause)
		
	return MSE
	

if __name__ == '__main__':
	
	X = []
	a = -5
	b = 4
	Lagrange_P_limit = 10
	interval = 0.005
	plot_time_interval = 0.5

	num_range = [x for x in xrange(2, Lagrange_P_limit+1)]
	for i in num_range:
		x = np.linspace(a, b, i)
		X.append(x)

	MSE = []
	for index, x in enumerate(X):
		mse_x = main(x, a, b, interval, Lagrange_P_limit, MSE, plot_time_interval)
		MSE = mse_x
	

	
	

