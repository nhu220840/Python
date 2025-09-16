import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def create_ts_data(data, window_size=5):
    i = 1
    while i < window_size:
        data[f"users_{i}"] = data["users"].shift(-i)
        i += 1
    data["target"] = data["users"].shift(-i)
    data = data.dropna()
    return data


data = pd.read_csv("Datasets/Time-series-datasets/web-traffic.csv")
data["date"] = pd.to_datetime(data["date"], format="mixed", dayfirst=True, errors="coerce")
data["users"] = data["users"].interpolate()

fig, ax = plt.subplots()
ax.plot(data["date"], data["users"])
ax.set_xlabel("Date")
ax.set_ylabel("Users")
plt.show()

data = create_ts_data(data)

x = data.drop(["date", "target"], axis=1)
y = data["target"]

train_ratio = 0.8
num_samples = len(x)

x_train = x[:int(num_samples * train_ratio)]
y_train = y[:int(num_samples * train_ratio)]
x_test = x[int(num_samples * train_ratio):]
y_test = y[int(num_samples * train_ratio):]

model = RandomForestRegressor()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
print(f"MAE: {mean_absolute_error(y_test, y_predict)}")
print(f"MSE: {mean_squared_error(y_test, y_predict)}")
print(f"R2: {r2_score(y_test, y_predict)}")

fig, ax = plt.subplots()
ax.plot(data["date"][:int(num_samples * train_ratio)], data["users"][:int(num_samples * train_ratio)], label="train")
ax.plot(data["date"][int(num_samples * train_ratio):], data["users"][int(num_samples * train_ratio):], label="test")
ax.plot(data["date"][int(num_samples * train_ratio):], y_predict, label="prediction")
ax.set_xlabel("Date")
ax.set_ylabel("Users")
ax.legend()
ax.grid()
plt.show()

