from math import sqrt

u = [5, 2, 3]
v = [4, 2, 1]

vektorovySoucin = [u[1]*v[2] - u[2]*v[1], u[2]
                   * v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]]
print(vektorovySoucin)

skalarniSoucin = u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
print(skalarniSoucin)

delkaW = sqrt(vektorovySoucin[0]**2 +
              vektorovySoucin[1]**2 + vektorovySoucin[2]**2)
print(delkaW)
