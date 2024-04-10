#!/usr/bin/python3
"""
module - FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User
from  models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


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
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as g:
                new_dict = json.load(g)
                for key, value in new_dict.items():
                    class_name = value['__class__']
                    obj = eval(f'{class_name}(**value)')
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    def delete(self, obj):
        """a method to delete an object based on the key"""
        self.reload()
        del self.__objects[obj]
        self.save()
        self.reload()
