import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("employees.csv")
# print(df.shape)
# print(df.head())

# # 2. Descriptive Statistics
#print(df.describe(include="all"))

# # 3. Salary Distribution by Department
# print(df.groupby("Department")["Salary"].describe())

# # 4. Salary Histogram
# plt.hist(df["Salary"], bins=10, edgecolor="black")
# plt.show()

# # 5. Boxplot: Salary by Department
# df.boxplot(column="Salary", by="Department")
# plt.title("Salary by Department")
# plt.suptitle("")   # remove the automatic "Boxplot grouped by" title
# plt.ylabel("Salary")
# plt.show()

# # 6. Correlation
# print(df["YearsExperience"].corr(df["Salary"]))
# ≈ 0.05

# # 7. Average Salary by Department
# print(df.groupby("Department")["Salary"].mean())

# # 8. Skewness & Kurtosis
print(df["Salary"].skew(), df["Salary"].kurt())
# Skewness ≈ 0.018, Kurtosis ≈ -0.57
# # Skewness ~0 → Salary distribution is symmetric.
# # Kurtosis <0 → Flatter distribution than normal.
# #Most statistical methods (e.g., t-test, ANOVA, regression, control charts) assume that data follows a normal distribution.
# # Skewness ≈ 0, Kurtosis ≈ 0 → Data is close to normal → you can apply those methods.

# #If skewness/kurtosis are large → use non-parametric tests (Mann-Whitney, Kruskal-Wallis, etc.) or transform data (log, Box-Cox).

# # 9. Scatter Plot: Age vs Salary
# plt.scatter(df["Age"], df["Salary"])
# plt.show()