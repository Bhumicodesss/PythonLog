#Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
#Salary(Lakhs) : Tax(%)

#Below 5 : 0%
#5-10 : 10%
#10-20 : 20%
#aboove 20 : 30%
inhandsalary = 0
salary= float(input("enter total salary:"))

if salary < 500000 :
    inhandsalary = salary - salary*0.1 - salary*0.05 - salary*0.03
elif salary >= 500000 and salary <= 1000000 :
    inhandsalary = salary - salary*(0.1 + 0.05 + 0.03 + 0.1)
elif salary >= 1000000 and salary <= 2000000 :
    inhandsalary = salary - salary*(0.1 + 0.05 + 0.03 + 0.2)
elif salary > 2000000 :
    inhandsalary = salary - salary*(0.1 + 0.05 + 0.03 + 0.3)

print("in hand salary after deduction is :", inhandsalary)