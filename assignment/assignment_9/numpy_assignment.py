import numpy as np

## Task 1
print("######################## Task 1 ########################")
OneDArray = np.arange(1,11,dtype=np.int64)
TwoDArray = np.array(np.arange(1,10,dtype=np.int64).reshape(3,3))
numArray = np.linspace(10,50,5,dtype=np.int64)

print("1D Array:",OneDArray)
print("Shape of 1D Array:",OneDArray.shape)
print("Data type of 1D Array:",OneDArray.dtype)

print("2D Array:",TwoDArray)
print("Shape of 2D Array:",TwoDArray.shape)
print("Data type of 2D Array:",TwoDArray.dtype)

print("Num Array:",numArray)
print("Shape of Num Array:",numArray.shape)
print("Data type of Num Array:",numArray.dtype)

## Task 2
print("######################## Task 2 ########################")
A = np.array([10, 20, 30, 40, 50],dtype=np.int64)
B = np.array([1, 2, 3, 4, 5],dtype=np.int64)

print("Addition:", A+B)
print("Subtraction:", A-B)
print("Multiplication:", A*B)
print("Division:", A/B)
print("Power:", A**2)

## Task 3
print("######################## Task 3 ########################")
values = np.array([2,4,6,8,10],dtype=np.int64)
print("Square root:", np.sqrt(values))
print("Exponential:", np.exp(values))
print("Logarithm:", np.log(values))
print("Sum:", np.sum(values))
print("Cumulative Sum:", np.cumsum(values))

## Task 4
print("######################## Task 4 ########################")
data = np.array([[10,20,30],[40,50,60],[70,80,90]],dtype=np.int64)
print("Row wise sum:",np.sum(data,axis=1))
print("Column wise sum:",np.sum(data,axis=0))
print("Min Value:",np.min(data))
print("Max Value:",np.max(data))
print("Mean:",np.mean(data))

##Task 5
print("######################## Task 5 ########################")
marks = np.array([78,85,90,66,72,88,95,60],dtype=np.int64)
print("Mean:",np.mean(marks))
print("Median:",np.median(marks))
print("Variance:",np.var(marks))
print("Standard Deviation:",np.std(marks))
print("Min:",np.min(marks))
print("Max:",np.max(marks))
print("Range:",np.ptp(marks))

##Task 6
print("######################## Task 6 ########################")
print("Sorted Array:",np.sort(marks))
print("25th Percentile:",np.percentile(marks,25))
print("50th Percentile:",np.percentile(marks,50))
print("75th Percentile:",np.percentile(marks,75))

average = np.mean(marks)
print("Students scored above average:", np.sum(marks > average))

##Task 7
print("######################## Task 7 ########################")
##daily sales data
sales = np.array([1200,1500,900,2000,1800,1700,1600],dtype=np.int64)

print("Total weekly sales:",np.sum(sales))
print("Average daily sales:",np.mean(sales))
print("Highest sales of the day:",np.max(sales))
print("Lowest sales of the day:",np.min(sales))
print("Standard Deviation:",np.std(sales))
print("Sales above average:",np.sum(sales > np.mean(sales)))