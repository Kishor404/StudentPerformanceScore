import pandas as pd
from sklearn.linear_model import LinearRegression


data=pd.read_csv("Student_Performance.csv")

x_id=["HoursStudied","PreviousScores","Extracurricular (0/1)","SleepHours","SampleQuestionPapersPracticed"]

X=data[x_id]
y=data["Performance"]

model=LinearRegression()

model.fit(X,y)

b0=model.intercept_
bn=model.coef_

#print(bn)

n=len(x_id)

X1=[]
for i in x_id:
	x=int(input("Enter "+i+" : "))
	X1.append(x)
	
y1=b0
for i in range(n):
	y1=y1+(bn[i]*X1[i])
	
print("Performance : ",y1)