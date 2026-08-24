#inputs we need from the users 
#total rent 
#total food ordered from the snacking
#electricity units spend 
#charge per unit 
#persons living in a room 

##outputs
#total amount you have to pay is 
rent=int(input("Enter the rent of your flat/hostel:"))
food=int(input("Enter the amount of your food you ordered:"))
electricity=int(input("Enter the total amount of electricity spend:"))
charge_per_unit=int(input("Enter the total charge per unit:"))
persons=int(input("Enter the number of persons living in a room:"))

total_bill=electricity*charge_per_unit

amount_to_pay_by_each_person=(rent + food + total_bill)//persons
print("each person will pay:",amount_to_pay_by_each_person)
