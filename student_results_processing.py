def calculate_final(coursework, exam):
    return coursework * 0.40 + exam * 0.60


def classify(mark):
    if mark >= 70:
        return "Distinction"
    elif mark >= 60:
        return "Credit"
    elif mark >= 50:
        return "Pass"
    else:
        return "Fail"


def valid_registration(registration):
    return (
        len(registration) == 5
        and registration[:2] == "VU"
        and registration[2:].isdigit()
    )


def process_students():
    students = {}

    try:
        count = int(input("Number of students: "))
    except ValueError:
        print("Number of students must be numeric")
        return

    if count <= 0:
        print("Number of students must be greater than zero")
        return

    for i in range(count):

        print("\nStudent", i + 1)

        registration = input("Registration number: ")

        if not valid_registration(registration):
            print("Invalid registration number")
            continue

        if registration in students:
            print("Duplicate registration number")
            continue

        name = input("Student name: ")

        try:
            coursework = float(input("Coursework mark: "))
            exam = float(input("Examination mark: "))
        except ValueError:
            print("Marks must be numeric")
            continue

        if coursework < 0 or coursework > 100:
            print("Coursework mark must be between 0 and 100")
            continue

        if exam < 0 or exam > 100:
            print("Examination mark must be between 0 and 100")
            continue

        final_mark = calculate_final(coursework, exam)
        classification = classify(final_mark)

        students[registration] = {
            "name": name,
            "coursework": coursework,
            "exam": exam,
            "final_mark": final_mark,
            "classification": classification
        }

    print("\nSTUDENT RESULTS")

    for registration, student in students.items():
        print(
            registration,
            student["name"],
            "| Coursework:", student["coursework"],
            "| Exam:", student["exam"],
            "| Final:", round(student["final_mark"], 2),
            "| Classification:", student["classification"]
        )


process_students()