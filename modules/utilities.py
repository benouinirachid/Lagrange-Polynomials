from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def function(x):
	return x**4 - 3.8*x**2 - 1


def plot(X_finite, X_actual, Y_actual, L, MSE, n, LP_limit, plot_time_pause):
	plt.subplots_adjust(hspace=0.5)

	plt.subplot(211)
	# Plot measured, actual in subplot 1
	Y_finite = [function(x) for x in X_finite]
	plt.plot(X_finite, Y_finite, 'ro')

	plt.plot(X_actual, Y_actual, 'k')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title("Lagrange Polynomial, L{}".format(len(X_finite)))

	L.plot()

	# Plot MSE in subplot 2
	plt.subplot(212)
	plot_mse(MSE, n-1)

	plt.pause(plot_time_pause)

	if n == LP_limit:
		plt.show()
	else:
		plt.clf()


def plot_mse(MSE, n):
	x_n = [x for x in xrange(2,2+n)]
	plt.plot(x_n, MSE, 'bo')
	plt.plot(np.linspace(0, len(x_n)+2, 50), np.zeros(50), 'k--')
	plt.xlabel("L degree polynomial")
	plt.ylabel("MSE")
	plt.title("MSE at L{}: {:.2e}".format(n+1, MSE[n-1]))
	x_min, x_max = 1, max(x_n)+1
	y_min = min(MSE) - max(MSE)*0.15
	y_max = max(MSE)*1.25
	plt.axis([x_min, x_max, y_min, y_max])


def calculate_error(Y_lagrange, Y_actual):
	MSE = 0
	for y, y_lagrange in zip(Y_actual, Y_lagrange):
		MSE += ((y - y_lagrange)**2)

	return MSE