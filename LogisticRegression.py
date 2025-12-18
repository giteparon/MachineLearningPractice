import numpy as np 
import sqlite3
import random
initialW = 0.01
initialB = 0.01

grades = []
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
for i in range(1000):
    id = f"ID{i}"
    cursor.execute('SELECT * FROM data WHERE id = ?', (id,))
    retrieved = cursor.fetchall()
    grades[i] =  retrieved[0][1]
def gradiantascent(w, b, x):
    #https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/
    