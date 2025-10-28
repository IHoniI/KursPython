def make_ruler(length):
    line1 = "|"
    line2 = "0"

    for i in range(1, length+1):
        line1 += "....|"
        tmp = f"{i:>5}"
        line2 += tmp

    out = line1+"\n"+line2
    return out


def make_grid(x, y):
    line1 = "---".join("+" for n in range(y+1))
    line2 = "   ".join("|" for n in range(y+1))

    lines = line1+"\n"+line2
    out = "\n".join(lines for _ in range(x))

    out += "\n"+line1

    return out

