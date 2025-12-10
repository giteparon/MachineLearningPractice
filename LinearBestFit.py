#Slope (m) Formula: m = n(∑xy)−(∑x)(∑y) / n(∑x^2)−(∑x)^2​
#Intercept (c) Formula: c = (∑y)−a(∑x) / n​
#for linear relations, we want to use the formula y = mx + c, and to predict the line of best fit we use the least square method, which predicts where the line of best fit will be using all data points.
grades = [5, 6 , 8, 8, 9, 1, 3, 4];
hoursStudied = [1, 2, 2, 3, 3, 0, 1, 1];
sumHoursStudied = 0;
sumGrades = 0;
xySum = 0
xsqSum = 0;
m = 0;
c = 0
n = len(grades);
for i in range(len(grades)):
    sumGrades += grades[i];
    sumHoursStudied += hoursStudied[i];
    xySum += grades[i] * hoursStudied[i];
    xsqSum += hoursStudied[i] ^ 2;
m = (n * (xySum) - sumHoursStudied * sumGrades) / (n * xsqSum - sumHoursStudied ^ 2);
c = sumGrades - m * sumHoursStudied;
def lineOfBestFit(x):
    y = m * x + c;
    print(m);
    print(c)
    print(sumGrades)
    print(sumHoursStudied)
    return y;
print(lineOfBestFit(2));
    



