import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer


data = pd.read_csv('../../machine-learning-project/test.csv')
# profile = ProfileReport(data, title="Student Score Report")
# data["Độ tuổi :"] = data["Độ tuổi :"].astype(float)
data.columns = data.columns.str.strip()
data["Độ tuổi :"] = pd.to_numeric(data["Độ tuổi :"], errors="coerce")  # Nếu có lỗi, đặt NaN

data["Điểm trung bình năm học gần nhất"] = pd.to_numeric(data["Điểm trung bình năm học gần nhất"], errors="coerce")  # Nếu có lỗi, đặt NaN

print("\n📌 Số lượng giá trị NaN trước khi xử lý:")
print(data[["Độ tuổi :", "Điểm trung bình năm học gần nhất"]].isnull().sum())
# target = "Điểm gpa học kì gần nhất"
# x = data.drop(columns=["Timestamp", target], errors='ignore')
# y = data[target]

# Tạo một đối tượng SimpleImputer với chiến lược điền giá trị trung vị
imputer = SimpleImputer(strategy='mean')

# Sử dụng imputer để điền giá trị thiếu cho các cột "math score" và "reading score"
# fit_transform() sẽ học giá trị trung vị từ dữ liệu huấn luyện và điền các giá trị thiếu
data[["Độ tuổi :", "Điểm trung bình năm học gần nhất"]] = imputer.fit_transform(data[["Độ tuổi :", "Điểm trung bình năm học gần nhất"]])

# Tạo một đối tượng StandardScaler để chuẩn hóa dữ liệu
# scaler = StandardScaler()

# Sử dụng scaler để chuẩn hóa (standardize) các cột "math score" và "reading score"
# Quá trình này sẽ chuyển đổi dữ liệu sao cho có trung bình bằng 0 và độ lệch chuẩn bằng 1
# data[["Độ tuổi :", "Điểm trung bình năm học gần nhất"]] = scaler.fit_transform(data[["Độ tuổi :", "Điểm trung bình năm học gần nhất"]])
# In ra giá trị trước và sau khi xử lý
# for i, j in zip(data[["Độ tuổi :", "Điểm trung bình năm học gần nhất"]].values, result):
#     print(f"Before {i}. After {j}")
print("\n📌 Số lượng giá trị NaN sau khi xử lý:")
print(data[["Độ tuổi :", "Điểm trung bình năm học gần nhất"]].isnull().sum())
