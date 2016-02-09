#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
Author : eric fourrier

Purpose : Some Helpers
"""

import json
import codecs

def write_to_json(data, file_path):
    """ write tweet by tweet to json """
    with codecs.open(file_path, 'a', encoding='utf-8') as f:
        json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)
