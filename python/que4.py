shop = {
    "apple": 5,
    "banana": 10
}
user_bought = 2
new_amount=shop.get("apple")-user_bought
shop["apple"]=new_amount
shop["orrange"]=20

print(shop)