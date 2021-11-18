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
    

