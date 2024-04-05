#!/usr/bin/python3
"""
Module - class baseModel

Defines all common attributes/methods for other classes
"""
import uuid
import datetime


class BaseModel:
    """
    Class that defines all common attributes/methods for other classes

    Attributes:
    id - string to be assigned with uuid when an instance is created
    created_at - datetime when an instance is created
    updated_at - assigned with the current datetime when an instance is created
    and is updated everytime the object is changed.

    Methods:
    __str__ - prints the object [<class name>] (<self.id>) <self.__dict__>
    save(self) - updates the public instance attribute updated_at
    to_dict() - returns a dict with all keys/values of the __dict__ instance

    """
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.get_time()
            self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    a = datetime.datetime.strptime(value, date_format)
                    self.__dict__[key] = a
                else:
                    self.__dict__[key] = value

    @staticmethod
    def get_time():
        """static method to determine current time"""
        current_dt = datetime.datetime.now()
        return current_dt.isoformat()

    def __str__(self):
        """A method to return string rep of the instanc"""
        a = self.__class__.__name__
        b = self.id
        c = self.__dict__
        return "[{}] ({}) {}".format(a, b, c)

    def save(self):
        """updates the updated at instance of a variable."""
        if hasattr(self, "updated_at"):
            setattr(self, "updated_at", self.get_time())
        else:
            raise Exception("broken object")

    def to_dict(self):
        """
        A function to return dict rep of the object"""
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
