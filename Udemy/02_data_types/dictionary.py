chai_ingredients = dict(type= "masala chai", sweetness= 3, base= "milk")
print(f"Chai ingredients are: {chai_ingredients}")
print(chai_ingredients.keys())

chai = {}
chai["type"] = "elaichi"
chai["base"] = "milk"

print(f"Chai consists of: {chai}")
print(chai.keys())
print(chai.values())
print(chai.items())
print(chai.popitem())
print(chai.items())

customer_note = chai.get("customer_note", "no_note")
print(customer_note)