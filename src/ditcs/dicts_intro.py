
fruit_basket = {
    "apple": 5,
    "banana": 3,
    "orange": 8,
    "grape": 2,
    "kiwi": 4,
}

vegetable_basket = {
    "carrot": 6,
    "broccoli": 4,
    "spinach": 7,
    "potato": 5,
    "tomato": 8,
}



try:
    print(fruit_basket["mango"])
except Exception as e:
    print("Key not found in the dictionary")


print(fruit_basket.get("mango", "Key not found in the dictionary"))


#merge two dicts

shopping_basket = fruit_basket | vegetable_basket

for k, v in shopping_basket.items():
    print(f"{k}: {v}")


first_item = shopping_basket.popitem()

print(f"First item: {first_item}")

print (type(first_item))