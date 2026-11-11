name = input("Enter item name: ")

try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    total = price + quantity

    print("total bill", total) 



except:
    print("Invalid input enter numbers only")