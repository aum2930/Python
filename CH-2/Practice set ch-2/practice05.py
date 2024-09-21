# 5. Write a python program to find an average of two numbers entered by the user.

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
sum = num1 + num2
avg = sum / 2
ans = int(avg) #here we used type conversion "float to int conversion"

print(type(ans),"The average of num1 and num2 is:",ans)

