def get_name(person):
    return person["name"]

def get_favourite_tv_show(tv_show):
    return tv_show["favourites"]["tv_show"]

def likes_to_eat(person, food):
    if food in person["favourites"]["snacks"]:
        return True
    return False

def add_friend(person, name):
    person["friends"].append(name)

def remove_friend(person, name):
    person["friends"].remove(name)

def total_money(list):
    monies = 0
    for money in list:
        monies += money["monies"]
    return monies

def lend_money(person1, person2, amount):
    person1_money = person1["monies"]
    person2_money = person2["monies"]
    person1_money -= amount
    person2_money += amount
    person1["monies"] = person1_money
    person2["monies"] = person2_money

def all_favourite_foods(list):
    favourite_foods = []
    i = 0
    for food in list["favourites"]["snacks"][i]:
        favourite_foods += food
    return favourite_foods





    


    

