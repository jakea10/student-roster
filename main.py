from student import Student
from datetime import date

if __name__ == "__main__":
    student1 = Student("Jake", "Sparrow", date(1993, 6, 5))
    print(student1.getFirstName())
    print(student1.getLastName())
    print(student1.getDateOfBirth())