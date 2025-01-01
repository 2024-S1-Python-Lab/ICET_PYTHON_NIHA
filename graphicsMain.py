from graphics.rectangle import area as rect_area,perimeter as rect_perimeter
l=int(input("enter length of a rectangle:"))
b=int(input("enter breadth of a rectangle:"))
print("Rectangle - Area:",rect_area(l,b))
print("Perimmeter:",rect_perimeter(l,b))

from graphics.circle import area as circ_area,perimeter as circ_perimeter
r=float(input("enter radius of a circle:"))
print("Circle - Area:",circ_area(r))
print("Perimeter:",circ_perimeter(r))

from graphics.graphics3d.cuboid import area as cuboid_area,perimeter as cuboid_perimeter
l=int(input("enter the length of  cuboid:"))
b=int(input("enter breadth of a cuboid:"))
h=int(input("enter the heigth of  cuboid:"))
print("Cuboid - Area:",cuboid_area(l,b,h))
print("Cuboid - Perimeter:",cuboid_perimeter(l,b,h))

from graphics.graphics3d.sphere import area as sphere_area,perimeter as sphere_perimeter  
r=float(input("enter radius of a sphere:"))             
print("Circle - Area:",sphere_area(r))
print("Perimeter:",sphere_perimeter(r))        
