
def trilaterate(dataset : list) -> list:

    # dataset to variables
    x1, y1, r1 = dataset[0]
    x2, y2, r2 = dataset[1]
    x3, y3, r3 = dataset[2]

    # calculate system coefficients
    A = 2*x2 - 2*x1
    B = 2*y2 - 2*y1
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2

    D = 2*x3 - 2*x2
    E = 2*y3 - 2*y2
    F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2

    # calculate coordinates for system solution
    x = (C*E - F*B) / (E*A - B*D)
    y = (C*D - A*F) / (B*D - A*E)

    return x, y
