
from typing import Union
import os

class Knight(object):
    def __init__(self, level: int) -> None:
        self.unit_type = "knight"
        filename: str = f"{self.unit_type}_{level}.dat"
        filename_abs: str = os.path.join(os.getcwd(), filename)

        with open(filename_abs, "r", encoding="utf-8") as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\n Attack power: {self.attack_power} \nAttack range: {self.attack_range}\nWeapon: {self.weapon}"

class Archer(object):

    def __init__(self, level: int) -> None:
        self.unit_type: str = "archer"
        filename: str = f"{self.unit_type}_{level}.dat"
        filename_abs: str = os.path.join(os.getcwd(), filename)

        with open(filename_abs, "r", encoding="utf-8") as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]
    
    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\n Attack power: {self.attack_power} \nAttack range: {self.attack_range}\nWeapon: {self.weapon}"
    

class Barracks(object):
    def build_unit(self, unit_type, level: int) -> Union[Knight, Archer]:
        if unit_type == "knight":
            return Knight(level=level)
        else:
            return Archer(level=level)
        

if __name__ == '__main__':
    barracks = Barracks()
    kn1 = barracks.build_unit("knight", 1)
    ar1 = barracks.build_unit("archer", 1)

    print(f"[Knight1]: {kn1}")
    print(f"[archer1]: {ar1}")