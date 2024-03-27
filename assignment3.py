# No.1
original_price  = 100
discount_percentage = 25

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price
    
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after discount", final_price)

# No.2
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)

if final_price == original_price:
    print("No discount applied. Final price:", original_price)
else:
    print("Final price after discount:", final_price)   