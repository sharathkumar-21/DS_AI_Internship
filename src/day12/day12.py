# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 17:24:54 2026

@author: Sharath Kumar
"""

print("task-1,correlation checker") 
import matplotlib.pyplot as plt
study_hours=[1,2,3,4,5,6,7,8]
scores=[50,55,65,70,75,85,90,95]
plt.scatter(study_hours,scores)
plt.title("scatter plot")
plt.show()

























print("task-2,comparison dashboard")
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
trend_sales = [100, 150, 200, 250, 300]

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales")

plt.subplot(1, 2, 2)
plt.plot(months, trend_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()












