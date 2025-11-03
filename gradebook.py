# =========================================================
# Author: Navya Kumar
# Roll No: 2501410054
# Date: 3 November 2025
# =========================================================

import csv

def avg_score(marks_data):
#Calculating avg
    total_marks = sum(marks_data.values())
    num_students = len(marks_data)
    return total_marks / num_students if num_students else 0

def median_score(marks_data):
    #Calculating median marks
    sorted_marks = sorted(marks_data.values())
    n = len(sorted_marks)
    if n == 0:
        return 0
    mid = n // 2
    return (sorted_marks[mid - 1] + sorted_marks[mid]) / 2 if n % 2 == 0 else sorted_marks[mid]

def highest_score(marks_data):
    #Return the highest mark.
    return max(marks_data.values()) if marks_data else None

def lowest_score(marks_data):
    #Return the lowest mark.
    return min(marks_data.values()) if marks_data else None

#Function to assign grades based on marks.
def grade_allocator(marks_data):
    #Assign grades based on marks.
    results = {}
    for student, score in marks_data.items():
        if score >= 90:
            results[student] = 'A'
        elif score >= 80:
            results[student] = 'B'
        elif score >= 70:
            results[student] = 'C'
        elif score >= 60:
            results[student] = 'D'
        else:
            results[student] = 'F'
    return results

def grade_summary(grade_data):
    #Return a dictionary of grade counts.
    summary = {g: 0 for g in ['A', 'B', 'C', 'D', 'F']}
    for g in grade_data.values():
        summary[g] += 1
    return summary

#Assigning pass or fail
def filter_pass_fail(marks_data):
    #Splitting students into passed and failed lists.
    passed_students = [n for n, s in marks_data.items() if s >= 40]
    failed_students = [n for n, s in marks_data.items() if s < 40]
    return passed_students, failed_students

# File handling
def import_csv(file_name):
    #Read student data from a CSV file.
    records = {}
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header if any
            for row in reader:
                if len(row) == 2:
                    name, score = row[0].strip(), row[1].strip()
                    try:
                        records[name] = float(score)
                    except ValueError:
                        print(f"⚠️ Invalid score for {name}, skipping.")
        if not records:
            print("No valid entries found.")
        else:
            print(f"\n✅ Imported {len(records)} student records from '{file_name}'.")
    except FileNotFoundError:
        print("❌ File not found! Check your filename.")
    return records

#Display function
def show_table(marks_data, grade_data):
    #Display formatted student results
    print("\n" + "-" * 50)
    print(f"{'Student Name':<20}{'Marks':<10}{'Grade':<10}")
    print("-" * 50)
    for name, score in marks_data.items():
        print(f"{name:<20}{score:<10.1f}{grade_data[name]:<10}")
    print("-" * 50)

#Main Program
def main():
    print("===== ACADEMIC PERFORMANCE EVALUATOR =====")

    while True:
        print("\n1. Enter Data Manually")
        print("2. Import from CSV File")
        print("3. Exit")
        option = input("Select an option (1-3): ")

        marks_data = {}

        if option == '1':
            try:
                count = int(input("\nEnter number of students: "))
                for i in range(count):
                    student = input(f"Enter name of student {i + 1}: ")
                    score = float(input(f"Enter marks for {student}: "))
                    marks_data[student] = score
            except ValueError:
                print("Invalid input! Try again.")
                continue

        elif option == '2':
            filename = input("\nEnter CSV filename (include .csv): ")
            marks_data = import_csv(filename)

        elif option == '3':
            print("\nProgram terminated. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
            continue

        if not marks_data:
            continue

        #Analytics
        avg = avg_score(marks_data)
        med = median_score(marks_data)
        high = highest_score(marks_data)
        low = lowest_score(marks_data)
        grades = grade_allocator(marks_data)
        dist = grade_summary(grades)
        passed, failed = filter_pass_fail(marks_data)

        #Display
        show_table(marks_data, grades)

        print("\n STATISTICAL OVERVIEW:")
        print(f"Average Marks: {avg:.2f}")
        print(f"Median Marks: {med:.2f}")
        print(f"Highest Marks: {high}")
        print(f"Lowest Marks: {low}")

        print("\n GRADE SUMMARY:")
        for grade, num in dist.items():
            print(f"{grade}: {num}")

        print("\n PASS/FAIL REPORT:")
        print(f"Passed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
        print(f"Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")

if __name__ == "__main__":
    main()
