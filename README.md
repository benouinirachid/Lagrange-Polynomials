# Lagrange-Polynomials

## Introduction

This script utilizes Lagrange Polynomials to curve fit a specified funtion (see modules/utilities.py to specify function of interest in function method). Starting with an L2 polynomial, the script will increment through L_N polynomials and plot the resulting approximation polynomial (blue dashed line) along with the real curve (black line) and points used to generate the polynomial (red dots). Note, L_N is specified in main.py under the variable Lagrange_P_limit. 

The mean-squared-error (MSE) is calcualated for each Lagrange Polynomial, and the error is plotted in the bottom plot for each iteration.

## Modules and Python Libraries Used

### Modules
1. lagrange_polynomials.py
2. utilities.py

### Libraries
1. Numpy
2. Matplotlib
3. time

## Running the Program
Navigate to the parent directory and enter the following command:

    python main.py
    
## Updates Needed
The script needs to be cleaned up and optimized. It is not completely DRY and there is a more optimal code structure to be sought.
