from datetime import date
import re


class Student:

    # Constructor
    def __init__(self, firstName: str, lastName: str, emailAddress: str, dateOfBirth: date) -> None:
        self.__firstName = firstName
        self.__lastName = lastName
        if self.isValidEmail(emailAddress):
            self.__emailAddress = emailAddress
        else:
            raise ValueError(f"Invalid email address: '{emailAddress}'")
        self.__dateOfBirth = dateOfBirth

    # Getters
    def getFirstName(self) -> str:
        return self.__firstName
    
    def getLastName(self) -> str:
        return self.__lastName
    
    def getEmailAddress(self) -> str:
        return self.__emailAddress
    
    def getDateOfBirth(self) -> date:
        return self.__dateOfBirth
    
    # Setters
    def setFirstName(self, firstName) -> None:
        if len(firstName) < 1:
            raise ValueError("Invalid name")
        
        self.__firstName = firstName

    def setLastName(self, lastName) -> None:
        if len(lastName) < 1:
            raise ValueError("Invalid name")
        
        self.__lastName = lastName

    # Other
    def print(self) -> None:
        print(f"Name: {self.__firstName} {self.__lastName},", end="")
        print(f"\tDOB: {self.__dateOfBirth}", end="")
        print(f"\tEmail: {self.__emailAddress}")

    def isValidEmail(self, emailAddress: str) -> bool:
        # It should be a string
        if type(emailAddress) != str:
            return False
        
        # There should be no spaces
        if bool(re.search(r"\s", emailAddress)):
            return False

        # There should only be one '@' character
        # and it should not the first or last character
        index = emailAddress.find('@')
        return index > 0 and index != (len(emailAddress) - 1) and (emailAddress.count('@') == 1)

