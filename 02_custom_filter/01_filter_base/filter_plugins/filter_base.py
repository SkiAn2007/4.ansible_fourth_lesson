#!/usr/bin/python
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
