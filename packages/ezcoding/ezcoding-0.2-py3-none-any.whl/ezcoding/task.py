# -*- coding: utf-8 -*-

import os
import importlib.util
from typing import Dict, AnyStr, Union, Optional

from ezcoding.template import Template
from ezcoding.generator import Generator
from ezcoding.ui import Application, Editor
from ezcoding.const import FILENAME_KEY
from ezcoding.utils import create_variable_macro


class Task(object):

    def __init__(self, template_dir: AnyStr, template_name: AnyStr):
        self.__template_directory: AnyStr = template_dir
        self.__template_name: AnyStr = template_name

    def run(self, filename: AnyStr, values: Optional[Dict[AnyStr, Union[AnyStr, Generator]]] = None):
        template = self.__load_template()
        assert isinstance(template, Template)

        value_dict = self.__create_values(filename, template, values)

        text = template.complete(value_dict)
        self.__write_file(filename, text)

    def __load_template(self) -> Union[None, Template]:
        try:
            filename = os.path.join(self.__template_directory, f'{self.__template_name}.py')
            if not os.path.isfile(filename):
                return None
            spec = importlib.util.spec_from_file_location(self.__template_name, filename)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            template = module.get_template()
            return template
        except:
            return None

    @staticmethod
    def __create_values(
            filename: AnyStr,
            template: Template,
            values: Optional[Dict[AnyStr, Union[AnyStr, Generator]]] = None)\
            -> Dict[AnyStr, Union[AnyStr, Generator]]:
        value_dict = values if isinstance(values, dict) else dict()
        if FILENAME_KEY not in value_dict:
            value_dict[FILENAME_KEY] = filename
        template.update_values(value_dict)
        variables = template.get_variables()
        edit_variables = False
        for variable in variables:
            if variable not in value_dict:
                value_dict[variable] = create_variable_macro(variable)
                edit_variables = True
        if edit_variables:
            Task.__edit_values(value_dict)
        return value_dict

    @staticmethod
    def __edit_values(values: Dict[AnyStr, Union[AnyStr, Generator]]):
        app = Application()
        dlg = Editor(values)
        dlg.show()
        app.exec()

    @staticmethod
    def __write_file(filename: AnyStr, text: AnyStr):
        with open(filename, 'w') as fp:
            fp.write(text)
