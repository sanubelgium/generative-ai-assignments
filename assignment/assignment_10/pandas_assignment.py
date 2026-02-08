import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print("######################## Task 1 ########################")
marks = [78,85,90,66,72]
marks_series = pd.Series(marks)
print("Series values: ",marks_series)
print("Series index: ",marks_series.index)
print("Series type: ",type(marks_series))
print("First element of series: ",marks_series[0])
print("Last element of series: ",marks_series[marks_series.size-1])
print("2nd Last element of series: ",marks_series[marks_series.size-2])


print("######################## Task 2 ########################")
print("Add 5 marks in the series", marks_series + 5)
print("Subtract 2 marks from the series", marks_series - 2)
print("Multiply 1.05 marks in the series", marks_series * 1.05)
print("Divide 2 marks in the series", marks_series / 2)

print("######################## Task 3 ########################")
print("Maximum marks: ",marks_series.max())
print("Minimum marks: ",marks_series.min())
print("Sum of marks: ",marks_series.sum())
print("Mean marks: ",marks_series.mean())

print("Apply lambda function to check whether user passed or failed (pass mark is 70): ",marks_series.apply(lambda x: "Pass" if x>70 else "Fail"))
print("Count of Passed student: ",marks_series.apply(lambda x: "Pass" if x>70 else "Fail").value_counts())


print("######################## Task 4 ########################")
students = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks": [78,85,90,66,72],
    "Subject": ["Math", "Math", "Science", "Science","Math"]
}

students_df = pd.DataFrame(students)
print("Students DataFrame first 3 rows: ",students_df[0:3])
print("Students DataFrame last 2 rows: ",students_df[3:5])
print("Shape of students DataFrame: ",students_df.shape)
print("Columns of students DataFrame: ",students_df.columns)

print("######################## Task 5 ########################")
print("Info: ",students_df.info())
print("Describe: ",students_df.describe())
print("Head: ",students_df.head())
print("Tail: ",students_df.tail())

students_df_sorted = students_df.sort_values(by="Marks",ascending=False)
print("Sort in descending order of marks: ",students_df_sorted)
print("Reset index: ",students_df_sorted.reset_index(drop=True))

print("######################## Task 6 ########################")
print("Score more than 75",students_df[students_df["Marks"] > 75])
print("Subject is Math",students_df[students_df["Subject"] == "Math"])
print("Score more then average",students_df[students_df["Marks"] > students_df["Marks"].mean()])
print("Failed student",students_df[students_df["Marks"] < 70])

print("######################## Task 7 ########################")
print("Average marks per subject",students_df.groupby("Subject")["Marks"].mean())
print("Count no of students per subject: ",students_df.groupby("Subject")["Name"].count())
print("Maximum marks per subject: ",students_df.groupby("Subject")["Marks"].max())

print("######################## Task 8 ########################")
print("bar graph - student name vs marks",students_df.plot(kind="bar",x="Name",y="Marks",title="Student Name vs Marks"  ))
plt.show()  
print("line graph - marks",students_df["Marks"].plot(kind="line",title="Marks line graph"))
plt.show()
print("histogram - marks",students_df["Marks"].plot(kind="hist",title="Marks histogram"))
plt.show()

print("######################## Task 9 ########################")
sales = {
    'Day' : ['Mon','Tue','Wed','Thu','Fri'],
    'Revenue' : [1200,1500,900,2000,1800]
}
sales_df = pd.DataFrame(sales)
print("Total Revenue: ",sales_df["Revenue"].sum())
print("Average Daily Revenue: ",sales_df["Revenue"].mean())
print("Day with highest revenue: ",sales_df["Day"].iloc[sales_df["Revenue"].idxmax()])
print("Day with revenue more than average: ",sales_df[sales_df["Revenue"] > sales_df["Revenue"].mean()])

print("bar graph - day vs revenue")
sales_df.plot(kind="bar",x="Day",y="Revenue",title="Day vs Revenue")
plt.show()