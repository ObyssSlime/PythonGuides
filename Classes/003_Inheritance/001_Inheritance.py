class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class HeroTank(Hero):
    pass

class HeroSupport(Hero):
    pass

hilda = HeroTank("Hilda", 6000)
nana = HeroSupport("Nana", 1200)

print(f"Hero name {hilda.name}, HP {hilda.hp}")
print(f"Hero name {nana.name}, HP {nana.hp}")
