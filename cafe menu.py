menu={" Pizza":{"Margherita":100,"Farmhouse":150,"Paneer makhani":180},
      " Pasta":{"Arrabiata":150,"White sauce":100,"Red sauce":120},
      " Coffee":{"Espresso":55,"Cappucino":60,"Dalgona":70}}
print("Welcome to Jivi's Cafe\nHere's our menu:")
for item,subitems in menu.items():
    print(item)
    for order in subitems:
        print(f"\t {order}: {subitems[order]}")

bill=0
billrec={}
while True:
    a=input("Please enter your order...")
    for item,subitems in menu.items():
        for order in subitems:
            if order==a:
                main=a+item
                price=subitems[order]
    if main in billrec:
        billrec[main]+=price
    else:
        billrec[main]=price
    more=input(f"Order of {a} has been added. Do you want to add more? (y/n)")
    if more=="n":
        break
print("\nYour bill is:")
for item,price in billrec.items():
    bill+=price
    print(f"{item}: {price} Rs.")
print(f"\nYour total bill is {bill} Rs.\nThanks for visiting!")


    

