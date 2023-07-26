def grade(marks):
    if marks >= 90:
        return "A+"
    elif 80 <= marks <=89:
        return "A"
    elif 70 <= marks <=79:
        return "B"
    elif 60 <= marks <=69:
        return "C"
    elif 50 <= marks <=59:
        return "D"
    else:
        return "Fail"
def main():
    while True:
        try:
            marks = int(input("Enter marks(0 to 100): "))
            if 0 <= marks <=100:
                grades = grade(marks)
                print(f"The student grade is: {grades}")
            else:
                print("Invalid Input! Please enter the marks between 0 to 100")
        except ValueError:
            print("Invalid Input! Enter a valid input. ")

        choice = input("Do you want to calculate the grade for other student? (y/n): ").lower()
        if choice != 'y':
            break
if __name__ == "__main__":
    print("Welcome to the student grading program!")
    main()

