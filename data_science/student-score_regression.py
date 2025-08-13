import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from lazypredict.Supervised import LazyRegressor

# Read data
data = pd.read_csv('Datasets/StudentScore.xls')
# profile = ProfileReport(data, title="Student Score Report")
# profile.to_file("student-score-report.html")
# print(data[["math score", "reading score", "writing score"]].corr())

# Split data
target = "writing score"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# print(data["gender"].unique())
# print(data["race/ethnicity"].unique())
# print(data["parental level of education"].unique())
# print(data["lunch"].unique())
# print(data["test preparation course"].unique())

# Fill missing value and scaling data
## Numerical feature
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(missing_values=-1, strategy='median')),
    ('scaler', StandardScaler())
])

## Ordinal feature
education_values = ["some high school", "high school", "some college", "associate's degree",
                    "bachelor's degree", "master's degree"]
gender_values = ["male", "female"]
lunch_values = x_train["lunch"].unique()
test_values = x_train["test preparation course"].unique()
ord_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OrdinalEncoder(categories=[education_values, gender_values, lunch_values, test_values])),
])

## Nominal feature
nom_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(sparse_output=False))
])

## Synthesis
preprocessor = ColumnTransformer(transformers=[
    ("num_feature", num_transformer, ["reading score", "math score"]),
    ("ord_feature", ord_transformer, ["parental level of education", "gender", "lunch", "test preparation course"]),
    ("nom_feature", nom_transformer, ["race/ethnicity"]),
])

# Training model
# reg = Pipeline(steps=[
#     ("preprocessor", preprocessor),
#     ("model", LinearRegression())
# ])

reg = Pipeline(steps=[
    ("preprocessor", preprocessor),
    # ("model", RandomForestRegressor())
])

# use this if u want to see the output of data transformation
result = reg.fit_transform(x_train)

# reg.fit(x_train, y_train)

# LazyPredict not using Pipeline
# reg = LazyRegressor(verbose=0,ignore_warnings=True, custom_metric=None)
# models, predictions = reg.fit(x_train, x_test, y_train, y_test)

# Predict test set
# y_predict = reg.predict(x_test)
# for i, j in zip(y_predict, y_test):
#     print(f"Predicted value: {i}. Actual value: {j}")

# Evaluate model
# print(f"MAE: {mean_absolute_error(y_test, y_predict)}")
# print(f"MSE: {mean_squared_error(y_test, y_predict)}")
# print(f"R2: {r2_score(y_test, y_predict)}")

# params = {
#     "preprocessor__num_feature__imputer__strategy": ["mean", "median"],
#     "model__n_estimators": [100, 200, 300],
#     "model__criterion": ['absolute_error', 'poisson', 'squared_error', 'friedman_mse'],
#     "model__max_depth": [None, 2, 5]
# }
# grid_search = GridSearchCV(estimator=reg, param_grid=params, cv=5, scoring="r2", verbose=2, n_jobs=-1)
# # grid_search = RandomizedSearchCV(estimator=reg, param_distributions=params, n_iter=20, cv=5, scoring="r2", verbose=2, n_jobs=-1)
# grid_search.fit(x_train, y_train)
# y_predict = reg.predict(x_test)
# for i, j in zip(y_predict, y_test):
#     print(f"Predicted value: {i}. Actual value: {j}")
#
# print(grid_search.best_estimator_)
# print(grid_search.best_score_)
# print(grid_search.best_params_)
# print(f"MAE: {mean_absolute_error(y_test, y_predict)}")
# print(f"MSE: {mean_squared_error(y_test, y_predict)}")
# print(f"R2: {r2_score(y_test, y_predict)}")