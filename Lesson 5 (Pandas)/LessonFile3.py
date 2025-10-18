import pandas as pd

# Завантаження даних з файлу
df = pd.read_csv("ds_salaries.csv").dropna()

print(f"Середня зарплата: {df.describe()["salary_in_usd"]["mean"]}")
print(f"Медіана зарплат: {df.describe()["salary_in_usd"]["50%"]}")
mode_salary = df['salary_in_usd'].mode()[0]
print("Мода зарплат:", mode_salary)