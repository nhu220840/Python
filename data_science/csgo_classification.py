import pandas as pd
from lazypredict.Supervised import numeric_transformer
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


# Read data
data = pd.read_csv("Datasets/csgo.csv")
# profile = ProfileReport(data)
# profile.to_file("csgo_report.html")

# Split data
target = "points"
x = data.drop(columns=["map", "day", "month", "year", "date", "wait_time_s", target], errors='ignore')
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)

num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

result_value = ["Lost", "Tie", "Win"]
ord_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OrdinalEncoder(categories=[result_value]))
])

numeric_features = ["match_time_s", "team_a_rounds", "team_b_rounds", "ping",
                    "kills", "assists", "deaths", "mvps", "hs_percent"]

preprocessor = ColumnTransformer(transformers=[
    ("num_feature", num_transformer, numeric_features),
    ("ord_feature", ord_transformer, ["result"]),
])

reg = Pipeline(steps=[
    ("preprocessor", preprocessor),
    # ("model", LinearRegression())
])

result = reg.fit_transform(x_train)
