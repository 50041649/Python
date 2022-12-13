#This application will calculate the commission of car sales.

#Ask the user to enter the value of the car they have sold.
CarCost = input("How much did the car cost? £")

#Print the value entered
print("The car sold for £" + str(CarCost))
print()

#Calculate the commission based on the sale of value
#Less than £1000 = 1.5%
#Less than £2000 = 2.5%
#Less than £3000 = 5%
#Greater than £3000 = 7.5%

#Create an IF ELSE to calculate commission
if(float(CarCost) <= 1000.00):
  print("The commission rate is 1.5%")
  CommissionRate = 1.5
elif(float(CarCost) <=2000.00):
  print("The commission rate is 2.5%")
  CommissionRate = 2.5
elif(float(CarCost) <=3000.00):
  print("The commission rate is 5%")
  CommissionRate = 5
else:
  print("The commission rate is 7.5%")
  CommissionRate = 7.5

CommissionValue = float(CommissionRate) / 100 * float(CarCost)

print("The commission rate is" + str(CommissionRate) + "%")
print("The commssion value is £" + str(CommissionValue))