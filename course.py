class Course:

    # Constructor
    def __init__(self, courseID: str, courseName: str, creditUnits: int) -> None:
        self.__courseID = courseID
        self.__courseName = courseName
        self.__creditUnits = creditUnits

    # Getters
    def getCourseID(self) -> str:
        return self.__courseID
    
    def getCourseName(self) -> str:
        return self.__courseName
    
    def getCreditUnits(self) -> int:
        return self.__creditUnits
    
    # Other
    def print(self) -> None:
        print(f"{self.__courseID} - {self.__courseName}, {self.__creditUnits} CUs")