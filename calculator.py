
print("Attempting to buy a new car in Lebanon from three different areas, each offering a specific price.") 
print("Searching for a 1974 Volkswagen Beetle.")
print("The three areas are Beirut, Tripoli and Bekaa")
Beirut = 7000 
Tripoli = 3200
Bekaa = 4100
print("South is currently unreachable")
print("After checking the car in Beirut, we told the owner we need a discount since the car requires registration")
print("this requires a discount of 1500")
new_beirut_car_price = Beirut - 1500
print("New price for Beirut Beetle:", new_beirut_car_price)
print("After checking the car in Tripoli, the price seemed fair but the car requires a new set of 4 wheels and new roof and locks")
print("We agreed with the owner to remove 200 from the main price")
new_tripoli_car_price = Tripoli - 200
print("New price for Tripoli Beetle:", new_tripoli_car_price)
print("Attempted to check the Bekaa car but Israel bombed the main highways, so I was unable to check it")
print("Me and my sibling agreed that we will buy the Tripoli car and divide the main price between us")
each_person_will_be_paying = new_tripoli_car_price / 2
print("Each person will be paying:", each_person_will_be_paying)
print("The 4 wheels in total were 50 each")
total_of_wheels = 50 * 4
print("Total cost of wheels:", total_of_wheels)
final_price = each_person_will_be_paying + total_of_wheels
print("Final price for each person after adding the wheels:", final_price)

print("This calculated scenario has been created by Asmahan")