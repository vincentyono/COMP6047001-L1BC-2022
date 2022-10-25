px = int(input("Enter the point px: "))
py = int(input("Enter the point py: "))
qx = int(input("Enter the point qx: "))
qy = int(input("Enter the point qy: "))

rx = (qx - px) + qx
ry = (qy - py) + qy

print(f"the point r = ({rx, ry})")
