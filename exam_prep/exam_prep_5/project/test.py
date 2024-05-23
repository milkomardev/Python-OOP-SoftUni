from project.concert_tracker_app import ConcertTrackerApp

musician_types = ["Singer", "Drummer", "Guitarist", "Singer"]
names = ["George", "Alex", "Lilly", "Pesho"]

app = ConcertTrackerApp()

for i in range(4):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))
print(app.musicians[3].learn_new_skill("sing high pitch notes"))

print(app.create_band("RockName"))
print(app.create_band("RockName2"))

for i in range(4):
    print(app.add_musician_to_band(names[i], "RockName"))

print(app.bands[0].__str__())


print(app.create_concert("Rock", 1, 1, 2, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))
print(app.start_concert("Sofia", "RockName"))
