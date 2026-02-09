################file handling #############
# file = open("sample.txt","w")
# file.write("hello,this is a file handling example.")
# file.close()
# file =open("sample.txt","r")
# content =file.read()
# # print(content)
# file.close()

# with open("sample.txt","r")as file:
#     content = file.read()
#     print(content)

# try:
#     with open("missing.txt","r")as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Filenot found.please check the filename.")


# import csv
# with open ("data.csv","w",newline="")as file:
#     writer = csv.writer(file)
#     writer.writerow(["name","age","city"])
#     writer.writerow(["sharath",21,"vijayanagar"])
#     writer.writerow(["akhil",22,"london"])
#     writer.writerow(["hemanth",23,"america"])
# with open("data.csv","r") as file:
#     reader =csv.reader(file)
#     for row in reader:
#         print(row)

from openpyxl import load_workbook

wb = load_workbook("sample_student.xlsx")
sheet = wb.active

for row in sheet.values:
    print(row)


