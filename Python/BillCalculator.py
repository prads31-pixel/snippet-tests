# Question 2: Restaurant Bill Calculator 
#Service Charge: 10% of meal cost
#Amount after Service: Meal cost + Service charge
#Tax: 5% of amount after service
#Tip: 5% of amount after service
#Total Bill: Amount after service + Tax + Tip


def calculate_restaurant_bill(meal_cost):
    if type(meal_cost) not in [int, float] or meal_cost <= 0 :
        print("Error: Invalid meal cost")
        return False

    Service_Charge = 0.1 # 10% of meal cost
    tax_rate = 0.05  #5% tax
    tip_rate = 0.05  # 5% tip

    Amount_after_Service = meal_cost +(meal_cost * Service_Charge) # Amount after Service: Meal cost + Service charge
    tax = Amount_after_Service * tax_rate
    tip = Amount_after_Service * tip_rate
    total_bill = Amount_after_Service + tax + tip

    return {
        "meal_cost": meal_cost,
        "Service_Charge": Service_Charge * 100,
        "Amount_after_Service": Amount_after_Service,
        "Tax": tax,
        "Tip": tip,
        "Total_Bill": total_bill,
        "return": True
    }
 

print("Lets check the restaurant bill calculator function.")


#Output Format:
#Meal Cost: {meal_cost}
#Service Charge (10%): {service_charge}
#Amount after Service: {amount_after_service}
#Tax (5%): {tax}

#Tip (5%): {tip_amount}
#Total Bill: {total}

while True:
    meal_cost = float(input("Enter meal cost: "))
    result = calculate_restaurant_bill(meal_cost)
    if result and result.get("return"):
        print(f"Meal Cost: {result['meal_cost']}")
        print(f"Service Charge ({result['Service_Charge']}%): {result['Amount_after_Service'] - result['meal_cost']}")
        print(f"Amount after Service: {result['Amount_after_Service']}")
        print(f"Tax ({result['Tax']/result['Amount_after_Service']*100}%): {result['Tax']}")
        print(f"Tip ({result['Tip']/result['Amount_after_Service']*100}%): {result['Tip']}")
        print(f"Total Bill: {result['Total_Bill']}")
        break
    else:
        False