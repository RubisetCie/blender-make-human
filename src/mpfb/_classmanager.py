"""This module provides a class for managing blender classes"""

import bpy
from bpy.utils import register_class, unregister_class
from . import get_preference

class ClassManager:

    """This class keeps track of blender classes and ensures that they
    get properly registered and unregistered"""

    __stack = None  # use a class attribute as classes stack
    __isinitialized = False

    def __init__(self):
        if not type(self).__isinitialized:  # Ensure ClassManager is only registered once
            type(self).__stack = []
            type(self).__isinitialized = True
        else:
            raise RuntimeError("ClassManager must be a singleton")

    def getClassStack(self):
        return type(self).__stack

    @classmethod
    def isinitialized(self):
        return self.__isinitialized

    @classmethod
    def add_class(cls, append_class):
        """Add a blender class to be managed"""
        if cls.__stack is None:
            raise RuntimeError("ClassManager is not initialized!")
        else:
            cls.__stack.append(append_class)

    @classmethod
    def register_classes(cls):
        """Iterate over all managed classes and ask blender to register
        them. This should only be called from the register() method."""
        if cls.__stack is None:
            raise RuntimeError("ClassManager is not initialized!")
        else:
            for reg_class in cls.__stack:
                register_class(reg_class)

    @classmethod
    def unregister_classes(cls):
        """Iterate over all managed classes and ask blender to unregister
        them. This should only be called from the unregister() method."""
        if cls.__stack is None:
            raise RuntimeError("ClassManager is not initialized!")
        else:
            for ureg_class in cls.__stack:
                try:
                    unregister_class(ureg_class)
                except Exception as e:
                    # This often happens during unit tests, and it's not a big deal
                    pass
