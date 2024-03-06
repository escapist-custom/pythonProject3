d = int(input())
v1 = int(input())
v2 = int(input())
t = int(input())

d_f = (v1 * t - (v1 * t // d) * d)
d_z = (v2 * t - (v2 * t // d) * d)

if d_f > d_z:
    print(d_f - d_z)
else:
    print(d_z - d_f)
