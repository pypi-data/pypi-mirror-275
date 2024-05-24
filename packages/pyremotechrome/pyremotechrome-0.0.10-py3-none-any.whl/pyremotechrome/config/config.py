from typing import Any
from os.path import dirname, realpath
from json import load as json_load

class _Dict(object):

    def __init__(self, *args, **kwargs) -> None:
        """DOCSTRING"""
        for key in kwargs:
            value = kwargs[key]
            self.__setattr__(key, value)

        for arg in args:
            if not isinstance(arg, dict):
                raise TypeError("None key arguments must be dictionary")

            for key in arg:
                value = arg[key]
                self.__setattr__(key, value)

    def __setattr__(self, key: Any, value: Any, depth: int = 0) -> None:
        """DOCSTRING"""
        if isinstance(value, dict):
            self.__setattr__(key, _Dict(value), depth + 1)
        else:
            super().__setattr__(key, value)



class Conf(_Dict):
    
    def __init__(self) -> None:
        conf_path = f"{dirname(realpath(__file__))}/config.json"
        with open(conf_path) as f:
            parsed = json_load(f)
            super().__init__(parsed)
