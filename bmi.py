#Get weight and height from user

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

#set BMI formula as a variable for following if statements

BMI = (weight) / ((height)*(height))

#if your BMI is >=30, then

if BMI >= 30:
    print(f"Your BMI of {BMI} indicates that you are obese")

#if your BMI is >=25, then

elif BMI >= 25:
    print(f"Your BMI of {BMI} indicates that you are overweight")

#if your BMI is >=18.5, then

elif BMI >= 18.5:
    print(f"Your BMI of {BMI} indicates that you are normal")

#or if your BMI is <18.5, then

else:
    print(f"Your BMI of {BMI} indicates that you are underweight")

