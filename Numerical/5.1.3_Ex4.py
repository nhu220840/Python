import numpy as np
import pandas as pd

def forward_difference(x_values, f_values):
    derivatives = []
    for i in range(len(x_values) - 1):
        h = x_values[i + 1] - x_values[i]
        deriv = (f_values[i + 1] - f_values[i]) / h
        derivatives.append(deriv)
    
    derivatives.append(None)
    return derivatives

def backward_difference(x_values, f_values):
    derivatives = [None]
    for i in range(1, len(x_values)):
        h = x_values[i] - x_values[i - 1]
        deriv = (f_values[i] - f_values[i - 1]) / h
        derivatives.append(deriv)
    
    return derivatives

def find_differential(x, f):
    forward_diff = forward_difference(x, f)
    
    backward_diff = backward_difference(x, f)
    
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
    
    return table, f_prime

def calculate_voltage(t, i, L, R):
    diff_table, di_dt = find_differential(t, i)
    
    voltage = []
    for j in range(len(t)):
        if di_dt[j] is not None:
            v = L * di_dt[j] + R * i[j]
            voltage.append(v)
        else:
            voltage.append(None)
            
    result_table = pd.DataFrame({
        't': t,
        'i': i,
        'di/dt': di_dt,
        'L(di/dt)': [L * rate if rate is not None else None for rate in di_dt],
        'Ri': R * i,
        'ℰ(t)': voltage
    })
    
    return result_table

def main():
    t = np.array([1.00, 1.01, 1.02, 1.03, 1.04])
    i = np.array([3.10, 3.12, 3.14, 3.18, 3.24])
    L = 0.98
    R = 0.142
    
    print("RL Circuit Voltage Calculation Problem")
    print("=" * 70)
    
    result = calculate_voltage(t, i, L, R)
    print("\nCompleted Table:")
    print(result.round(4))

if __name__ == "__main__":
    main()