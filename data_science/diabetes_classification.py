import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from lazypredict.Supervised import LazyClassifier


# Read data
data = pd.read_csv('Datasets/diabetes.csv')
# profile = ProfileReport(data, title="Profiling Report")
# profile.to_file("diabetes_report.html")

# Data split in vertical
target = "Outcome"
x = data.drop(target, axis=1)
y = data[target]

# Data split in horizontal
# Random state: no la ti le 1 bo data duoc xao tron co trat tu
# neu ko co dinh no thi moi lan chay lai ham data se van dam bao 20% cho test size
# nhung ko dam bao moi lan do tat ca du lieu trong bo test deu giong nhau
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.25, random_state=42)

# Data preprocessing
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Training model
# model = SVC()
# model = LogisticRegression()
# model = RandomForestClassifier(n_estimators=100, criterion="gini", random_state=42)
# model.fit(x_train, y_train)

# Predict new value
# y_predict = model.predict(x_test)

# params = {
#     "n_estimators": [100, 200, 300],
#     "criterion": ["gini", "entropy", "log_loss"]
# }
# grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42), param_grid=params, cv=4, scoring="recall", verbose=2)

# params = {
#     "penalty":["l1", "l2"],
#     "max_iter":[100, 200, 300],
#     "multi_class":["auto", "ovr", "multinomial"]
# }
#
# grid_search = GridSearchCV(estimator=LogisticRegression(random_state=42), param_grid=params, cv=5, verbose=1)
# grid_search.fit(x_train, y_train)

# print(grid_search.best_estimator_)
# print(grid_search.best_score_)
# print(grid_search.best_params_)
#
# y_predict = grid_search.predict(x_test)

# print(y_predict); print(len(y_predict))
# print(y_test.values); print(len(y_test))
# for i, j in zip(y_predict, y_test):
#     print(f"Predicted: {i}. Actual: {j}")

# print(classification_report(y_test, y_predict))

clf = LazyClassifier(verbose=0,ignore_warnings=True, custom_metric=None)
models, predictions = clf.fit(x_train, x_test, y_train, y_test)

