
import pandas as pd
import numpy as np
from pathlib import Path

rng = np.random.default_rng(42)

departments = ["Operations", "Marketing", "Technology", "Finance"]
cities = ["Delhi", "Mumbai", "Bangalore", "Hyderabad"]
priorities = ["High", "Medium", "Low"]
statuses = ["Completed", "In Progress", "Not Started"]

tasks = []

for i in range(1, 501):
    department = rng.choice(departments)
    city = rng.choice(cities)
    priority = rng.choice(priorities, p=[0.3, 0.5, 0.2])
    status = rng.choice(statuses, p=[0.55, 0.30, 0.15])

    start_date = pd.Timestamp("2026-08-01") + pd.Timedelta(
        days=int(rng.integers(0, 75))
    )

    planned_days = int(rng.integers(3, 22))
    due_date = start_date + pd.Timedelta(days=planned_days)

    if status == "Completed":
        actual_end_date = due_date + pd.Timedelta(
            days=int(rng.integers(-4, 9))
        )
        progress = 100
    else:
        actual_end_date = pd.NaT
        progress = (
            int(rng.integers(10, 95))
            if status == "In Progress"
            else 0
        )

    budget = int(rng.integers(10000, 150001))

    tasks.append({
        "Task_ID": f"T{i:04d}",
        "Department": department,
        "City": city,
        "Priority": priority,
        "Status": status,
        "Start_Date": start_date,
        "Due_Date": due_date,
        "Actual_End_Date": actual_end_date,
        "Progress_Percent": progress,
        "Budget_INR": budget
    })

df = pd.DataFrame(tasks)

as_of_date = pd.Timestamp("2026-11-02")

df["Delayed"] = (
    ((df["Status"] == "Completed") &
     (df["Actual_End_Date"] > df["Due_Date"])) |
    ((df["Status"] != "Completed") &
     (df["Due_Date"] < as_of_date))
)

df["At_Risk"] = (
    (df["Status"] != "Completed") &
    (df["Priority"] == "High") &
    (df["Due_Date"] <= as_of_date + pd.Timedelta(days=7))
)

output = Path("data")
output.mkdir(exist_ok=True)

df.to_csv(output / "project_tasks.csv", index=False)
df.to_excel(output / "project_tasks.xlsx", index=False)

print("Dataset generated successfully!")
print("Total Tasks:", len(df))
print("Completed:", (df["Status"] == "Completed").sum())
print("Delayed:", df["Delayed"].sum())
print("At Risk:", df["At_Risk"].sum())

