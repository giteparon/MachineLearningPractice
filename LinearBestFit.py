#Slope (m) Formula: m = n(∑xy)−(∑x)(∑y) / n(∑x^2)−(∑x)^2​
#Intercept (c) Formula: c = (∑y)−a(∑x) / n​
#for linear relations, we want to use the formula y = mx + c, and to predict the line of best fit we use the least square method, which predicts where the line of best fit will be using all data points.
import matplotlib.pyplot as plt 
import numpy as np 
import sqlite3
import random
conn = sqlite3.connect('data.db');
cursor = conn.cursor();
create_table_sql = """
    CREATE TABLE IF NOT EXISTS data (
        id STRING PRIMARY KEY,
        grade INTEGER,
        hours INTEGER
    );
    """

cursor.execute(create_table_sql)
for i in range(1000):
    gradesql = random.randint(0,100)
    hoursStudiedsql = int(gradesql / 10 + random.randint(-2, 2))
    toInsert = f"ID{i}"
    data_to_insert = (toInsert, gradesql, hoursStudiedsql)
    cursor.execute("INSERT INTO data (id, grade, hours) VALUES (?, ?, ?)", data_to_insert)

conn.commit()

sumHoursStudied = 0;
sumGrades = 0;
xySum = 0
xsqSum = 0;
m = 0;
c = 0
n = 1000;
for i in range(1000):
    id = f"ID{i}"
    cursor.execute('SELECT * FROM data WHERE id = ?', (id,))
    retrieved = cursor.fetchall()
    sumGrades += retrieved[0][1];
    sumHoursStudied += retrieved[0][2];
    xySum += retrieved[0][1] * retrieved[0][2];
    xsqSum += retrieved[0][2]** 2;
m = ((n * xySum) - (sumHoursStudied * sumGrades)) / ((n * xsqSum) - (sumHoursStudied ** 2))

c = (sumGrades / n) - (m * sumHoursStudied / n)
def lineOfBestFit(x):
    y = m * x + c;
    print(m);
    print(c)
    print(sumGrades)
    print(sumHoursStudied)
    return y;
print(lineOfBestFit(2));

    



