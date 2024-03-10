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
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json_obj = {}
            for key, value in self.__objects.items():
                json_obj[key] = value.to_dict()
                f.write(json.JSONEncoder().encode(json_obj))

    def reload(self):
        """decodes from json file to object if the file exists
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                file_content = f.readlines()
            if len(file_content) > 0:
                file_txt = ''.join(file_content)
            else:
                file_txt = '{}'
            self.__objects = json.JSONDecoder().decode(file_txt)
