# h=float(input("Enter Height in meters: "))
# w=float(input("Enter weight in Kilograms: "))
# bmi=w/(h**2)
# print(bmi)
# if bmi>=30:
#     print("Obesity")
# elif bmi>=25:
#     print("Overweight")
# elif bmi>=18.5:
#     print("Normal")
# else:
#     print("Underweight")

au=["sydney","melbourne","Brisbane","Perth"]
uae=["Dubai","Abu Dhabi","Sharjah","Ajman"]
india=["Mumbai","Bangalore","Chennai","Delhi"]
name=input("Enter city name: ")
# if name in au:
#     print("The city ",name,"belongs to Australia")
# if name in uae:
#     print("The city ",name,"belongs to UAE")
# else:
#     print("The city ",name,"belongs to India")
name1=input("Enter second city name: ")
if name in au and name1 in au:
    print("Both cities are in Australia")
elif name in uae and name1 in uae:
    print("Both cities belong in UAE")
elif name in india and name1 in india:
    print("Both cities belong in India")
else:
    print("They dont belong in same country")