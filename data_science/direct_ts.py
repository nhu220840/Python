import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def create_ts_data(data, window_size=5, target_size=3):
    i = 1
    while i < window_size:
        data[f"co2_{i}"] = data["co2"].shift(-i)
        i += 1
    i = 0
    while i < target_size:
        data[f"target_{i+1}"] = data["co2"].shift(-i-window_size)
        i += 1
    data = data.dropna(axis=0)
    return data

# Read data
data = pd.read_csv("/media/sherry/New Volume/Python/data_science/Datasets/Time-series-datasets/co2.csv")
data["time"] = pd.to_datetime(data["time"])
data["co2"] = data["co2"].interpolate()
# print(data.dtypes)
# print(data.info())

# fig, ax = plt.subplots()
# ax.plot(data["time"], data["co2"])
# ax.set_xlabel("Year")
# ax.set_ylabel("CO2")
# plt.show()

# Data transform
window_size = 5
target_size = 3
data = create_ts_data(data, window_size, target_size)