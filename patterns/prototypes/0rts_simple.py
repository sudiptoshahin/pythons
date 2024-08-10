
class Knight(object):
    def __init__(self, life: int, speed: int, attack_power: int, 
                attack_range: int, weapon: str)-> None:
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self) -> str:
        return f"Life: {self.life}\nSpeed: {self.speed}\n Attack power: {self.attack_power} \nAttack range: {self.attack_range}\nWeapon: {self.weapon}"


class Barracks(object):
    """ create barracks """
    def generate_knight(self) -> Knight:
        """generate knight"""
        return Knight(400, 5, 3, 1, "short sword")
    

if __name__ == "__main__":
    barracks = Barracks()
    kn1 = barracks.generate_knight()
    print(f"[knight1]: {kn1}")