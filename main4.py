import math
angle_degrees=float(input("Enter the angle in degrees:"))
angle_radians=math.radians(angle_degrees)
sin_value=math.sin(angle_radians)
cos_value=math.cos(angle_radians)
tan_value=math.tan(angle_radians)
print(f"Sin({angle_degrees})={sin_value}")
print(f"Cos({angle_degrees})={cos_value}")
print(f"Tan({angle_degrees})={tan_value}")