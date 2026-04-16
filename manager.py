import json
import os
from student import Student

FILE = "students.json"

class StudentManager:
    def __init__(self):
        self.students = []
        self.load()

    def load(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                data = json.load(f)
                self.students = [Student.from_dict(s) for s in data]

    def save(self):
        with open(FILE, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=2)

    def id_exists(self, student_id):
        return any(s.student_id == student_id for s in self.students)

    def add(self, student_id, name, grade):
        if self.id_exists(student_id):
            print(f"❌ ID '{student_id}' already exists.")
            return
        self.students.append(Student(student_id, name, grade))
        self.save()
        print(f"✅ Student '{name}' added.")

    def update(self, student_id, name=None, grade=None):
        for s in self.students:
            if s.student_id == student_id:
                if name: s.name = name
                if grade: s.grade = grade
                self.save()
                print(f"✅ Student '{student_id}' updated.")
                return
        print(f"❌ Student ID '{student_id}' not found.")

    def delete(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                self.save()
                print(f"🗑️ Student '{student_id}' deleted.")
                return
        print(f"❌ Student ID '{student_id}' not found.")

    def list_all(self):
        if not self.students:
            print("📭 No students found.")
            return
        print("\n" + "="*40)
        print(f"{'ID':<10} {'Name':<20} {'Grade'}")
        print("="*40)
        for s in self.students:
            print(f"{s.student_id:<10} {s.name:<20} {s.grade}")
        print("="*40 + "\n")