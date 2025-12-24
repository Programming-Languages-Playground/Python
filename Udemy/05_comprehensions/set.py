favorite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favorite_chais}
print(unique_chai)

recipies = {
    "Masala Chai": ["ginger", "cardmom", "clove"],
    "Elaichi Chai": ["cardmom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}
                           # list                               # iterating through the list
unique_spices = {spice for ingredients in recipies.values() for spice in ingredients}
print(unique_spices)

