import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from diabetes_classification import scaler

data = pd.read_csv("Datasets/csgo.csv")
# profile = ProfileReport(data)
# profile.to_file("csgo_report.html")

target = "result"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)

# scaler = StandardScaler()
# x_train = scaler.fit_transform(x_train)
# x_test = scaler.transform(x_test)


