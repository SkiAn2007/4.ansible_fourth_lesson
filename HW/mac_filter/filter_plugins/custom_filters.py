#!/usr/bin/python

from ansible.errors import (
    AnsibleFilterTypeError
)
import re


def mac_normalizer(input_str):
    '''
        convert input string into string with : separator
    '''
    if not isinstance(input_str, str):
        raise AnsibleFilterTypeError("String type is expected, "
                                     "got type %s instead" % type(input_str))
    if not re.search('[0-9a-fA-F]{12}', input_str) or len(input_str) != 12:
        raise AnsibleFilterTypeError("seems like its not mac address")
    return ':'.join(input_str[i:i+2] for i in range(0, 12, 2)).lower()

class FilterModule(object):
    def filters(self):
        return {
            'mac_normalizer': mac_normalizer
        }
