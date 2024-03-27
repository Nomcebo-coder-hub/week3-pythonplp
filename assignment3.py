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

