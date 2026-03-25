sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

powers = {(1, 2, 4, 8, 16): 2, (1, 3, 9, 27, 81): 3}

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}
my_empty_dictionary = {}

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["cheesecake"] = 8

animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo["horses"] = 2

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})

menu["oatmeal"] = 5

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(students)
print(library)