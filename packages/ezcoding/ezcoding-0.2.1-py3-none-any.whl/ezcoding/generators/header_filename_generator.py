# -*- coding: utf-8 -*-

import os
from typing import AnyStr, Optional

from ezcoding.generator import Generator
from ezcoding.const import FILENAME_KEY


class HeaderFilenameGenerator(Generator):

    def __init__(self, key: Optional[AnyStr] = None, extension: Optional[AnyStr] = None):
        self.__key: AnyStr = FILENAME_KEY
        self.__extension: AnyStr = 'h'

        if isinstance(key, str):
            self.__key = key
        if isinstance(extension, str):
            self.__extension = extension

    def generate(self, *args, **kwargs) -> AnyStr:
        assert self.__key in kwargs
        filename = os.path.basename(kwargs[self.__key])
        basename, ext = os.path.splitext(filename)
        return f'{basename}.{self.__extension}'
