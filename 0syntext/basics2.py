from typing import List

def find_cube_root(x: int) -> int:
    ans: int = 0
    while ans**3 < abs(x):
        print(f"Value of the decrementing function abs(x) - ans**3 is {abs(x) - ans**3}")
        ans = ans + 1
    if ans**3 != abs(x):
        print(f"{x} is not a perfect cube.")
    else:
        if x < 0:
            ans = -ans
        print(f"Cube root of {x} is {ans}")

def rootPwr(num: int) -> List[int]:
    root: float = num ** 0.5
    pwr: int
    


if __name__ == '__main__':
    # find the cube root of a perfect cube
    x: int = int(input("Enter a number: "))
    # print(find_cube_root(x))
    i = 0
    while i < x:
        i = i + 1
    print(i)