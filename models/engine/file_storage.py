#!/usr/bin/python3

"""the module contains a class used for serialization
and deserialization process"""

import json
import os


class FileStorage:
    """FileStorage class containing methods for
    creating, storing and restoring file data"""

    __file_path = 'obj.json'
    __objects = {}

    def all(self):
        """returns all the stored objects"""
        return self.__objects

    def new(self, obj):
        """stores a new object that is not stored previously"""
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_key] = obj

    def save(self):
        """encodes objects and writes it to json file
        """
        json_data = {}
        for key, value in self.__objects.items():
            json_data[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)

    def reload(self):
        """decodes from json file to object if the file exists
        """
        from models.base_model import BaseModel
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                file_content = f.read()
            if file_content:
                json_data = json.loads(file_content)
                for key, value in json_data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
