# -*- coding: utf-8 -*-

import os
import json
from typing import Tuple, AnyStr, Union
from argparse import ArgumentParser

from ezcoding import Task


def parse_arguments() -> Tuple[AnyStr, AnyStr]:
    parser = ArgumentParser()
    parser.add_argument('--filename', type=str, required=True)
    parser.add_argument('--template', type=str, required=True)
    values = parser.parse_args()
    return values.filename, values.template


def parse_template_dir() -> Union[AnyStr, None]:
    home_path = os.path.expanduser('~')
    config_path = os.path.join(home_path, '.ezcoding')
    if not os.path.isfile(config_path):
        return None
    with open(config_path, 'r') as fp:
        data = json.load(fp)
    if 'template_dir' in data:
        return data['template_dir']
    return None


def main():
    template_dir = parse_template_dir()
    if template_dir is None:
        return
    filename, template_name = parse_arguments()
    task = Task(template_dir=template_dir, template_name=template_name)
    task.run(filename)


if __name__ == '__main__':
    main()
