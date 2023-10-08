inhandsalary = 0
salary = float(input("Enter total salary: "))

# Calculate HRA, DA, PF
deductions = 0.1 + 0.05 + 0.03
inhandsalary = salary * (1 - deductions)

# Calculate tax based on salary range
if salary < 500000:
    tax_percentage = 0
elif 500000 <= salary < 1000000:
    tax_percentage = 0.1
elif 1000000 <= salary < 2000000:
    tax_percentage = 0.2
else:
    tax_percentage = 0.3

# Apply tax deduction
tax_deduction = salary * tax_percentage
inhandsalary -= tax_deduction

print("In-hand salary after deduction is:", inhandsalary)
