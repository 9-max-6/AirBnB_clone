#!/usr/bin/python3
"""
module - FileStorage
"""
import json
from models import base_model


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "storage.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        pass

    def all(self):
        """returns the dictionary __objects"""
        self.save()
        self.reload()
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.to_dict()["__class__"] + "." + obj.to_dict()["id"]
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing"""
        try:
            g = open(FileStorage.__file_path, 'r', encoding="utf-8")
            new_dict = json.load(g)
            for key, value in new_dict.items():
                obj = base_model.BaseModel(**value)
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    def delete(self, obj):
        """a method to delete a key based on the """
        self.reload()
        del self.__objects[obj]
        self.save()
        self.reload()
