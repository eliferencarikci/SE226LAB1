import geometry_utils

def main():
    shape_functions = {
        "circle": geometry_utils.circle_area,
        "rectangle": geometry_utils.rectangle_area,
        "triangle": geometry_utils.triangle_area
    }

    print(" Shape Area Calculator ")
    shape_type = input("Enter shape type (circle, rectangle, triangle): ").lower().strip()

    if shape_type not in shape_functions:
        print(f"Error: '{shape_type}' is not a valid shape.")
        return

    try:
        if shape_type == "circle":
            radius = float(input("Enter radius: "))
            area = shape_functions["circle"](radius)
            
        elif shape_type == "rectangle":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            area = shape_functions["rectangle"](width, height)
            
        elif shape_type == "triangle":
            base = float(input("Enter base length: "))
            height = float(input("Enter height: "))
            area = shape_functions["triangle"](base, height)

        print(f"The area of the {shape_type} is: {area:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")

if __name__ == "__main__":
    main()