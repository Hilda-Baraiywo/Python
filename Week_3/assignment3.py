def claculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = claculate_discount(price, discount_percent)
    
print("Final price:", final_price)
    
