from student import Student
from datetime import date
from course import Course

if __name__ == "__main__":
    s1 = Student("Jake", "Sparrow", "jake.sparrow@acme.com", date(1993, 6, 5))
    s1.print()

    # s2 = Student("John", "Doe", "john.doe@gmail.com", 5)
    # s2.print()

    d426 = Course("D426", "Data Management - Foundations", 3)
    d427 = Course("D427", "Data Management - Applications", 4)

    s1.addCourse(d426)
    s1.addCourse(d427)
    s1.print()