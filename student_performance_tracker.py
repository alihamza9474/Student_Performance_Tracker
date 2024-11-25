



# Step 1: Define the Student Class
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores  # List of integers representing scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)


# Step 2: Define the PerformanceTracker Class
class PerformanceTracker:
    def __init__(self):
        self.students = {}  # Dictionary to store student objects by name

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0  # Avoid division by zero if no students exist
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        print("\n--- Student Performance ---")
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Student: {name}, Average: {average:.2f}, Status: {status}")
        class_average = self.calculate_class_average()
        print(f"\nClass Average: {class_average:.2f}")


# Step 3: Handle User Input
def main():
    tracker = PerformanceTracker()

    while True:
        # Input student data
        name = input("Enter student's name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break

        scores = []
        for subject in ["Math", "Science", "English"]:
            while True:
                try:
                    score = int(input(f"Enter {name}'s score in {subject}: "))
                    scores.append(score)
                    break
                except ValueError:
                    print("Invalid input! Please enter a numeric score.")

        tracker.add_student(name, scores)

    # Step 4: Calculate and Display Performance
    tracker.display_student_performance()


# Run the program
if __name__ == "__main__":
    main()
