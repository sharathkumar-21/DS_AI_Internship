# # # # # student = {
# # # # #     "name":"sharath",
# # # # #     "class":12
    
# # # # # }
# # # # # print(student)
# # # # # print(type(student))

# # # # # student["age"]=20
# # # # # student["city"]="vijayanagar"
# # # # # print(student)


# # # # marks ={"math":80,"science":75,"english":85}
# # # # print(marks.get("math"))
# # # # print(marks.get("history",0))
# # # # for subject,score in marks.items():
# # # #     print(subject,score)
# # # # marks.update({"history":90})
# # # # print(marks)

# purchase={
#     "alice":250,
#     "bob":400,
#     "charlie":150
# }
# for person,amount in purchase.items():
#     print(f"{person} used${amount}")

# n = int(input("enter the number of customers: "))
# user_purchases ={}

# for i in range(n):
#     name = input("enter the customer name: ")
#     amount = int(input(f"enter the purchase amount for{name}"))
#     user_purchases[name]=amount
#     print("customer purchase data:",user_purchases)

# top_customer = max(user_purchases,key=user_purchases.get) 
# print("top spending customer:" ,top_customer)   

print("task 1,contact book")

contacts ={
    "sharath": "6360899136",
    "sanjana": "8088647472",
    "chaitra": "7349161248"
}
contacts["mani"] = 9353655164
contacts["prajwal"] = 8088218209

present_contacts = contacts.get("sharath","contact not found")
absent_contacts = contacts.get("akhil","contact not found")
print("safe lock results:")
print("sharath:",present_contacts)
print("akhil", absent_contacts)

print("\n contact list:")
for name,phone in contacts.items():
    print(f"contact: {name} | phone : {phone}")

print("task 2,duplicate cleaner")
IDs = ["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]
unique_users =set(IDs)
print(unique_users)
print("ID05" in unique_users)

original_length = len(IDs)
set_length = len(unique_users)
duplicates_removed = original_length-set_length
print(duplicates_removed)


print("task-3,interest matcher")

friend_1 ={"python","cooking","hiking","movies"}
friend_2 ={"hiking","gaming","photography","pyhton"}

print(f"intersection:{friend_1 & friend_2}")
print(f"union:{friend_1 | friend_2}")
print(f"difference:{friend_1 - friend_2}")