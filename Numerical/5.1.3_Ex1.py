import numpy as np
import pandas as pd

def forward_difference(x_values, f_values):
    derivatives = []
    for i in range(len(x_values) - 1):
        h = x_values[i+1] - x_values[i]
        deriv = (f_values[i+1] - f_values[i]) / h
        derivatives.append(deriv)
    
    derivatives.append(None)
    return derivatives

def backward_difference(x_values, f_values):
    derivatives = [None]
    for i in range(1, len(x_values)):
        h = x_values[i] - x_values[i-1]
        deriv = (f_values[i] - f_values[i-1]) / h
        derivatives.append(deriv)
    
    return derivatives

def find_differential(x, f):
    forward_diff = forward_difference(x, f)
    
    backward_diff = backward_difference(x, f)
    
    # print("Forward Differences:", forward_diff)
    # print("Backward Differences:", backward_diff)

    f_prime = []
    f_prime.append(forward_diff[0])
    for i in range(1, len(x) - 1):
        f_prime.append((forward_diff[i] + backward_diff[i]) / 2)
    f_prime.append(backward_diff[-1])
    
    table = pd.DataFrame({
        'x': x,
        'f(x)': f,
        "f'(x)": f_prime
    })
    
    return table

def main():
    x_a = np.array([0.5, 0.6, 0.7])
    f_a = np.array([0.4794, 0.5646, 0.6442])

    x_b = np.array([0.0, 0.2, 0.4])
    f_b = np.array([0.00000, 0.74140, 1.3718])
    print("Numerical Differentiation Using Forward and Backward Difference Methods")
    print("=" * 70)

    print("\nCompleted Table (a):")
    print(find_differential(x_a, f_a))

    print("\nCompleted Table (b):")
    print(find_differential(x_b, f_b))

if __name__ == "__main__":
    main()