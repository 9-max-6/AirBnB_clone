#!/usr/bin/python3
"""
module - FileStorage
"""
import json


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "hard_storage.py"
    __objects = {}

    def __init__(self, *args, **kwargs):
        pass

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = self.__dict__["id"] + str(type(self).__name__)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing"""
        try:
            g = open(FileStorage.__objects, 'r', encoding="utf-8")
            FileStorage.__objects = json.load(g)
        except FileNotFoundError:
            pass
