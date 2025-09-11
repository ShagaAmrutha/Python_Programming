def average_marks(marks):
    return sum(marks) / len(marks)

def top_performer(students):
    avg_dict = {}
    for name, marks in students.items():
        avg_dict[name] = round(average_marks(marks), 2)
    topper = max(avg_dict, key=avg_dict.get)
    return avg_dict, topper

students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

averages, topper = top_performer(students)
print("Average Marks:", averages)
print("Top Performer:",topper)