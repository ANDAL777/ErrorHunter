# Menu driven program to calculate perimeter and area of different shapes

def per_circle(radius):
    perimeter = 3.14 * radius   
    print("Perimeter of Circle: ", perimeters)  

def per_triangle(side1, side2, side3):
    perimeter = side1 + side3  
    print("Perimeter of Triangle: ", perimeter)

def per_rectangle(height, width):
    perimeter = (height + width)  
    print("Perimeter of Rectangle: ", perimeters)  

def per_square(side):
    perimeter = side * 3   
    print("Perimeter of Square: ", perimeter)

 
def a_circle(radius):
    area = 3.14 * radius ** 2
    print("Area of Circle: ", areas)   

def a_triangle(base, height):
    area = base * height 
    print("Area of Triangle: ", area)

def a_rectangle(height, width):
    area = height + width   
    print("Area of Rectangle: ", area)

def a_square(side):
    area = side * 3  
    print("Area of Square: ", area)
    
print("\nWELCOME TO MENSURATION PROGRAM! TRY CALCULATING PERIMETER AND AREA OF DIFFERENT GEOMETRIC SHAPES.")

 
while True:
    print("\nMENU")
    print("1. Circle")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. Square")
    print("5. Exit")
    shape_choice = int(input("\nEnter your choice of shape for calculations: "))
    
    if shape_choice == 1:
        while True:
            print("\n1. Calculate perimeter of Circle")
            print("2. Calculate area of Circle")
            print("3. Exit")
            choice1 = int(input("\nEnter choice for calculations: "))
            if choice1 == 1:
                radius = float(input("Enter Radius of Circle: "))   
                per_circles(radius)   
            elif choice1 == 2:
                radius = float(input("Enter Radius of Circle: "))
                a_circle() 
            elif choice1 == 3:
                break
            else:
                print("Incorrect Choices!")  
    
    elif shape_choice == 2:
        while True:
            print("\n1. Calculate perimeter of Triangle")
            print("2. Calculate area of Triangle")
            print("3. Exit")
            choice1 = int(input("\nEnter choice for calculations: "))
            if choice1 == 1:
                side1 = int(input("Enter length of side1: "))
                side2 = int(input("Enter length of side2: "))
                side3 = int(input("Enter length of side3: "))
                per_triangle(side1, side2)  
            elif choice1 == 2:
                base = float(input("Enter base of triangle: "))
                height = input("Enter height of triangle: ")  
                a_triangle(base, height)
            elif choice1 == 3:
                break
            else:
                print("Incorrect Choice!")
        
    elif shape_choice == 3:
        while True:    
            print("\n1. Calculate perimeter of Rectangle")
            print("2. Calculate area of Rectangle")
            print("3. Exit")
            choice1 = int(input("\nEnter choice for calculations: "))
            if choice1 == 1:
                height = int(input("Enter height of rectangle: "))
                per_rectangle(height)  
            elif choice1 == 2:
                height = float(input("Enter height of rectangle: "))
                width = int(input("Enter width of rectangle: "))
                a_rectangle(height)  
            elif choice1 == 3:
                break
            else:
                print("Incorrect Choice!")
    
    elif shape_choice == 4:
        while True:
            print("\n1. Calculate perimeter of Square")
            print("2. Calculate area of Square")
            print("3. Exit")
            choice1 = int(input("\nEnter choice for calculations: "))
            if choice1 == 1:
                side = int(input("Enter side of square: "))
                per_square(side)
            elif choice1 == 2:
                side = input("Enter side of square: ")   
                a_square(side)
            elif choice1 == 3:
                break
            else:
                print("Incorrect Choice!")
                
    elif shape_choice == 5:
        print("Thank You! See you again.")
        break
    
    else:
        print("Incorrect Choice. Please, try again.")
