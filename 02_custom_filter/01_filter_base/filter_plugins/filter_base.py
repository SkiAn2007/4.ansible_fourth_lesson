#!/usr/bin/python

# from ansible.errors import (
#     AnsibleFilterTypeError
# )

def filter_function(variable):
    '''
        function doc
    '''
    return variable


class FilterModule(object):
    def filters(self):
        return {
            'filter_function': filter_function
        }
