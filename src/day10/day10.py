
import pandas as pd

# STEP 2 — Create messy dataset (added Date + messy City + duplicate row)
data = {
    "CustomerID": [101,102,103,104,105,106,107,107,108,109],
    "Name": ["Amit","Sara","John",None,"Priya","David","Meena","Meena","Ali","Riya"],
    "Age": [25,None,30,22,None,28,35,35,None,26],
    "City": [" Bangalore","Mumbai ","Delhi",None,"Bangalore","Chennai","Mumbai","Mumbai","Delhi"," Bangalore "],
    "OrderAmount": [2500,1800,None,2200,3000,None,1500,1500,2700,None],
    "PaymentMethod": ["UPI","Card","Cash","Card",None,"UPI","Cash","Cash","Card","UPI"],
    "Date": ["2024-01-05","2024-01-10","2024-02-01","2024-02-05","2024-03-01",
             "2024-03-05","2024-03-10","2024-03-10","2024-04-01","2024-04-05"]
}

df = pd.DataFrame(data)

# STEP 3 — Inspect dataset
print("First rows:\n", df.head())
print("\nDataset info:")
print(df.info())

# STEP 4 — Check missing values
print("\nMissing values per column:")
print(df.isna().sum())

# STEP 5 — Fill missing values (statistical approach)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["OrderAmount"] = df["OrderAmount"].fillna(df["OrderAmount"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])
df["Name"] = df["Name"].fillna("Unknown")

# STEP 6 — Check data types before conversion
print("\nData types BEFORE conversion:")
print(df.dtypes)

# STEP 7 — Convert data types
df["Age"] = df["Age"].astype(int)
df["Date"] = pd.to_datetime(df["Date"])

print("\nData types AFTER conversion:")
print(df.dtypes)

# -------------------------------------------------
# NEW PART — STRING CLEANING
# -------------------------------------------------

# Strip extra spaces from City names
df["City"] = df["City"].str.strip()

# Convert City names to lowercase
df["City"] = df["City"].str.lower()

print("\nCity column after cleaning:")
print(df["City"])

# -------------------------------------------------
# NEW PART — DUPLICATE HANDLING
# -------------------------------------------------

# Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nShape after removing duplicates:", df.shape)

# FINAL CLEAN DATASET

print("\nFinal cleaned dataset:")
print(df.head())











import pandas as pd

customer_orders = {
    "CustomerID": [101,102,103,104,105,106,107,107,108,109],
    "Name": ["sharath","akhil","hemanth",None,"sanjana","chaitra","avinash","veerana","Alice","Riya"],
    "Product": ["car","tanker","computer accesories","mobile phone ",
                "Dslr Camera","Bluetooth","Smart Watch",
                "QLED TV","Remote Control Car","toy Drone"],
    "City": ["hospet","vijayanagar","Delhi",None,"kudligi","kotturu",
             "Mumbai","Mumbai","Delhi","Bangalore"],
    "OrderAmount": [2420,3800,None,1300,3000,None,1580,18500,1700,None],
    "PaymentMethod": ["UPI","Card","Cash","Card",None,"UPI","Cash","Cash","Card","UPI"],
    "Date": ["2026-01-05","2025-01-10","2025-02-01","2026-02-05",
             "2025-03-01","2024-03-05","2024-03-10","2024-03-10",
             "2024-04-01","2024-04-05"]
}

df = pd.DataFrame(customer_orders)

df.to_csv("customer_orders.csv", index=False)

print("CSV file created successfully")

print("Task 1: The Integrity Audit")
import pandas as pd
df = pd.read_csv("customer_orders.csv")
pd.set_option("display.max_columns", None)
print("missing_val:\n",df.isna().sum())
print(df)
df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")
df["OrderAmount"] = df["OrderAmount"].fillna(df["OrderAmount"].mean())
df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())
removed_duplicates = df.drop_duplicates()
print("removed_duplicates:",removed_duplicates)














purchases = {
    "Price" : ["$120.50","$89.99","$250.00","$45.75","$120.50"],
    "Date" : ['2024-01-05','2024-01-10','2024-02-01','2024-02-15','2024-02-15'],
    "Product" : ["Smartphone","bluetooth","Laptop","charger","Phone"]
}
df = pd.DataFrame(purchases)
print(df.to_csv('sales.csv'))
print(df.dtypes,"\n")
Price_data= df['Price'].str.replace('$',"")
print(Price_data.astype(float),"\n")
df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'],"\n")
print(df)


















details = {
    "Location": [" New York", "new york", "NEW YORK ", "Chicago", " chicago "],
    "Sales": [300, 100, 400, 1200, 150]
}
df= pd.DataFrame(details)
location = df['Location']
print(location.str.strip())
print(location.str.lower())
print(location.unique)















































# STEP 1 — Import pandas
import pandas as pd

# STEP 2 — Create messy dataset (added Date + messy City + duplicate row)
data = {
    "CustomerID": [101,102,103,104,105,106,107,107,108,109],
    "Name": ["Amit","Sara","John",None,"Priya","David","Meena","Meena","Ali","Riya"],
    "Age": [25,None,30,22,None,28,35,35,None,26],
    "City": [" Bangalore","Mumbai ","Delhi",None,"Bangalore","Chennai","Mumbai","Mumbai","Delhi"," Bangalore "],
    "OrderAmount": [2500,1800,None,2200,3000,None,1500,1500,2700,None],
    "PaymentMethod": ["UPI","Card","Cash","Card",None,"UPI","Cash","Cash","Card","UPI"],
    "Date": ["2024-01-05","2024-01-10","2024-02-01","2024-02-05","2024-03-01",
             "2024-03-05","2024-03-10","2024-03-10","2024-04-01","2024-04-05"]
}

df = pd.DataFrame(data)

# STEP 3 — Inspect dataset
print("First rows:\n", df.head())
print("\nDataset info:")
print(df.info())

# STEP 4 — Check missing values
print("\nMissing values per column:")
print(df.isna().sum())

# STEP 5 — Fill missing values (statistical approach)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["OrderAmount"] = df["OrderAmount"].fillna(df["OrderAmount"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])
df["Name"] = df["Name"].fillna("Unknown")

# STEP 6 — Check data types before conversion
print("\nData types BEFORE conversion:")
print(df.dtypes)

# STEP 7 — Convert data types
df["Age"] = df["Age"].astype(int)
df["Date"] = pd.to_datetime(df["Date"])

print("\nData types AFTER conversion:")
print(df.dtypes)

# -------------------------------------------------
# NEW PART — STRING CLEANING
# -------------------------------------------------

# Strip extra spaces from City names
df["City"] = df["City"].str.strip()

# Convert City names to lowercase
df["City"] = df["City"].str.lower()

print("\nCity column after cleaning:")
print(df["City"])

# -------------------------------------------------
# NEW PART — DUPLICATE HANDLING
# -------------------------------------------------

# Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nShape after removing duplicates:", df.shape)

# FINAL CLEAN DATASET
print("\nFinal cleaned dataset:")
print(df.head())

#Task 1  The Integrity Audit

df = pd.read_csv('customers.csv')
print(f'shape of the DataFrame before cleaning : {df.shape}')
nulls = df.isna().sum()
filling_nulls = df.fillna(df.median(numeric_only=True), inplace=True)
duplicates = df.duplicated().sum()
removed_duplicates = df.drop_duplicates()
print(f'shape of the DataFrame after cleaning : {removed_duplicates.shape}')






