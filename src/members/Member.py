from typing import List, Optional
from datetime import date

# Base class for all members
class Person:
    def __init__(self, name: str, dob: date, contact: Optional[str] = None) -> None:
        self.name = name
        self.dob = dob
        self.contact = contact

    def get_age(self) -> int:
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def __str__(self) -> str:
        return f"Name: {self.name}, DOB: {self.dob}, Contact: {self.contact}"

    def __repr__(self) -> str:
        return f"Person(name={self.name}, dob={self.dob}, contact={self.contact})"


# Student class
class Student(Person):
    def __init__(self, name: str, dob: date, admit_id: str, grade: str) -> None:
        super().__init__(name, dob)
        self.admit_id = admit_id
        self.grade = grade

    def calculate_fees(self) -> float:
        # Dummy logic for fees calculation (you can replace it with actual logic)
        return 20000.0  # Example fee amount

    def __str__(self) -> str:
        return f"{super().__str__()}, Admit ID: {self.admit_id}, Grade: {self.grade}"


# Teacher class
class Teacher(Person):
    def __init__(self, name: str, dob: date, employee_id: str, subject: str, salary: float) -> None:
        super().__init__(name, dob)
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary

    def get_salary(self) -> float:
        return self.salary

    def assign_subject(self, subject: str) -> None:
        self.subject = subject

    def __str__(self) -> str:
        return f"{super().__str__()}, Employee ID: {self.employee_id}, Subject: {self.subject}, Salary: {self.salary}"


# Non-Teaching Staff class
class NonTeachingStaff(Person):
    def __init__(self, name: str, dob: date, employee_id: str, role: str, salary: float) -> None:
        super().__init__(name, dob)
        self.employee_id = employee_id
        self.role = role
        self.salary = salary

    def get_salary(self) -> float:
        return self.salary

    def assign_role(self, role: str) -> None:
        self.role = role

    def __str__(self) -> str:
        return f"{super().__str__()}, Employee ID: {self.employee_id}, Role: {self.role}, Salary: {self.salary}"


# Utility functions
def create_student(name: str, dob: date, admit_id: str, grade: str) -> Student:
    return Student(name, dob, admit_id, grade)


def create_teacher(name: str, dob: date, employee_id: str, subject: str, salary: float) -> Teacher:
    return Teacher(name, dob, employee_id, subject, salary)


def create_non_teaching_staff(name: str, dob: date, employee_id: str, role: str, salary: float) -> NonTeachingStaff:
    return NonTeachingStaff(name, dob, employee_id, role, salary)