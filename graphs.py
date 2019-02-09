import os
import matplotlib.pyplot as plt

def get_from_file(f):
    contents = []
    fh = open(f)
    for line in fh:
        contents.append(line)
    fh.close()
    return contents

filename = "coords.txt"
data = get_from_file(filename)

xs = eval(data[0])
ys = eval(data[1])
eq = data[2]
xmin = min(xs)
xmax = max(xs)
ymin = min(ys) - 5
ymax = max(ys) + 5

plt.plot(xs, ys, "b-")
plt.axis([xmin, xmax, ymin, ymax])
plt.title(eq)
plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.show()
