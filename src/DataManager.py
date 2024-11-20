import json
import members.Member as Member
from typing import Union
from lib.FileAccess import FileAccess
from lib.JsonEditor import JsonEditor

class DataManager:
    def __init__(self, file_path: str) -> None:
        """
        Initializes the DataManager with an optional file path for storing data.
        """
        self.file_path = file_path
        self.Students: list[Member.Student] = []
        self.Teachers: list[Member.Teacher] = []
        self.NonTeachingStaffs: list[Member.NonTeachingStaff] = []
        self.load_data()

    def Add(self, person: Union[Member.Student, Member.Teacher, Member.NonTeachingStaff]) -> None:
        """
        Adds a new person (Student, Teacher, or Non-Teaching Staff) to the appropriate list.
        """
        if isinstance(person, Member.Student):
            self.Students.append(person)
        elif isinstance(person, Member.Teacher):
            self.Teachers.append(person)
        elif isinstance(person, Member.NonTeachingStaff):
            self.NonTeachingStaffs.append(person)
        else:
            raise ValueError("Invalid type of person provided for addition.")
        self.save_data()

    def Update(self, person_id: str, updated_person: Union[Member.Student, Member.Teacher, Member.NonTeachingStaff]) -> bool:
        """
        Updates an existing member based on their ID.
        Returns True if the update is successful, otherwise False.
        """
        lists = {
            "Students": self.Students,
            "Teachers": self.Teachers,
            "NonTeachingStaffs": self.NonTeachingStaffs,
        }
        
        for member_type, member_list in lists.items():
            for i, member in enumerate(member_list):
                if hasattr(member, "admit_id") and member.admit_id == person_id:
                    member_list[i] = updated_person
                    self.save_data()
                    return True
                elif hasattr(member, "employee_id") and member.employee_id == person_id:
                    member_list[i] = updated_person
                    self.save_data()
                    return True
        return False

    def Remove(self, person_id: str) -> bool:
        """
        Removes a person from the data lists based on their ID.
        Returns True if the person is successfully removed, otherwise False.
        """
        lists = {
            "Students": self.Students,
            "Teachers": self.Teachers,
            "NonTeachingStaffs": self.NonTeachingStaffs,
        }
        
        for member_type, member_list in lists.items():
            for i, member in enumerate(member_list):
                if hasattr(member, "admit_id") and member.admit_id == person_id:
                    del member_list[i]
                    self.save_data()
                    return True
                elif hasattr(member, "employee_id") and member.employee_id == person_id:
                    del member_list[i]
                    self.save_data()
                    return True
        return False

    def save_data(self) -> None:
        """
        Saves the current state of data to the JSON file.
        """
        data = {
            "Students": [student.__dict__ for student in self.Students],
            "Teachers": [teacher.__dict__ for teacher in self.Teachers],
            "NonTeachingStaffs": [staff.__dict__ for staff in self.NonTeachingStaffs],
        }
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully.")

    def load_data(self) -> None:
        """
        Loads data from the JSON file into the respective lists.
        """
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.Students = [Member.Student(**student) for student in data.get("Students", [])]
                self.Teachers = [Member.Teacher(**teacher) for teacher in data.get("Teachers", [])]
                self.NonTeachingStaffs = [
                    Member.NonTeachingStaff(**staff) for staff in data.get("NonTeachingStaffs", [])
                ]
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No data file found. Starting with empty lists.")
        except json.JSONDecodeError:
            print("Error loading JSON data. Starting with empty lists.")
