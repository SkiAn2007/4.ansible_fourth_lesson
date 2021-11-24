#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: example_py
author: Pupkin V.
short_description: Example module concat 3 strings
description:
  - Concating 3 strings for module writing example
version_added: 1.0.0
options:
  string1:
    description:
      - first string
      - This is a required parameter
    type: str
  string2:
    description:
      - second string
    type: str
  string3:
    description:
      - third string
    type: str
'''

EXAMPLES = r'''
- name: Concat 3 strings
  example_py:
    string1: Just
    string2: Do
    string3: It
  connection: local
'''

RETURN = r'''
msg:
  description: Errors if occured
  returned: always
  type: str
  sample: ""
result_str:
  description: final string
  returned: always
  type: str
  sample: Just do it
rc:
  description: Return code
  returned: always
  type: int
  sample: 0
'''

from ansible.module_utils.basic import (
    AnsibleModule
)


def example_function(str1):
    failed = False
    msg = "Success"
    rc = 0
    # Формируем конечную строку
    try:
        result = str1
    except TypeError as e:
        failed = True
        result = ""
        msg = "TypeError. str1 is not a string"
        rc = 1
    return(failed, result, rc, msg)


def main():
    # Задаем аргументы модуля
    module_args = dict(
        string1=dict(required=True, type='str')
    )
    # Создаем объект - модуль
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    # Получаем из модуля аргументы
    string1 = module.params["string1"]
    # Вызываем нашу функцию
    lc_return = example_function(string1)
    # Если задача зафейлилась
    if lc_return[0]:
        module.fail_json(changed=False,
                         failed=lc_return[0],
                         result_str=lc_return[1],
                         rc=lc_return[2],
                         msg=lc_return[3])
    # Если задача успешно завершилась
    else:
        module.exit_json(changed=False,
                         failed=lc_return[0],
                         result_str=lc_return[1],
                         rc=lc_return[2],
                         msg=lc_return[3])


if __name__ == "__main__":
    main()
