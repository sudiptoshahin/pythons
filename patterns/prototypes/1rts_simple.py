

class Knight(object):

    def __init__(self, life: int, speed: int, attack_power: int, 
                attack_range: int, weapon: str)-> None:
        self.unit_type = "Knight"
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self) -> str:
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\n Attack power: {self.attack_power} \nAttack range: {self.attack_range}\nWeapon: {self.weapon}"
    

class Archer(object):

    def __init__(self, life: int, speed: int, attack_power: int, 
                attack_range: int, weapon: str)-> None:
        self.unit_type = "Archer"
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self) -> str:
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\n Attack power: {self.attack_power} \nAttack range: {self.attack_range}\nWeapon: {self.weapon}"
    

class Barracks(object):
    def generate_knight(self)-> Knight:
        return Knight(400, 5, 3, 1, "short sword")
    
    def generate_archer(self)-> Archer:
        return Archer(200, 7, 1, 5, "short bow")
    

if __name__ == "__main__":
    barracks = Barracks()
    kn1 = barracks.generate_knight()

    ar1 = barracks.generate_archer()

    print(f"[knight1] : {kn1}")
    print(f"[archer1] : {ar1}")