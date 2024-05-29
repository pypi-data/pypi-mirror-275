# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser
from typing import AnyStr, Optional

from ezcoding.generator import Generator


class AuthorGenerator(Generator):

    def __init__(self, default_value: Optional[AnyStr] = None):
        self.__default_value: AnyStr = str()
        if isinstance(default_value, str):
            self.__default_value = default_value

    def generate(self, *args, **kwargs) -> AnyStr:
        home_path = os.path.expanduser('~')
        gitconfig_path = os.path.join(home_path, '.gitconfig')
        if os.path.isfile(gitconfig_path):
            config_parser = ConfigParser()
            config_parser.read(gitconfig_path, encoding='utf-8')
            return config_parser.get('user', 'name')
        return self.__default_value
