from datetime import date


class Student:

    def __init__(self, firstName: str, lastName: str, emailAddress: str, dateOfBirth: date) -> None:
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth

    def getFirstName(self) -> str:
        return self.__firstName
    
    def getLastName(self) -> str:
        return self.__lastName
    
    def getDateOfBirth(self) -> date:
        return self.__dateOfBirth

