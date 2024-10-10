def find_duplicates(student_ids):
    id_count = {}
    for student_id in student_ids:
        if student_id in id_count:
            id_count[student_id] += 1
        else:
            id_count[student_id] = 1
    duplicated_ids = [student_id for student_id, count in id_count.items() if count > 1]
    if duplicated_ids:
        affected_students = sum(count for count in id_count.values() if count > 1)
        print(f"Duplicated IDs: {', '.join(map(str, sorted(duplicated_ids)))}")
        print(f"Number of Students Affected: {affected_students}")
    else:
        print("No duplications.")
n = int(input("Enter number of students: "))
student_ids = list(map(int, input("Student IDs: ").split()))
find_duplicates(student_ids)