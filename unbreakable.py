# Error handle

# ZeroDivisionError - divide by zero

# ValueError - right type biut wrong value

# KeyError - dictionary key does not exist

# Unbreakable Student Marks Checker

while True:
    try:
        marks = int(input("Enter student marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
        else:
            break

    except ValueError:
        print("Please enter numbers only.")

print("Student marks:", marks)