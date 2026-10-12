
# Student result maker

print("🎓 STUDENT RESULT MAKER")
print("-" * 30)

# Take student's name
name = input("Enter student name: ")

# Take marks for 3 subjects
maths = float(input("Enter Maths marks (out of 100): "))
science = float(input("Enter Science marks (out of 100): "))
english = float(input("Enter English marks (out of 100): "))

# Check whether marks are valid
if not (0 <= maths <= 100 and
        0 <= science <= 100 and
        0 <= english <= 100):

    print("Invalid marks! Enter marks between 0 and 100.")

else:
    # Calculate total and percentage
    total = maths + science + english
    percentage = total / 3

    # Calculate grade and result
    if maths < 35 or science < 35 or english < 35:
        grade = "F"
        result = "Fail"

    elif percentage >= 90:
        grade = "A+"
        result = "Pass"

    elif percentage >= 80:
        grade = "A"
        result = "Pass"

    elif percentage >= 70:
        grade = "B"
        result = "Pass"

    elif percentage >= 60:
        grade = "C"
        result = "Pass"

    elif percentage >= 35:
        grade = "D"
        result = "Pass"

    # Display the report card
    print("\n" + "=" * 30)
    print("         REPORT CARD")
    print("=" * 30)

    print("Student Name:", name)
    print("Maths Marks:", maths)
    print("Science Marks:", science)
    print("English Marks:", english)

    print("-" * 30)
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)
    print("=" * 30)
