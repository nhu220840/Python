import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def create_ts_data(data, window_size=5):
    i = 1
    while i < window_size:
        data[f"co2_{i}"] = data["co2"].shift(-i)
        i += 1
    data["target"] = data["co2"].shift(-i)
    data = data.dropna(axis=0)
    return data

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

data = create_ts_data(data)

x = data.drop(["time", "target"], axis=1)
y = data["target"]

train_ratio = 0.8
num_samples = len(x)

x_train = x[:int(num_samples * train_ratio)]
y_train = y[:int(num_samples * train_ratio)]
x_test = x[int(num_samples * train_ratio):]
y_test = y[int(num_samples * train_ratio):]

reg = LinearRegression()

reg.fit(x_train, y_train)
y_predict = reg.predict(x_test)
print(f"MAE: {mean_absolute_error(y_test, y_predict)}")
print(f"MSE: {mean_squared_error(y_test, y_predict)}")
print(f"R2: {r2_score(y_test, y_predict)}")

fig, ax = plt.subplots()
ax.plot(data["time"][:int(num_samples * train_ratio)], data["co2"][:int(num_samples * train_ratio)], label="train")
ax.plot(data["time"][int(num_samples * train_ratio):], data["co2"][int(num_samples * train_ratio):], label="test")
ax.plot(data["time"][int(num_samples * train_ratio):], y_predict, label="prediction")
ax.set_xlabel("Year")
ax.set_ylabel("CO2")
ax.legend()
ax.grid()
plt.show()