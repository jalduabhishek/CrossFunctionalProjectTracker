
import pandas as pd
from pathlib import Path

df = pd.read_csv("data/project_tasks.csv")

total = len(df)
completed = (df["Status"] == "Completed").sum()
in_progress = (df["Status"] == "In Progress").sum()
not_started = (df["Status"] == "Not Started").sum()

delayed = df["Delayed"].astype(str).str.lower().eq("true").sum()
at_risk = df["At_Risk"].astype(str).str.lower().eq("true").sum()

completion_rate = completed / total * 100

completed_tasks = df[df["Status"] == "Completed"].copy()
completed_tasks["Due_Date"] = pd.to_datetime(completed_tasks["Due_Date"])
completed_tasks["Actual_End_Date"] = pd.to_datetime(
    completed_tasks["Actual_End_Date"]
)

on_time = (
    completed_tasks["Actual_End_Date"] <= completed_tasks["Due_Date"]
).sum()

on_time_rate = (
    on_time / completed * 100 if completed else 0
)

department_summary = df.groupby("Department").agg(
    Total_Tasks=("Task_ID", "count"),
    Completed=("Status", lambda x: (x == "Completed").sum()),
    Delayed=("Delayed", lambda x: x.astype(str).str.lower().eq("true").sum()),
    At_Risk=("At_Risk", lambda x: x.astype(str).str.lower().eq("true").sum())
)

department_summary["Completion_Rate"] = (
    department_summary["Completed"] /
    department_summary["Total_Tasks"] * 100
).round(2)

Path("reports").mkdir(exist_ok=True)

department_summary.to_csv("reports/department_summary.csv")

with open("reports/project_summary.txt", "w", encoding="utf-8") as f:
    f.write(f"Total Tasks: {total}\n")
    f.write(f"Completed Tasks: {completed}\n")
    f.write(f"In Progress: {in_progress}\n")
    f.write(f"Not Started: {not_started}\n")
    f.write(f"Completion Rate: {completion_rate:.2f}%\n")
    f.write(f"Delayed Tasks: {delayed}\n")
    f.write(f"At-Risk Tasks: {at_risk}\n")
    f.write(f"On-Time Completion Rate: {on_time_rate:.2f}%\n")

print("PROJECT PERFORMANCE SUMMARY")
print("---------------------------")
print(f"Total Tasks: {total}")
print(f"Completed: {completed}")
print(f"In Progress: {in_progress}")
print(f"Not Started: {not_started}")
print(f"Completion Rate: {completion_rate:.2f}%")
print(f"Delayed Tasks: {delayed}")
print(f"At-Risk Tasks: {at_risk}")
print(f"On-Time Completion Rate: {on_time_rate:.2f}%")

print("\nDEPARTMENT PERFORMANCE")
print(department_summary)
