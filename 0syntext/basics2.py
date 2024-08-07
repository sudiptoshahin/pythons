

def find_cube_root(x: int) -> int:
    ans: int = 0
    while ans**3 < abs(x):
        ans = ans + 1
    if ans**3 != abs(x):
        print(f"{x} is not a perfect cube.")
    else:
        if x < 0:
            ans = -ans
        print(f"Cube root of {x} is {ans}")


if __name__ == '__main__':
    # find the cube root of a perfect cube
    x: int = int(input("Enter a number: "))
    print(find_cube_root(x))