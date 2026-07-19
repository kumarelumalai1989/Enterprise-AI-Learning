name = input("Enter employee name: ")
age = int(input("Enter employee age: "))
experience = int(input("Enter years of experience: "))

print("Employee Summary:")
print(f"Name: {name}")
print(f"Age: {age}")
if experience > 10:
    print(f"Senior Engineer")
else:
    print(f"Engineer")