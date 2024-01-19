from student import Student
from datetime import date

if __name__ == "__main__":
    s1 = Student("Jake", "Sparrow", "jake.sparrow@acme.com", date(1993, 6, 5))
    print(s1.getFirstName())
    print(s1.getLastName())
    print(s1.getDateOfBirth())

    # s1.setFirstName("")
    # print(s1.getFirstName())

    s2 = Student("John", "Doe", "john.doe@gmail.com", 5)
    s2.print()