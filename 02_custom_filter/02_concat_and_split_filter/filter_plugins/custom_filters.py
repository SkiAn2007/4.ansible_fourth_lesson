#!/usr/bin/python

from ansible.errors import (
    AnsibleFilterTypeError
)


def concat_filter(var_a, var_b):
    '''
        concat 2 strings
    '''
    if not isinstance(var_a, str):
        raise AnsibleFilterTypeError("String type is expected, "
                                     "got type %s instead" % type(var_a))

    if not isinstance(var_b, str):
        raise AnsibleFilterTypeError("String type is expected, "
                                     "got type %s instead" % type(var_b))

    return str(var_a + var_b)


def split_filter(input_str, input_separator=' '):
    '''
        split string into list of strings with particular separator
    '''
    if not isinstance(input_str, str):
        raise AnsibleFilterTypeError("String type is expected, "
                                     "got type %s instead" % type(input_str))
    return str(input_str).split(sep=input_separator)


class FilterModule(object):
    def filters(self):
        return {
            'concat_filter': concat_filter,
            'split_filter': split_filter
        }
