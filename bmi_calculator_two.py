height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/(height**2)
rbmi = round(bmi)

if bmi<18.5 :
    print(f"Your BMI is {rbmi}, you are underweight.")
elif bmi<25:
    print(f"Your BMI is {rbmi}, you are normal weight.")
elif bmi<30:
    print(f"Your BMI is {rbmi}, you are slightly overweight.")
elif bmi<35:
    print(f"Your BMI is {rbmi}, you are obese.")
else:
    print(f"Your BMI is {rbmi}, you are clinically obese.")
         