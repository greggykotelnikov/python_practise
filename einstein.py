def einstein(m):
    c = 3 * (10 ** 8)
    e = m * (c ** 2)
    return e 

def main():
    mass = int(input("Enter your mass in kilograms: "))
    print(f"The energy output from your mass is approximately equal to {einstein(mass)} joules")

main()