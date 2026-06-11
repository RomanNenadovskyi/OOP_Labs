import pandas as pd

# Завдання 1. Імпорт та первинний аналіз даних

class DataLoader:

    def load_data(self, file_path):
        df = pd.read_csv(file_path)
        return df


class DataAnalyzer:

    def show_head_tail(self, df):

        print("\nПерші 5 рядків таблиці:")
        print(df.head())

        print("\nОстанні 5 рядків таблиці:")
        print(df.tail())


    def shape_info(self, df):

        rows, columns = df.shape
        print(f"\nКількість рядків: {rows}")
        print(f"Кількість стовпців: {columns}")


    def memory_usage(self, df):

        memory_bytes = df.memory_usage(deep=True).sum()
        memory_mb = memory_bytes / (1024 ** 2)

        print(f"\nНабір даних займає {memory_mb:.2f} MB пам'яті")
# ==========================================


# Завдання 2. Аналіз структури та типів даних

class DataStructure:

    def show_info(self, df):

        print("\nТипи даних у таблиці:")
        df.info()


    def check_missing(self, df):

        print("\nКількість пропущених значень:")
        print(df.isnull().sum())
# ==========================================


# Завдання 3. Фільтрація вакансій

class DataFilter:

    def filter_cloud(self, df):

        print("\nВакансії у сфері Cloud Computing:")
        print(df[df["Industry"] == "Cloud Computing"])


    def filter_senior(self, df):

        print("\nВакансії рівня Senior:")
        print(df[df["Experience Level"] == "Senior"])


    def filter_fulltime_city(self, df):

        print("\nFull-Time вакансії у місті New York:")
        print(df[(df["Job Type"] == "Full-Time") & (df["Location"] == "New York")])
# ==========================================


# Завдання 4. Сортування даних за зарплатою

class SalaryAnalyzer:

    def prepare_salary(self, df):

        # Витягуємо максимальну зарплату з тексту
        df["Max Salary"] = df["Salary Range"].str.extract(r'(\d+)$')
        df["Max Salary"] = df["Max Salary"].astype(int)

        return df


    def sort_salary(self, df):

        sorted_df = df.sort_values(by="Max Salary", ascending=False)

        print("\n5 вакансій з найвищою зарплатою:")
        print(sorted_df.head(5))
# ==========================================


# Завдання 5. Групування та агрегатні функції

class DataGrouping:

    def group_by_industry(self, df):

        result = df.groupby("Industry").agg(

            vacancy_count=("Job Title", "count"),
            average_salary=("Max Salary", "mean")

        )

        print("\nСтатистика вакансій по галузях:")
        print(result)

        print("\nГалузь з найбільшою середньою зарплатою:")
        print(result.sort_values(by="average_salary", ascending=False).head(1))
# ==========================================


# Завдання 6. Використання apply()

class SalaryCategory:

    def categorize_salary(self, salary):

        if salary <= 40000:
            return "Low"

        elif 40001 <= salary <= 70000:
            return "Medium"

        else:
            return "High"


    def create_category(self, df):

        df["Salary Category"] = df["Max Salary"].apply(self.categorize_salary)

        print("\nПеревірка категоризації зарплат:")
        print(df[["Max Salary", "Salary Category"]].head())
# ==========================================


# Завдання 7. Часовий аналіз вакансій

class TimeAnalysis:

    def analyze_jobs_by_year(self, df):

        df["Date Posted"] = pd.to_datetime(df["Date Posted"])

        df["Year"] = df["Date Posted"].dt.year

        jobs_per_year = df.groupby("Year").agg(
            vacancies=("Job Title", "count")
        )

        print("\nКількість вакансій по роках:")
        print(jobs_per_year)
# ==========================================

# Основна програма

loader = DataLoader()
df = loader.load_data("Job opportunities.csv")

# Завдання 1
analyzer = DataAnalyzer()
analyzer.show_head_tail(df)
analyzer.shape_info(df)
analyzer.memory_usage(df)

# Завдання 2
structure = DataStructure()
structure.show_info(df)
structure.check_missing(df)

# Завдання 3
filter_data = DataFilter()
filter_data.filter_cloud(df)
filter_data.filter_senior(df)
filter_data.filter_fulltime_city(df)

# Завдання 4
salary = SalaryAnalyzer()
df = salary.prepare_salary(df)
salary.sort_salary(df)

# Завдання 5
group = DataGrouping()
group.group_by_industry(df)

# Завдання 6
category = SalaryCategory()
category.create_category(df)

# Завдання 7
time_analysis = TimeAnalysis()
time_analysis.analyze_jobs_by_year(df)