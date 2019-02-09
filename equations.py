def write_to_file(data):
    filename = "coords.txt"
    fh = open(filename, "w")
    fh.write(data)
    fh.close()

def quadratic(a, b, c):
    return lambda x: a*x*x + b*x + c

def quad_eq(a, b, c):
    eq = "y = "
    eq += "-" if a < 0 else ""                      # if a is positive or negaive
    eq += str(abs(a)) if a not in [1, -1] else ""   # only show a if not 1 or -1
    eq += "x" + chr(178)                            # x squared
    eq += " + " if b>=0 else " - "                  # plus or minus sign before b
    eq += str(abs(b))                               # b without sign
    eq += " + " if c>=0 else " - "                  # plus or minus sign before c
    eq += str(abs(c))                               # c without sign
    return eq

def linear(a, b):
    return lambda x: a*x + b

def line_eq(a, b):
    eq = "y = "
    eq += "-" if a < 0 else ""                      # if a is positive or negaive
    eq += str(abs(a)) if a not in [1, -1] else ""   # only show a if not 1 or -1
    eq += "x"                                       # x 
    eq += " + " if b>=0 else " - "                  # plus or minus sign before b
    eq += str(abs(b))                               # b without sign
    return eq

def choose_equation():
    choice = int(input("Choose 1 for linear, 2 for quadratic: "))
    while choice not in [1, 2]:
        choice = int(input("Choose 1 or 2: "))
    return choice

def get_coefficients(choice):
    eq_line = "y = ax + b"
    eq_quad = "y = ax{} + bx + c".format(chr(178))
    print("Input values for the function {}".format(eq_line if choice == 1 else eq_quad))
    a = int(input("a: "))
    b = int(input("b: "))
    if choice == 2:
        c = int(input("c: "))
    if choice == 1:
        return (a, b)
    else:
        return (a, b, c)

def get_xrange():
    print("Input range for x")
    min = int(input("min: "))
    max = int(input("max: "))
    while max <= min:
        max = int(input("max must be greater than min: "))
    return (min, max + 1)

def do_everything():
    choice = choose_equation()
    values = get_coefficients(choice)
    xminmax = get_xrange()
    if choice == 1:
        f = linear(*values)
        eq = line_eq(*values)
    else:
        f = quadratic(*values)
        eq = quad_eq(*values)

    xs = list(range(*xminmax))
    ys = [f(x) for x in xs]
    print()
    print("Equation : ", eq)
    print("x: ", xs)
    print("y: ", ys)

    file_data = str(xs) + "\n" + str(ys) + "\n" + eq
    write_to_file(file_data)

if __name__ == "__main__":
    again = "y"
    while again == "y":
        do_everything()
        input("\nPress enter to view graph")
        execfile("graphs.py")
        again = input("Another graph? (y/n): ")
