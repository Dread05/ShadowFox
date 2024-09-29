js=["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
length=(len(js))
print(length)

js.append("Batgirl")
js.append("Nightwing")
print(js)

def lc(js,element):
    return [ item for item in js if item==element ] + [item for item in js if item !=element]

element="WonderWoman"
print(lc(js,element))

move=js.index("Superman")
ele=js.pop(move)
new_position=3
js.insert(new_position,ele)
print(js)

js.clear()
js.extend(["Cyborg","Shazam","Hawkgirl","MartianManhunter","Green Arrow"])

js.sort()
print(js)

