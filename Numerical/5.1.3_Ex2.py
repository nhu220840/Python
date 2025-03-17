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

def calculate_speed(x, f):
    forward_diff = forward_difference(x, f)
    
    backward_diff = backward_difference(x, f)
    
    # print("Forward Differences:", forward_diff)
    # print("Backward Differences:", backward_diff)

    f_prime = []
    f_prime.append(forward_diff[0])
    for i in range(1, len(x) - 1):
        f_prime.append((forward_diff[i] + backward_diff[i]) / 2)
    f_prime.append(backward_diff[-1])
    
    # Cai nay thay doi dinh dang in ra
    table = pd.DataFrame({
        'Time': x,
        'Distance': f,
        "Speed": f_prime
    })
    
    return table

def main():
    # Cai nay thay doi duoc gia tri trong tung bai
    time = np.array([0, 3, 5, 8, 10, 13])
    distance = np.array([0, 225, 383, 623, 742, 993])
    print("Numerical Differentiation Using Forward and Backward Difference Methods")
    print("=" * 70)

    print(calculate_speed(time, distance))

if __name__ == "__main__":
    main()




