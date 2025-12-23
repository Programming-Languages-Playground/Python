def add_vat(amount, vatRate):
    return amount * (100 + vatRate)/100

orders = [100, 200, 300]

for order in orders:
    finalVat = add_vat(order, 10)
    print(f"Original Price: {order}, Final with VAT: {finalVat}")

# Scopes 

# nonlocal 

def updateOrder():
    chai_type = "Elaichi"

    def kitchen():
        # nonlocal - just above the function
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

updateOrder()

# global

chai_type = "plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "irani"
    kitchen()
    print(f"After updating chai type, chaitype: {chai_type}")

front_desk()

# positional vs keywords

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") # positional
make_chai(tea="Green", sugar="Extra", milk="Yes") # keywords

# args vs kwargs

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinamon", "Cardmom", sweetner="Honey", foam="yes")
