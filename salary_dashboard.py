import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("pandas_employee.csv")
print(df.head())
# average salary
avg_salary=df.groupby("department")["salary"].mean()
print(avg_salary)
# plot bar chart
avg_salary.plot(kind="bar")
plt.xlabel("department")
plt.ylabel("average salary")
plt.title("average salary by department")
plt.show()
# salary distribution
plt.hist(df["salary"],bins=5)
plt.xlabel("salary")
plt.ylabel("employee")
plt.title("salary distribution")
plt.show()
# exprience vs salary
plt.scatter(df["experience"],df["salary"])
plt.xlabel("experience")
plt.ylabel("salary")
plt.title("Experience vs salary")
plt.show()
# deparment-wise employee count
val_count=df["department"].value_counts()
print(val_count)
val_count.plot(kind="pie",autopct="%1.1f%%")
plt.title("employee count")
plt.ylabel("")
plt.show()