# STRING to INT
age = "30"
print(type(age))
ageCast = int(age)
print(type(ageCast))
# int("50") works
# int("Deb") wont work
print("My age is " + age + " but next year I will be " + str(int(age)+1))
# STRING to Float
ageFloat = "30"
print(type(age))
ageFloatCast = float(age)
print(type(ageFloatCast))
print(ageFloatCast)
# STRING to BOOL
# Also long as there is symbolic value (value other than 0) in it, it will be True. If there is no data in it, it will be False
age = "30"
print(type(age))
ageBoolCast = bool(age)
print(type(ageBoolCast))
print(ageBoolCast)
# INT to  String
age = 30
print(type(age))
ageStringCast = str(age)
print(type(ageStringCast))
print(ageStringCast)
# INT to Float
age = 30
print(type(age))
ageFloatCast = float(age)
print(type(ageFloatCast))
print(ageFloatCast)
# INT to BOOL
age = 0
print(type(age))
ageBool = bool(age)
print(type(ageBool))
print(ageBool)
# Float to INT
price = 4.99
print(type(price))
priceINT = int(price)
print(type(priceINT))
print(priceINT)
# it is not rounding, it is simply striping off the values
# Float to BOOL
price = 0.99
print(type(price))
priceBool = bool(price)
print(type(priceBool))
print(priceBool)
# Float to String
price = 0.99
print(type(price)) 
priceString= str(price)
print(type(priceString))
print(priceString)
# BOOL to String
broke = True
print(str(broke))
# BOOL to INT
broke = False
print(int(broke))
# BOOL to Float
broke = True
print(float(broke))
