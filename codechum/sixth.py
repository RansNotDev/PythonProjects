import math
def sphere_surface_area_and_volume(diameter):
    radius = diameter / 2
    volume = (4 / 3) * math.pi * (radius ** 3)
    surface_area = 4 * math.pi * (radius ** 2)
    return volume, surface_area
diameter = float(input("Enter the diameter of the sphere: "))
volume, surface_area = sphere_surface_area_and_volume(diameter)
print(f"Surface Area of the sphere: {surface_area:.2f}")
print(f"Volume of the sphere: {volume:.2f}")