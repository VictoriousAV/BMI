number = float(input("ENTER THE WEIGHT IN KG:"))
num = float(input("ENTER THE HEIGHT IN METER"))

result = number / num** 2

if result <= 18.5:
    print("UNDERWEIGHT")
elif result >= 18.5 and result <=24.9:
 print ("NORMAL")
elif result >= 25 and result <=29.9 :
 print("OVERWEIGHT")
elif result >= 30:
 print("OBESE")
else:
  print("YOU NO GET BMI")
