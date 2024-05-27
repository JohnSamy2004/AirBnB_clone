#!/usr/bin/python3
'''base model'''
import uuid
from datetime import datetime
import models

class BaseModel:
    '''base class'''
    def __init__(self, *args, **kwargs):
        '''initialize'''
        if kwargs:
            dt_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], dt_format)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        kwargs['created_at'], dt_format)
                else:
                    setattr(self, key, value)
        else:     
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''should print: [<class name>] (<self.id>) <self.__dict__>'''

        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute
        updated_at with the current datetime'''

        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        '''returns a dictionary containing all keys/values of
        __dict__ of the instance'''

        cool_dict = self.__dict__.copy()
        cool_dict['__class__'] = self.__class__.__name__
        cool_dict['created_at'] = self.created_at.isoformat()
        cool_dict['updated_at'] = self.updated_at.isoformat()
        return cool_dict