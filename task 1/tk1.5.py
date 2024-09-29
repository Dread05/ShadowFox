class avengers:
    def __init__(self, name, age, gender, sp,weapon,leader=False):
        self.name=name
        self.age=age
        self.gender=gender
        self.sp=sp
        self.weapon=weapon
        self.leader=leader
    def info(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Super Power: {self.sp}\n"
                f"Weapon: {self.weapon}\n"
                f"Leader: {'Yes' if self.leader else 'No'}\n")
sh = [
    avengers("Captain America", 100, "Male", "Super Strength", "Shield", True),
    avengers("Iron Man", 48, "Male", "Technology", "Armor"),
    avengers("Black Widow", 35, "Female", "Superhuman", "Batons"),
    avengers("Hulk", 45, "Male", "Unlimited Strength", "No Weapon"),
    avengers("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    avengers("Hawkeye", 40, "Male", "Fighting Skills", "Bow and Arrows")
]
for hero in sh:
    print(hero.info())