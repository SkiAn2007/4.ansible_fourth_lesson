#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
import requests as r

DOCUMENTATION = r'''
---
module: healthcheck
author: Pupkin V.
short_description: healthcheck of site
description:
  - healthcheck of site with or without TLS
version_added: 1.0.0
requirements:
  - requests
  - python >= 3.6
options:
  addr:
    description:
      - Address of site we want to check
      - This is a required parameter
    type: str
  tls:
    description:
      - Whether site using certificates or not
      - Default value is 'True'
    type: bool
'''

EXAMPLES = r'''
- name: Check availability of site
  healthcheck:
    addr: mysite.example
  connection: local

- name: Check availability of site without certs
  healthcheck:
    addr: mysite.example
    tls: false
  connection: local
'''

RETURN = r'''
msg:
  description: Errors if occured
  returned: always
  type: str
  sample: ""
site_status:
  description: State status
  returned: always
  type: str
  sample: Available
rc:
  description: Return code
  returned: always
  type: int
  sample: 200
'''

def main():
    # Аргументы для модуля
    arguments = dict(
        addr=dict(required=True, type='str'),
        tls=dict(type='bool', default="True")
    )
    # Создаем объект - модуль
    module = AnsibleModule(
        argument_spec=arguments,
        supports_check_mode=False
    )
    # Получаем аргументы
    addr = module.params["addr"]
    tls = module.params["tls"]

    schema = 'https' if tls else 'http'
    msg = 'everything is ok'
    try:
        response = r.get('{0}://{1}'.format(schema, addr))
        site_status = response.status_code
        rc = 0
    except r.exceptions.RequestException as e:  # This is the correct syntax
        msg = 'exception happen during requests execution'
        site_status = 0

    if site_status != 200:
        if site_status != 0:
            msg = 'something could went wrong'
        rc = 1

    # Если задача зафейлилась
    if rc:
        module.fail_json(changed=False,
                         failed=True,
                         result_str=site_status,
                         rc=rc,
                         msg=msg)
    # Если задача успешно завершилась
    else:
        module.exit_json(changed=False,
                         failed=False,
                         result_str=site_status,
                         rc=rc,
                         msg=msg)

if __name__ == "__main__":
    main()
