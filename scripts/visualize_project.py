
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("data/project_tasks.csv")
Path("reports").mkdir(exist_ok=True)

# Chart 1: Task status distribution
status_counts = df["Status"].value_counts()
plt.figure(figsize=(8, 5))
status_counts.plot(kind="bar")
plt.title("Task Status Distribution")
plt.xlabel("Task Status")
plt.ylabel("Number of Tasks")
plt.tight_layout()
plt.savefig("reports/task_status.png", dpi=150)
plt.close()

# Chart 2: Completion rate by department
completion = df.groupby("Department")["Status"].apply(
    lambda x: (x == "Completed").mean() * 100
)
plt.figure(figsize=(8, 5))
completion.plot(kind="bar")
plt.title("Completion Rate by Department")
plt.xlabel("Department")
plt.ylabel("Completion Rate (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("reports/department_completion.png", dpi=150)
plt.close()

# Chart 3: Delayed tasks by department
df["Delayed"] = df["Delayed"].astype(str).str.lower().eq("true")
delays = df.groupby("Department")["Delayed"].sum()

plt.figure(figsize=(8, 5))
delays.plot(kind="bar")
plt.title("Delayed Tasks by Department")
plt.xlabel("Department")
plt.ylabel("Delayed Tasks")
plt.tight_layout()
plt.savefig("reports/department_delays.png", dpi=150)
plt.close()

# Chart 4: At-risk tasks by priority
df["At_Risk"] = df["At_Risk"].astype(str).str.lower().eq("true")
risk = df.groupby("Priority")["At_Risk"].sum()

plt.figure(figsize=(8, 5))
risk.plot(kind="bar")
plt.title("At-Risk Tasks by Priority")
plt.xlabel("Priority")
plt.ylabel("At-Risk Tasks")
plt.tight_layout()
plt.savefig("reports/priority_risks.png", dpi=150)
plt.close()

print("All four charts generated successfully!")
