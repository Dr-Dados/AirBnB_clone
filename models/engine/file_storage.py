
#!/usr/bin/python3

import json
from datetime import datetime
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objetcs

    def new(self, obj):
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__[key] = obj

        def save(self):
            """
            serializes FileStorage.__objects
            """
            with open(FileStorage.__file_path, 'w+') as f:
                dictofobjs = {}
                for key, value in FileStorage.__objects.items():
                    dictofobj[key] = value.to_dict()
                json.dump(dictofobjs, f)

            def reload(self):
                """
                deserialzes instances got from json file
                """
             try:
            with open(FileStorage.__file_path, 'r') as f:
                dictofobjs = json.loads(f.read())
                from models.base_model import BaseModel
                from models.user import User
                for key, value in dictofobjs.items():
                    if value['__class__'] == 'BaseModel'
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value['__class__'] == 'User':
                        FileStorage.__objects[key] = User(**value)
                   except FileNotFoundError:
            pass
