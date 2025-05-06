import argparse
from quadratic.solver import QuadraticEquation

def main():
    parser = argparse.ArgumentParser(description="Résout une équation quadratique ax² + bx + c = 0")
    parser.add_argument("a", type=float, help="Coefficient a")
    parser.add_argument("b", type=float, help="Coefficient b")
    parser.add_argument("c", type=float, help="Coefficient c")
    args = parser.parse_args()

    try:
        equation = QuadraticEquation(args.a, args.b, args.c)
        x1, x2 = equation.solve()
        print(f"Les solutions sont : x1 = {x1}, x2 = {x2}")
    except ValueError as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
