# -*- coding: utf-8 -*-

import re

FILENAME_KEY = '__filename'

VARIABLE_PATTERN = re.compile(r'\$[_A-Za-z][_A-Za-z0-9]*\$')
