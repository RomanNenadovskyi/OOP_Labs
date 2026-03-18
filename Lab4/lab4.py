import sqlite3
import pandas as pd

# 1. Підключення до бази даних
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# 2. Завантаження CSV у DataFrame
df = pd.read_csv("Job opportunities.csv")

print("Перші 5 рядків CSV:")
print(df.head())

print("\nНазви колонок:")
print(df.columns)

# 3. Завантаження у SQLite
df.to_sql("jobs", conn, if_exists="replace", index=False)

print("\nДані завантажено у таблицю jobs")

# -------------------------------------------------
# 4. Перші 10 вакансій

print("\nПерші 10 вакансій:")

query = """
SELECT *
FROM jobs
LIMIT 10;
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 5. Вакансії з навичкою SQL

print("\nВакансії з навичкою SQL:")

query = """
SELECT *
FROM jobs
WHERE "Required Skills" LIKE '%SQL%';
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 6. Унікальні Location і Company

print("\nУнікальні Location та Company:")

query = """
SELECT DISTINCT Location, Company
FROM jobs;
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 7. Середня зарплата за Experience Level

print("\nСередня зарплата за Experience Level:")

query = """
SELECT "Experience Level",
AVG(CAST(substr("Salary Range",1,5) AS INTEGER)) as avg_salary
FROM jobs
GROUP BY "Experience Level";
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 8. Кількість вакансій за Experience Level

print("\nКількість вакансій за Experience Level:")

query = """
SELECT "Experience Level",
COUNT(*) as total_jobs
FROM jobs
GROUP BY "Experience Level";
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 9. Мінімальна та максимальна зарплата

print("\nМінімальна та максимальна зарплата:")

query = """
SELECT
MIN(CAST(substr("Salary Range",1,5) AS INTEGER)) as min_salary,
MAX(CAST(substr("Salary Range",1,5) AS INTEGER)) as max_salary
FROM jobs;
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 10. Кількість вакансій у кожній індустрії (salary > 50000)

print("\nКількість вакансій у кожній індустрії (зарплата > 50000):")

query = """
SELECT Industry,
COUNT(*) as jobs_count
FROM jobs
WHERE CAST(substr("Salary Range",1,5) AS INTEGER) > 50000
GROUP BY Industry;
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 11. Середня зарплата для кожної індустрії

print("\nСередня зарплата для кожної індустрії:")

query = """
SELECT Industry,
AVG(CAST(substr("Salary Range",1,5) AS INTEGER)) as avg_salary
FROM jobs
GROUP BY Industry;
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 12. Кількість вакансій за Location та Experience Level

print("\nКількість вакансій за Location та Experience Level:")

query = """
SELECT Location, "Experience Level",
COUNT(*) as total
FROM jobs
GROUP BY Location, "Experience Level";
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 13. Кількість вакансій за Industry та Job Type

print("\nКількість вакансій за Industry та Job Type:")

query = """
SELECT Industry, "Job Type",
COUNT(*) as total
FROM jobs
GROUP BY Industry, "Job Type";
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 14. Середня зарплата за Location і Experience Level

print("\nСередня зарплата за Location і Experience Level:")

query = """
SELECT Location, "Experience Level",
AVG(CAST(substr("Salary Range",1,5) AS INTEGER)) as avg_salary
FROM jobs
GROUP BY Location, "Experience Level";
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 15. 5 вакансій з найбільшою зарплатою

print("\n5 вакансій з найвищою зарплатою:")

query = """
SELECT *
FROM jobs
ORDER BY CAST(substr("Salary Range",1,5) AS INTEGER) DESC
LIMIT 5;
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 16. Компанії з найбільшою кількістю вакансій у 2023

print("\nКомпанії з найбільшою кількістю вакансій у 2023:")

query = """
SELECT Company,
COUNT(*) as jobs_count
FROM jobs
WHERE "Posting Date" LIKE '2023%'
GROUP BY Company
ORDER BY jobs_count DESC;
"""

result = pd.read_sql(query, conn)
print(result)

# -------------------------------------------------
# 17. Закриття з'єднання

conn.close()