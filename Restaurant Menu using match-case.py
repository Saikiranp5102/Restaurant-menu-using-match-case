print("-----Menu-----")
print("1. Biryani")
print("2. Chicken 65")
print("3. Veg Pulao")
print("4. Butter Chicken")
print("5. Paneer Tikka")
menu = int(input("Enter your choice :"))

match menu:
    case 1:
        print("Item         :   Biryani")
        print("Price        :   ₹250")
        print("Description  :   Fragrant basmathi rice cooked with rice and chicken")
    case 2:
        print("Item         :   Chicken 65")
        print("Price        :   ₹180")
        print("Description  :   Crispy and spicy deep fried chicken pieces")
    case 3:
        print("Item         :   Veg Pulao")
        print("Price        :   ₹220")
        print("Description  :   Fragrant saffron threads are delicately infused into the long-grain basmathi rice")
    case 4:
        print("Item         :   Butter Chicken")
        print("Price        :   ₹350")
        print("Description  :   Chicken tossed in a tangy, creamy, butterlicious tomato flavoured sauce")
    case 5:
        print("Item         :   Paneer Tikka")
        print("Price        :   ₹200")
        print("Description  :   Grilled paneer cubes marinated with spices and yogurt")
    case _:
        print("Sorry Nor available 🙁... Choose another item..!")