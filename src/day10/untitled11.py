# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:21:14 2026

@author: Sharath Kumar
"""
import pandas as pd
df = pd.read_csv("customer_orders")
print("missing_val:\n",df.isna.sum())

print("Shape before cleaning:", df.shape)


print("\nMissing Values Report:")
print(df.isna().sum())


numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())


df = df.drop_duplicates()

print("\nShape after cleaning:", df.shape)

pd.set_option("display.max_columns",None)
print(df)

